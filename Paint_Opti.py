# by ZePytime, available at: https://github.com/ZePytime/numworks_paint

from math import *
from kandinsky import *
from ion import *
from time import *
h=color
w=keydown
i=255
j=150
m=fill_rect
S=[320,222];B=h(240,i,240);G=h(j,j,j)
P=[h(i,i,i),h(0,0,0),h(i,0,0),h(i,i,0),h(0,i,0),h(0,i,i),h(i,0,i)]
class A:
 def __init__(s):s.a=True;s.b=0.01;s.j=8;s.g=8;s.i=[0,0];s.l=h(0,0,0);s.m=B;s.e=[]
def f(xy,z,c):m(xy[0],xy[1],z,z,c)
class U:
 def __init__(s,p,q,r):s.p=p;s.q=[p[0]+q,p[1]+q];s.r=r;f(p,q,r)
 def s(s,v,t):
  x,y=v[0]+t.j//2,v[1]+t.j//2
  return s.p[0]<=x<=s.q[0] and s.p[1]<=y<=s.q[1]
def o(x,y,t):
 if x>S[0]:x=0
 elif y>S[1]:y=0
 elif x<0-t.j:x=S[0]
 elif y<0-t.j:y=S[1]
 if not t.a:f(t.i,t.j,t.m);t.m=get_pixel(x,y)
 for v in t.e:
  if v.s([x,y],t):t.l=v.r;break
 if t.a:
  f([x,y],t.j,t.l)
  if t.j>2:f([x+1,y+1],t.j-2,G)
 else:f([x,y],t.j,G)
 t.i=[x,y];sleep(t.b)
def p(t):
 x=0
 for r in P:x+=10;t.e.append(U([x,5],20,r));x+=20
 o(160,110,t)
 while 1:
  if w(KEY_UP):o(t.i[0],t.i[1]-1,t)
  elif w(KEY_DOWN):o(t.i[0],t.i[1]+1,t)
  if w(KEY_LEFT):o(t.i[0]-1,t.i[1],t)
  elif w(KEY_RIGHT):o(t.i[0]+1,t.i[1],t)
  if w(KEY_PLUS):sleep(0.05);t.b=max(0,t.b-0.002)
  elif w(KEY_MINUS):sleep(0.05);t.b=min(0.2,t.b+0.002)
  if w(KEY_OK):
   sleep(0.25)
   if t.a:
    f(t.i,t.j,t.l);t.m=t.l;t.g=t.j;t.a=False;t.j=1
   else:t.a=True;t.j=t.g
  if t.a:
   if w(KEY_MULTIPLICATION):
    sleep(0.25);f(t.i,t.j,t.l);t.j=min(10,t.j+1);o(t.i[0],t.i[1],t)
   elif w(KEY_DIVISION):
    sleep(0.25);f(t.i,t.j,t.l);t.j=max(1,t.j-1);o(t.i[0],t.i[1],t)
m(0,0,S[0],S[1],B)
T=A()
p(T)
