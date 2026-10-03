# -*- coding: utf-8 -*-
"""Generate the section's SVG diagrams using exact solution formulas (stdlib only)."""
from __future__ import division
import os
import math
import io
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
BLUE, ORANGE, GREEN, GRAY = '#2563eb', '#d97706', '#159568', '#64748b'

class Figure(object):
    def __init__(self, title, height=480):
        self.h = height
        self.parts = [u'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="%d" viewBox="0 0 1080 %d" role="img" aria-labelledby="title"><title id="title">%s</title><rect width="1080" height="%d" fill="white"/><g font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" fill="#1e293b">' % (height, height, escape(title), height)]
        self.text(540, 30, title, 22)

    def text(self, x, y, value, size=16, color='#1e293b', anchor='middle'):
        self.parts.append(u'<text x="%g" y="%g" font-size="%g" fill="%s" text-anchor="%s">%s</text>' % (x, y, size, color, anchor, escape(value)))

    def line(self, points, color=GRAY, width=2, dash=False):
        self.parts.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%g" stroke-linejoin="round"%s/>' % (' '.join('%g,%g' % p for p in points), color, width, ' stroke-dasharray="6 5"' if dash else ''))

    def dot(self, x, y, color=BLUE, radius=5):
        self.parts.append('<circle cx="%g" cy="%g" r="%g" fill="%s"/>' % (x, y, radius, color))

    def arrow(self, a, b, color=GRAY, width=2):
        self.line([a,b], color, width)
        ang = math.atan2(b[1]-a[1], b[0]-a[0])
        pts = [b, (b[0]-8*math.cos(ang-.45),b[1]-8*math.sin(ang-.45)), (b[0]-8*math.cos(ang+.45),b[1]-8*math.sin(ang+.45))]
        self.parts.append('<polygon points="%s" fill="%s"/>' % (' '.join('%g,%g' % p for p in pts),color))

    def save(self, name):
        with io.open(os.path.join(ROOT,name), 'w', encoding='utf-8') as f:
            f.write(u'\n'.join(self.parts)+u'</g></svg>')

class Plot(object):
    def __init__(self, f, left, top, width, height, xr, yr, xlabel='x', ylabel='v'):
        self.f,self.left,self.top,self.w,self.h,self.xr,self.yr=f,left,top,width,height,xr,yr
        self.curve([(xr[0],0),(xr[1],0)], '#cbd5e1', 1)
        self.curve([(0,yr[0]),(0,yr[1])], '#cbd5e1', 1)
        f.text(left+width+12,self.xy(0,0)[1]+5,xlabel)
        f.text(self.xy(0,0)[0],top-12,ylabel)

    def xy(self,x,y):
        return (self.left+(x-self.xr[0])/(self.xr[1]-self.xr[0])*self.w,self.top+self.h-(y-self.yr[0])/(self.yr[1]-self.yr[0])*self.h)

    def curve(self, pts, color=BLUE, width=2.5, dash=False):
        self.f.line([self.xy(x,y) for x,y in pts],color,width,dash)

    def arrow(self,a,b,color=GRAY):
        self.f.arrow(self.xy(*a),self.xy(*b),color)

    def dot(self,p,color=BLUE):
        self.f.dot(*self.xy(*p),color=color)

    def label(self,x,y,text,color=GRAY,dx=0,dy=0,size=15):
        px,py=self.xy(x,y)
        self.f.text(px+dx,py+dy,text,size,color)

def samples(fn,end,n=240,start=0):
    return [fn(start+(end-start)*i/n) for i in range(n+1)]

def circle(p,r,color=BLUE,dash=False):
    p.curve(samples(lambda t:(r*math.cos(t),r*math.sin(t)),2*math.pi),color,2.5,dash)

def heading(f,x,title,subtitle):
    f.text(x,67,title,18)
    f.text(x,92,subtitle,14,GRAY)

