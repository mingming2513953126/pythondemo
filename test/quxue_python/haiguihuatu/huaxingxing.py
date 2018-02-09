import turtle, time
t = turtle.Pen()
def mystar(size, filled):
	if filled == True:
		t.begin_fill()
	for i in range(1, 19):
		t.forward(size)
		if i % 2 == 0:
			t.left(175)
		else:
			t.left(225)
	if filled == True:
		t.end_fill()

if __name__ == '__main__':
	t.color(0.9, 0.75, 0)
	mystar(120, True)