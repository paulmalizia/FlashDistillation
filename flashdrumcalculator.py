import graphics
from graphics import *

def main():
	win = GraphWin("Flash Drum Calculator", 500, 375)
	win.setCoords(0, 0, 10, 10)

	#Flash Drum & I/O - Vertical Lines
	Line(Point(4,4), Point(4,8)).draw(win)
	Line(Point(6,4), Point(6,8)).draw(win)
	Line(Point(5,8), Point(5,9)).draw(win)
	Line(Point(5,4), Point(5,3)).draw(win)
	
	#Flash Drum & I/O - Horizontal Lines
	Line(Point(5,9), Point(8,9)).draw(win)
	Line(Point(5,3), Point(8,3)).draw(win)
	Line(Point(4,4), Point(6,4)).draw(win)
	Line(Point(4,8), Point(6,8)).draw(win)
	Line(Point(1,6), Point(4,6)).draw(win)

	#Flash Drum - Interface
	Text(Point(1.6,6.5), "F:").draw(win)
	Text(Point(1,5.5), "Chemical 1:").draw(win)
	Text(Point(1.6,4.8), "K\u2081:").draw(win)
	Text(Point(1,4.1), "Chemical 2:").draw(win)
	Text(Point(1.6,3.4), "K\u2082:").draw(win)
	Text(Point(1,2.7), "Chemical 3:").draw(win)
	Text(Point(1.6,2.0), "K\u2083:").draw(win)
	Text(Point(1,1.3), "Chemical 4:").draw(win)
	Text(Point(1.6,0.6), "K\u2084:").draw(win)
	Text(Point(7.5,9.5), "V:").draw(win)
	Text(Point(7.5,8.5), "y\u2081:").draw(win)
	Text(Point(7.5,8), "y\u2082:").draw(win)
	Text(Point(7.5,7.5), "y\u2083:").draw(win)
	Text(Point(7.5,7), "y\u2084:").draw(win)
	Text(Point(7.5,3.5), "L:").draw(win)
	Text(Point(7.5,2.5), "x\u2081:").draw(win)
	Text(Point(7.5,2), "x\u2082:").draw(win)
	Text(Point(7.5,1.5), "x\u2083:").draw(win)
	Text(Point(7.5,1), "x\u2084:").draw(win)
	
	#Flash Drum Units - Interface
	Text(Point(3.4,6.5), "kmol/h").draw(win)
	Text(Point(3.4,5.5), "mol%").draw(win)
	Text(Point(3.4,4.1), "mol%").draw(win)
	Text(Point(3.4,2.7), "mol%").draw(win)
	Text(Point(3.4,1.3), "mol%").draw(win)
	Text(Point(9.5,9.5), "kmol/h").draw(win)
	Text(Point(9.5,8.5), "%").draw(win)
	Text(Point(9.5,8), "%").draw(win)
	Text(Point(9.5,7.5), "%").draw(win)
	Text(Point(9.5,7), "%").draw(win)

	Text(Point(9.5,3.5), "kmol/h").draw(win)
	Text(Point(9.5,2.5), "%").draw(win)
	Text(Point(9.5,2), "%").draw(win)
	Text(Point(9.5,1.5), "%").draw(win)
	Text(Point(9.5,1), "%").draw(win)

	#Inputs
	feedText = Entry(Point(2.4, 6.5), 5)
	feedText.setText("00.0")
	feedText.draw(win)

	species1_in = Entry(Point(2.4, 5.5), 5)
	species1_in.setText("00.0")
	species1_in.draw(win)

	k1_in = Entry(Point(2.4, 4.8), 5)
	k1_in.setText("00.0")
	k1_in.draw(win)

	species2_in = Entry(Point(2.4, 4.1), 5)
	species2_in.setText("00.0")
	species2_in.draw(win)

	k2_in = Entry(Point(2.4, 3.4), 5)
	k2_in.setText("00.0")
	k2_in.draw(win)

	species3_in = Entry(Point(2.4, 2.7), 5)
	species3_in.setText("00.0")
	species3_in.draw(win)

	k3_in = Entry(Point(2.4, 2), 5)
	k3_in.setText("00.0")
	k3_in.draw(win)

	k4_in = Entry(Point(2.4, 0.6), 5)
	k4_in.setText("00.0")
	k4_in.draw(win)

	#Outputs - Vapor
	voText = Text(Point(8.6, 9.5),"")
	voText.draw(win)

	y1Text = Text(Point(8.6, 8.5),"")
	y1Text.draw(win)

	y2Text = Text(Point(8.6, 8),"")
	y2Text.draw(win)

	y3Text = Text(Point(8.6, 7.5),"")
	y3Text.draw(win)

	y4Text = Text(Point(8.6, 7),"")
	y4Text.draw(win)

	#Outputs - Liquid
	loText = Text(Point(8.6, 3.5),"")
	loText.draw(win)

	x1Text = Text(Point(8.6, 2.5),"")
	x1Text.draw(win)

	x2Text = Text(Point(8.6, 2),"")
	x2Text.draw(win)

	x3Text = Text(Point(8.6, 1.5),"")
	x3Text.draw(win)

	x4Text = Text(Point(8.6, 1),"")
	x4Text.draw(win)

	#Autocomplete
	species4_in = Text(Point(2.4, 1.3), "")
	species4_in.draw(win)

	#Convert input
	i = 1
	while i == 1:
		x = win.getMouse()
		f = float(feedText.getText())
		z1 = float(species1_in.getText())
		z2 = float(species2_in.getText())
		z3 = float(species3_in.getText())
		z4 = 100 - z3 - z2 - z1
		species4_in.setText(z4)
		k1 = float(k1_in.getText())
		k2 = float(k2_in.getText())
		k3 = float(k3_in.getText())
		k4 = float(k4_in.getText())

		def n_raphson(fn, dfn, phi, tol, maxiter):
			for i in range(maxiter):
				phinew = phi - fn(phi)/dfn(phi)
				if abs(phinew - phi) < tol: break
				phi = phinew
			return phi

		y = lambda phi: (z1*(1-k1))/(1+phi*(k1-1)) + (z2*(1-k2))/(1+phi*(k2-1)) + (z3*(1-k3))/(1+phi*(k3-1)) + (z4*(1-k4))/(1+phi*(k4-1))
		dy = lambda phi: (z1*(1-k1)**2)/((1+phi*(k1-1))**2) + (z2*(1-k2)**2)/((1+phi*(k2-1))**2) + (z3*(1-k3)**2)/((1+phi*(k3-1))**2) + (z4*(1-k4)**2)/((1+phi*(k4-1))**2)

		phi = n_raphson(y, dy, 0.5, 0.0001, 100)

		y1 = k1*z1/(1+phi*(k1-1))
		y2 = k2*z2/(1+phi*(k2-1))
		y3 = k3*z3/(1+phi*(k3-1))
		y4 = k4*z4/(1+phi*(k4-1))

		x1 = z1/(1+phi*(k1-1))
		x2 = z2/(1+phi*(k2-1))
		x3 = z3/(1+phi*(k3-1))
		x4 = z4/(1+phi*(k4-1))

		v = phi * f
		l = f - v
		
		y1Text.setText(round(y1, 2))
		y2Text.setText(round(y2, 2))
		y3Text.setText(round(y3, 2))
		y4Text.setText(round(y4, 2))

		x1Text.setText(round(x1, 2))
		x2Text.setText(round(x2, 2))
		x3Text.setText(round(x3, 2))
		x4Text.setText(round(x4, 2))

		voText.setText(round(v, 2))
		loText.setText(round(l, 2))

main()