# 1. Nullclines provide directions; the solution crosses them.
f=Figure(u'零增长曲线：先判断方向，再看轨迹怎样经过')
for left,center in [(90,290),(620,820)]:
    p=Plot(f,left,130,330,270,(-1.5,1.5),(-1.23,1.23))
    p.curve([(-1.5,0),(1.5,0)],ORANGE,2.5)
    p.curve([(0,-1.23),(0,1.23)],GREEN,2.5)
    p.dot((0,0),GRAY)
    if left==90:
        heading(f,center,u'两条线把平面分成四块',u"x′ = v，v′ = −x")
        for x,v in [(.7,.7),(.7,-.7),(-.7,-.7),(-.7,.7)]:
            p.arrow((x-.13*v,v+.13*x),(x+.13*v,v-.13*x))
        p.label(.78,1.04,u'右下 ↘')
        p.label(.78,-1.06,u'左下 ↙')
        p.label(-.78,-1.06,u'左上 ↖')
        p.label(-.78,1.04,u'右上 ↗')
    else:
        heading(f,center,u'蓝色圆才是这一条运动轨迹',u'轨迹顺时针走，并穿过两条零增长曲线')
        circle(p,1)
        for t in [.25,1.8,3.4,5.0]:
            p.arrow((math.cos(t),-math.sin(t)),(math.cos(t+.15),-math.sin(t+.15)),BLUE)
        for pt in [(1,0),(0,1),(-1,0),(0,-1)]: p.dot(pt,BLUE)
f.text(290,436,u'橙色横轴：x′ = 0，箭头竖直（原点除外）',16,ORANGE)
f.text(820,436,u'绿色纵轴：v′ = 0，箭头水平（原点除外）',16,GREEN)
f.text(540,468,u'两条线的交点才是平衡点；零增长曲线不是阻挡轨迹的墙。',16)
f.save('ode-nullclines-explained.svg')

# 2. Time is eliminated, pairing values measured at the same t.
f=Figure(u'消去时间：把同一时刻的两个数，合成相图上的一个点')
heading(f,285,u'左：分别看 x 和 y 随时间变化',u"x′ = 1，y′ = 2；从 (0, 0) 出发")
p=Plot(f,85,140,365,250,(0,2.3),(0,4.6),'t',u'数值')
p.curve([(0,0),(2,2)],BLUE)
p.curve([(0,0),(2,4)],ORANGE)
for t in [1,2]:
    p.curve([(t,0),(t,2*t)],'#cbd5e1',1,True)
    p.dot((t,t),BLUE);p.dot((t,2*t),ORANGE)
    p.label(t,0,str(t),dy=22)
p.label(1.7,1.4,u'x = t',BLUE)
p.label(1.65,3.9,u'y = 2t',ORANGE)
heading(f,810,u'右：只看 y 与 x 的关系',u'y = 2x；箭头由原方程决定')
p=Plot(f,640,140,320,250,(0,2.3),(0,4.6),'x','y')
p.curve([(0,0),(2.1,4.2)],GREEN)
p.arrow((.6,1.2),(.8,1.6),GREEN)
p.arrow((1.55,3.1),(1.75,3.5),GREEN)
for pt,label in [((0,0),u'(0, 0)'),((1,2),u'(1, 2)：t = 1'),((2,4),u'(2, 4)：t = 2')]:
    p.dot(pt,GREEN);p.label(pt[0],pt[1],label,GREEN,dx=-20 if pt[0]==2 else 35,dy=-15)
f.text(540,443,u'例如 t = 1：左图读出 x = 1、y = 2，右图就得到点 (1, 2)。',17)
f.text(540,471,u'时间被省去了，留下直线的形状；往哪边走、走多快，仍要看原方程。',16)
f.save('ode-eliminate-time-explained.svg')

# 3. Exact damped solution from (1,1), and its squared radius.
def damp(t):
    w=math.sqrt(3)/2
    x=math.exp(-t/2)*(math.cos(w*t)+math.sqrt(3)*math.sin(w*t))
    v=math.exp(-t/2)*(math.cos(w*t)-math.sqrt(3)*math.sin(w*t))
    return x,v
f=Figure(u'沿轨迹求导：距离的平方不增加，就不会跑出圆外')
heading(f,290,u'左：从 (1, 1) 出发的有阻力轨迹',u"x′ = v，v′ = −x − v")
p=Plot(f,125,128,290,290,(-2.3,2.3),(-2.3,2.3))
circle(p,2,GRAY,True);circle(p,math.sqrt(2),'#cbd5e1',True)
p.curve(samples(damp,12,600),BLUE)
for t in [.5,2,4,6]:p.arrow(damp(t),damp(t+.14),BLUE)
p.dot((1,1),ORANGE);p.label(1,1,u'起点 (1, 1)',ORANGE,dx=52,dy=-10)
p.label(0,-2.1,u'外圈：G = 4',GRAY,dy=15)
heading(f,805,u'右：同一运动的 G 随时间变化',u'G = x² + v²，G′ = −2v² ≤ 0')
p=Plot(f,635,140,340,250,(0,10.5),(0,4.6),'t','G')
p.curve([(0,4),(10,4)],GRAY,1.5,True)
p.label(5,4,u'边界 G = 4',GRAY,dy=-12)
p.curve(samples(lambda t:(t,sum(z*z for z in damp(t))),10,400),BLUE)
p.dot((0,2),ORANGE);p.label(1.4,2,u'起点 G = 2',ORANGE,dy=-12)
for t in [0,5,10]:p.label(t,0,str(t),dy=22)
f.text(540,454,u'蓝色曲线只能下降或暂时变平，不可能从 2 升到 4。',17)
f.text(540,476,u'所以左图的轨迹不会向外穿过虚线圆。',16)
f.save('ode-boundary-explained.svg')

