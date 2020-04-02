import turtle

class pen:
	def __init__(self,x,y,color='Black',size=0.05,shapesize=0.1):
		self.t = turtle.Turtle()
		self.x = x
		self.y = y
		self.color = color
		self.t.color(color)
		self.t.shapesize(shapesize)
		self.t.pensize(size)
		self.t.penup()
		self.t.goto(x,y)
		self.t.pendown()

	def stright(self,start,end,color=None):

		if color == None :
			color = self.color

		self.t.penup()
		self.t.goto(start[0],start[1])
		self.t.color(color)
		self.t.pendown()
		self.t.goto(end[0],end[1])
		self.t.color(self.color)

	def circle(self,start,r,orientation,theta,color=None):

		if color == None :
			color = self.color

		self.t.penup()
		self.t.goto(start[0],start[1])
		self.t.setheading(orientation)
		self.t.color(color)
		self.t.pendown()
		self.t.circle(r,theta)
		self.t.color(self.color)


class script:

	def __init__(self,pen):
		self.pen = pen

	def draw(self,str,s,h=100,w=30,gap=2,t=[1,0]):

		for i in range(len(str)):
			ss = [s[0] + t[0]*i*(gap+w),s[1]+ t[1]*i*(gap+h)]
			self.call(str[i],h,w,ss)


	def A(self,h,w,s,color=None):

		e = [s[0]+(w/2),s[1]+h]
		self.pen.stright(s,e,color=color)

		e1 = [s[0]+w,s[1]]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+(w/4),s[1]+(h/2)]
		e1 = [s[0]+(3*w/4),s[1]+(h/2)]
		self.pen.stright(e,e1,color=color)

		return

	def B(self,h,w,s,color=None):

		e1 =  [s[0],s[1]+h]
		self.pen.stright(s,e1,color=color)

		e = [s[0]+(3*w/4),s[1]+h]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+w,s[1]+(3*h/4)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+(3*w/4),s[1]+(h/2)]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0],s[1]+(h/2)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+(3*w/4),s[1]+(h/2)]
		e1 = [s[0]+w,s[1]+(h/4)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+(3*w/4),s[1]]
		self.pen.stright(e1,e,color=color)

		self.pen.stright(e,s,color=color)

		return

	def C(self,h,w,s,color=None):

		e1 = [s[0]+w,s[1]+(h)]
		e = [s[0]+w,s[1]+(3*h/4)]
		self.pen.stright(e,e1,color=color)

		e = [s[0],s[1]+h]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0],s[1]]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+w,s[1]+(h/4)]
		self.pen.stright(e,e1,color=color)


		return

	def D(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		self.pen.stright(s,e,color=color)

		e1 = [s[0],s[1]+h]
		e = [s[0]+(3*w/4),s[1]+h]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+w,s[1]+(3*h/4)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]+(h/4)]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+(3*w/4),s[1]]
		self.pen.stright(e,e1,color=color)

		self.pen.stright(e1,s,color=color)

		return

	def E(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		self.pen.stright(s,e,color=color)

		e1 = [s[0]+w,s[1]+h]
		self.pen.stright(e,e1,color=color)

		e = [s[0],s[1]+(h/2)]
		e1 = [s[0]+w,s[1]+(h/2)]
		self.pen.stright(e,e1,color=color)

		e1 = [s[0]+w,s[1]]
		self.pen.stright(s,e1,color=color)

		return

	def F(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		self.pen.stright(s,e,color=color)

		e1 = [s[0]+w,s[1]+h]
		self.pen.stright(e,e1,color=color)

		e = [s[0],s[1]+(h/2)]
		e1 = [s[0]+w,s[1]+(h/2)]
		self.pen.stright(e,e1,color=color)

		return

	def G(self,h,w,s,color=None):

		e1 = [s[0]+w,s[1]+(h)]
		e = [s[0]+w,s[1]+(3*h/4)]
		self.pen.stright(e,e1,color=color)

		e = [s[0],s[1]+h]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0],s[1]]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+w,s[1]+(h/2)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+(w/2),s[1]+(h/2)]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+(w/2),s[1]+(h/4)]
		self.pen.stright(e,e1,color=color)

		return

	def H(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		self.pen.stright(s,e,color=color)

		e = [s[0],s[1]+(h/2)]
		e1 = [s[0]+w,s[1]+(h/2)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]+h]
		e1 = [s[0]+w,s[1]]
		self.pen.stright(e,e1,color=color)

		return

	def I(self,h,w,s,color=None):

		e1 = [s[0]+(w/4),s[1]+h]
		e = [s[0]+(3*w/4),s[1]+h]
		self.pen.stright(e,e1,color=color)

		e1 = [s[0]+(w/2),s[1]+h]
		e = [s[0]+(w/2),s[1]]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+(w/4),s[1]]
		e = [s[0]+(3*w/4),s[1]]
		self.pen.stright(e,e1,color=color)

		return

	def J(self,h,w,s,color=None):

		e1 = [s[0],s[1]+h]
		e = [s[0]+w,s[1]+h]
		self.pen.stright(e,e1,color=color)

		e1 = [s[0]+(w/2),s[1]+h]
		e = [s[0]+(w/2),s[1]]
		self.pen.stright(e1,e,color=color)

		self.pen.stright(e,s,color=color)

		e1 = [s[0],s[1]+(h/4)]
		self.pen.stright(s,e1,color=color)

		return

	def K(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		self.pen.stright(s,e,color=color)

		e1 = [s[0]+w,s[1]+h]
		e = [s[0],s[1]+(h/2)]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+w,s[1]]
		self.pen.stright(e,e1,color=color)


		return

	def L(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		self.pen.stright(e,s,color=color)

		e1 = [s[0]+w,s[1]]
		self.pen.stright(s,e1,color=color)

		return

	def M(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		self.pen.stright(s,e,color=color)

		e1 = [s[0]+(w/2),s[1]+(h/2)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]+h]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+w,s[1]]
		self.pen.stright(e,e1,color=color)

		return

	def N(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		self.pen.stright(s,e,color=color)

		e1 = [s[0]+w,s[1]]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]]
		e1 = [s[0]+w,s[1]+h]
		self.pen.stright(e,e1,color=color)

		return

	def O(self,h,w,s,color=None):
		e = [s[0],s[1]+h]
		self.pen.stright(e,s,color=color)

		e = [s[0]+w,s[1]]
		self.pen.stright(s,e,color=color)

		e1 = [s[0]+w,s[1]+h]
		self.pen.stright(e,e1,color=color)

		e = [s[0],s[1]+h]
		self.pen.stright(e1,e,color=color)

		return

	def P(self,h,w,s,color=None):

		e1 =  [s[0],s[1]+h]
		self.pen.stright(s,e1,color=color)

		e = [s[0]+(3*w/4),s[1]+h]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+w,s[1]+(3*h/4)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+(3*w/4),s[1]+(h/2)]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0],s[1]+(h/2)]
		self.pen.stright(e,e1,color=color)

		return

	def Q(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		self.pen.stright(e,s,color=color)

		e = [s[0]+w,s[1]]
		self.pen.stright(s,e,color=color)

		e1 = [s[0]+w,s[1]+h]
		self.pen.stright(e,e1,color=color)

		e = [s[0],s[1]+h]
		self.pen.stright(e1,e,color=color)

		e = [s[0]+(7*w/8),s[1]+(h/8)]
		e1 = [s[0]+(9*w/8),s[1]-(h/8)]
		self.pen.stright(e,e1,color=color)

		return

	def R(self,h,w,s,color=None):

		e1 =  [s[0],s[1]+h]
		self.pen.stright(s,e1,color=color)

		e = [s[0]+(3*w/4),s[1]+h]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+w,s[1]+(3*h/4)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+(3*w/4),s[1]+(h/2)]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0],s[1]+(h/2)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]]
		self.pen.stright(e1,e,color=color)


		return

	def S(self,h,w,s,color=None):
		e1 = [s[0]+w,s[1]+(h)]
		e = [s[0]+w,s[1]+(3*h/4)]
		self.pen.stright(e,e1,color=color)

		e = [s[0],s[1]+h]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0],s[1]+(h/2)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]+(h/2)]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+w,s[1]]
		self.pen.stright(e,e1,color=color)

		self.pen.stright(e1,s,color=color)

		e1 = [s[0],s[1]+(h/4)]
		self.pen.stright(s,e1,color=color)

		return

	def T(self,h,w,s,color=None):

		e1 = [s[0],s[1]+h]
		e = [s[0]+w,s[1]+h]
		self.pen.stright(e,e1,color=color)

		e1 = [s[0]+(w/2),s[1]+h]
		e = [s[0]+(w/2),s[1]]
		self.pen.stright(e1,e,color=color)

		return

	def U(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		e1 = [s[0],s[1]+(h/4)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+(w/4),s[1]]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+(3*w/4),s[1]]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]+(h/4)]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+w,s[1]+h]
		self.pen.stright(e,e1,color=color)

		return

	def V(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		e1 = [s[0]+(w/2),s[1]]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]+h]
		self.pen.stright(e1,e,color=color)

		return

	def W(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		e1 = [s[0]+(w/4),s[1]]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+(w/2),s[1]+(h/2)]
		self.pen.stright(e1,e,color=color)

		e1 = [s[0]+(3*w/4),s[1]]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]+h]
		self.pen.stright(e1,e,color=color)

		return

	def X(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		e1 = [s[0]+w,s[1]]
		self.pen.stright(e,e1,color=color)

		e1 = [s[0]+w,s[1]+h]
		self.pen.stright(e1,s,color=color)

		return

	def Y(self,h,w,s,color=None):

		e = [s[0],s[1]+h]
		e1 = [s[0]+(w/2),s[1]+(h/2)]
		self.pen.stright(e,e1,color=color)

		e = [s[0]+w,s[1]+h]
		self.pen.stright(e1,e,color=color)

		e = [s[0]+(w/2),s[1]+(h/2)]
		e1 = [s[0]+(w/2),s[1]]
		self.pen.stright(e,e1,color=color)

		return

	def Z(self,h,w,s,color=None):

		e = [s[0]+w,s[1]+h]
		self.pen.stright(s,e,color=color)

		e1 = [s[0],s[1]+h]
		self.pen.stright(e,e1,color=color)

		e1 = [s[0]+w,s[1]]
		self.pen.stright(s,e1,color=color)

	def space(self,h,w,s,color=None):

		return

	def call(self,C,h,w,s,color=None):

		if C == 'A':
			self.A(h=h,w=w,s=s,color=color)
			return
		if C == 'B':
			self.B(h=h,w=w,s=s,color=color)
			return
		if C == 'C':
			self.C(h=h,w=w,s=s,color=color)
			return
		if C == 'D':
			self.D(h=h,w=w,s=s,color=color)
			return
		if C == 'E':
			self.E(h=h,w=w,s=s,color=color)
			return
		if C == 'F':
			self.F(h=h,w=w,s=s,color=color)
			return
		if C == 'G':
			self.G(h=h,w=w,s=s,color=color)
			return
		if C == 'H':
			self.H(h=h,w=w,s=s,color=color)
			return
		if C == 'I':
			self.I(h=h,w=w,s=s,color=color)
			return
		if C == 'J':
			self.J(h=h,w=w,s=s,color=color)
			return
		if C == 'K':
			self.K(h=h,w=w,s=s,color=color)
			return
		if C == 'L':
			self.L(h=h,w=w,s=s,color=color)
			return
		if C == 'M':
			self.M(h=h,w=w,s=s,color=color)
			return
		if C == 'N':
			self.N(h=h,w=w,s=s,color=color)
			return
		if C == 'O':
			self.O(h=h,w=w,s=s,color=color)
			return
		if C == 'P':
			self.P(h=h,w=w,s=s,color=color)
			return
		if C == 'Q':
			self.Q(h=h,w=w,s=s,color=color)
			return
		if C == 'R':
			self.R(h=h,w=w,s=s,color=color)
			return
		if C == 'S':
			self.S(h=h,w=w,s=s,color=color)
			return
		if C == 'T':
			self.T(h=h,w=w,s=s,color=color)
			return
		if C == 'U':
			self.U(h=h,w=w,s=s,color=color)
			return
		if C == 'V':
			self.V(h=h,w=w,s=s,color=color)
			return
		if C == 'W':
			self.W(h=h,w=w,s=s,color=color)
			return
		if C == 'X':
			self.X(h=h,w=w,s=s,color=color)
			return
		if C == 'Y':
			self.Y(h=h,w=w,s=s,color=color)
			return
		if C == 'Z':
			self.Z(h=h,w=w,s=s,color=color)
			return
		if C == ' ':
			self.space(h=h,w=w,s=s,color=color)
			return





wn = turtle.Screen()


p = pen(0,0)
S = script(p)
S.draw(str='THIS IS JUST FOR EXAMPLE',s=[-200,300],gap=4,h=30,w=12,t=[1,0])
S.draw(str='THIS IS ALSO POSSIBLE',s=[-500,10],gap=4,h=30,w=12,t=[1,0.2])
S.draw(str='EVEN THIS IS POSSIBLE',s=[250,80],gap=4,h=30,w=12,t=[-1,-0.2])
S.draw(str='FOR EVEN THIS IS POSSIBLE',s=[-50,-80],gap=3,h=25,w=10,t=[1,-0.2])




wn.exitonclick()