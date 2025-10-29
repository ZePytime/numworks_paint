# by ZePytime, available at: https://github.com/ZePytime/numworks_paint

from math import *
from kandinsky import *
from ion import *
from time import *

# setup constants
SCREEN_WIDTH, SCREEN_HEIGHT = 320, 222
BACKGROUND_COLOR = color(240, 255, 240)
COLOR_CURSOR_GRAY = color(150, 150, 150)
PALETTE = [color(255, 255, 255), color(0, 0, 0), color(255, 0, 0), color(255, 255, 0), color(0, 255, 0), color(0, 255, 255), color(255, 0, 255)]


class State:
  def __init__(self):
    # setup initial parameters
    self.all_color_zone = []
    self.is_drawing = True
    self.speed = 0.01
    # setup cursor parameters
    self.cursor_size = 8
    self.last_size = 8
    self.current_coordinates = [0, 0]
    self.color_cursor = color(0, 0, 0)
    self.last_color = color(0, 0, 0)


def draw_square(xy, size, color):
    """Draws a square at the given coordinates with the specified size and color."""
    fill_rect(xy[0], xy[1], size, size, color)


class ColorZone:
  def __init__(self, top_left, size, color):
    """Initializes a color zone with given coordinates, size, and color."""
    self.top_left = top_left
    self.bottom_right = [top_left[0]+size, top_left[1]+size]
    self.size = size
    self.color = color
    draw_square(self.top_left, self.size, self.color)

  def in_color_zone(self, co, state):
    """Verify if the cursor is inside the color zone."""
    cx, cy = co[0] + state.cursor_size//2, co[1] + state.cursor_size//2
    return self.top_left[0] <= cx <= self.bottom_right[0] and self.top_left[1] <= cy <= self.bottom_right[1]


def setup_color_zones(state):
  """Initializes color zones (color palette) on the screen."""
  state.all_color_zone = []
  x_offset = 0
  for color in PALETTE:
    x_offset += 10
    state.all_color_zone.append(ColorZone([x_offset, 5], 20, color))
    x_offset += 20


def out_screen(x, y, state):
  """Checks and adjusts the coordinates (x, y) to ensure they stay within screen bounds."""
  if x>SCREEN_WIDTH:
    x=0
  elif y>SCREEN_HEIGHT:
    y=0
  elif x<0-state.cursor_size:
    x=SCREEN_WIDTH
  elif y<0-state.cursor_size:
    y=SCREEN_HEIGHT
  return x, y


def move_cursor(x, y, state):
  """Moves the cursor to the new coordinates (x, y)."""
  
  # adjust coordinates to stay within screen bounds
  x, y = out_screen(x, y, state)
  
  # clear the previous cursor position if the cursor is not drawing
  if not state.is_drawing:
    draw_square(state.current_coordinates, state.cursor_size, state.last_color)
    state.last_color = get_pixel(x, y)
  
  # check if the cursor is in any color zone
  for color_zone in state.all_color_zone:
    if color_zone.in_color_zone([x,y], state):
      state.color_cursor = color_zone.color
      break
  
  # move the cursor to the new position
  if state.is_drawing:
    draw_square([x, y], state.cursor_size, state.color_cursor)
    if state.cursor_size > 2:
      # draw inner gray square for better visibility
      draw_square([x+1, y+1], state.cursor_size-2, COLOR_CURSOR_GRAY)
  else:
    # show gray cursor when not drawing
    draw_square([x, y], state.cursor_size, COLOR_CURSOR_GRAY)

  # update current coordinates
  state.current_coordinates = [x, y]
  # pause for a short duration to control speed
  sleep(state.speed)


def main(state):
  """Main function to run the paint application."""
  # setup background
  fill_rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR)

  # setup color zones (color palette)
  setup_color_zones(state)

  # initial cursor position
  move_cursor(160, 110, state)

  # main loop to handle user input
  while True:
    # Movement controls
    if keydown(KEY_UP):
      move_cursor(state.current_coordinates[0],state.current_coordinates[1]-1,state)
    elif keydown(KEY_DOWN):
      move_cursor(state.current_coordinates[0],state.current_coordinates[1]+1,state)
    if keydown(KEY_LEFT):
      move_cursor(state.current_coordinates[0]-1,state.current_coordinates[1],state)
    elif keydown(KEY_RIGHT):
      move_cursor(state.current_coordinates[0]+1,state.current_coordinates[1],state)
    
    # Speed controls
    if keydown(KEY_PLUS):
      sleep(0.05)
      state.speed-=0.002
      if state.speed < 0:
        state.speed = 0
    elif keydown(KEY_MINUS):
      sleep(0.05)
      state.speed+=0.002
      state.speed = min(state.speed, 0.2)

    # Draw controls
    if keydown(KEY_OK):
      sleep(0.25)
      state.is_drawing = not state.is_drawing
      if state.is_drawing:
        state.cursor_size = state.last_size
      else:
        state.last_size = state.cursor_size
        draw_square(state.current_coordinates, state.cursor_size, state.color_cursor) # erase the gray square used to identify the cursor
        state.last_color = state.color_cursor
        state.cursor_size = 1 # change the size of the cursor to simplify the memorization of pixels that should not be replaced during its movement

    # Cursor size controls
    if state.is_drawing:
      if keydown(KEY_MULTIPLICATION):
        sleep(0.25)
        state.cursor_size += 1
        # limit the cursor size to a maximum of 10
        state.cursor_size = min(state.cursor_size, 10)

      elif keydown(KEY_DIVISION):
        sleep(0.25)
        state.cursor_size -= 1
        # limit the cursor size to a minimum of 1
        state.cursor_size = max(state.cursor_size, 1)

# run the paint application
state = State()
main(state)