# 4. Stable node versus saddle: exact trajectories.
f=Figure(u'平衡点附近：有的状态会回来，有的方向会越走越远')
for mode,left,center in [('node',110,290),('saddle',650,830)]:
    p=Plot(f,left,130,285,285,(-1.6,1.6),(-1.6,1.6),'x','y')
    if mode=='node':
        heading(f,center,u'两边都往回走：吸引附近状态',u"x′ = −x，y′ = −2y")
        for x,y in [(1.3,1.3),(-1.3,1.3),(1.3,-1.3),(-1.3,-1.3),(.5,1.4),(-.5,-1.4)]:
            fn=lambda t:(x*math.exp(-t),y*math.exp(-2*t))
            p.curve(samples(fn,4),BLUE)
            p.arrow(fn(.35),fn(.55),BLUE)
        f.text(center,449,u'靠近原点后，变化逐渐放慢。',16)
    else:
        heading(f,center,u'纵轴靠近、横向远离：鞍点',u"x′ = x，y′ = −y")
        for sx,sy in [(1,1),(-1,1),(1,-1),(-1,-1)]:
            fn=lambda t:(sx*.15*math.exp(t),sy*1.3*math.exp(-t))
            p.curve(samples(fn,math.log(1.4/.15)),ORANGE)
            p.arrow(fn(1.25),fn(1.45),ORANGE)
        for s in [-1,1]:
            p.arrow((0,s*1.3),(0,s*.55),GREEN)
            p.arrow((s*.3,0),(s*1.3,0),ORANGE)
        f.text(center,449,u'只有纵轴上的起点会趋向原点。',16)
    p.dot((0,0),GRAY)
f.text(540,477,u'灰点都是平衡点，但附近轨迹的走向不同。箭头表示时间增加的方向。',16)
f.save('ode-equilibria-explained.svg')

# 5. Plot the actual derivative and its approximation; cubic counterexample.
f=Figure(u'线性近似：靠近时看得准，离远后可能判断错方向',520)
heading(f,280,u'左：原方程与近似方程的变化率',u'横轴是 x，纵轴是 x′；这张是函数图，不是相图')
p=Plot(f,90,145,365,275,(-.55,1.55),(-1.65,1.05),'x',u'x′')
p.curve(samples(lambda x:(x,-x+x*x),1.5,start=-.5),BLUE)
p.curve([(-.5,.5),(1.5,-1.5)],ORANGE,2,True)
p.dot((0,0),GRAY);p.dot((1,0),BLUE)
p.label(1,0,'1',dy=22)
p.label(.6,.6,u'蓝：−x + x²',BLUE)
p.label(.8,-1.35,u'橙：−x',ORANGE)
heading(f,815,u'右：一次项为零，仍可能有相反趋势',u'两个例子的线性近似都是 y′ ≈ 0')
for y,label,toward,col in [(210,u'y′ = −y³：靠近零',True,GREEN),(350,u'y′ = y³：远离零',False,ORANGE)]:
    f.text(805,y-38,label,18,col)
    f.line([(630,y),(1000,y)],'#cbd5e1',2)
    f.dot(815,y,GRAY)
    f.text(815,y+29,'0')
    f.text(1020,y+5,'y')
    for a,b in [((660,y),(775,y)),((970,y),(855,y))]:
        f.arrow(a if toward else b,b if toward else a,col)
f.text(280,460,u'x 接近 0：两条线接近，方向一致。',16)
f.text(280,488,u'x > 1：一个为正、一个为负，方向相反。',16)
f.text(815,460,u'不能只因一次项为零，就认定不动。',16)
f.text(815,488,u'此时要回到原方程，看三次项的正负号。',16)
f.save('ode-linearization-explained.svg')
