# by ZePytime, available at: https://github.com/ZePytime/numworks_paint

from math import *
from kandinsky import *
from ion import *
from time import *
c=color
f=fill_rect
k=keydown
o=sleep
a=True
b=0.01
S=[320,222]
z=255
d=[c(z,z,z),c(0,0,0),c(z,0,0),c(z,z,0),c(0,z,0),c(0,z,z),c(z,0,z)]
e=[]
g=8
h={KEY_ONE:1,KEY_TWO:2,KEY_THREE:3,KEY_FOUR:4,KEY_FIVE:5,KEY_SIX:6,KEY_SEVEN:7,KEY_EIGHT:8,KEY_NINE:9}
i=[0,0]
j=8
l=c(0,0,0)
class u:
  def __init__(self,p,q,r):
    self.p=p
    self.ai=[p[0]+q[0],p[1]+q[1]]
    self.q=q
    self.r=r
    f(self.p[0],self.p[1],self.q[0],self.q[1],self.r)
  def s(self,v):
    global j
    aj,al=v[0],v[1]
    aa,ab=v[0]+j,v[1]+j
    ac,ad=self.p
    ae,af=self.ai
    ag=aj<ae and aa>ac
    ah=al<af and ab>ad
    return ag and ah
def n(x,y):
  global j
  global i
  global l
  global m
  if x>S[0]:
    x=0
  elif y>S[1]:
    y=0
  elif x<0-j:
    x=S[0]
  elif y<0-j:
    y=S[1]
  if not a:
    f(i[0],i[1],j,j,m)
    m=get_pixel(x,y)
  for t in e:
    if t.s([x,y]):
      l=t.r
      break
  f(x,y,j,j,l)
  if j>2:
    f(x+1,y+1,j-2,j-2,c(130,130,130))
  i=[x,y]
  o(b)
def ak():
  global a
  global j
  global g
  global b
  global m
  global h
  global e
  x=0
  for r in d:
    x+=10
    e.append(u([x,5],[20,20],r))
    x+=20
  n(160,110)
  while True:
    if k(KEY_UP):
      n(i[0],i[1]-1)
    if k(KEY_DOWN):
      n(i[0],i[1]+1)
    if k(KEY_LEFT):
      n(i[0]-1,i[1])
    if k(KEY_RIGHT):
      n(i[0]+1,i[1])
    if k(KEY_PLUS):
      o(0.1)
      b-=0.001
    if k(KEY_MINUS):
      o(0.1)
      b+=0.001
    if k(KEY_OK):
      o(0.25)
      a=not a
      if a:
        j=g
      else:
        g=j
        f(i[0],i[1],j,j,l)
        m=l
        j=1
    if a:
      for w in h.keys():
        if k(w):
          f(i[0],i[1],j,j,l)
          j=h[w]
          break
ak()
