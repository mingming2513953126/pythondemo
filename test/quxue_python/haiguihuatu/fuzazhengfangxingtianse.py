import turtle, time
t = turtle.Pen()
def mysquare1(size, filled):
	if filled == True:
		t.begin_fill()
	for i in range(1, 5):
		t.forward(size)
		t.left(90)
	if filled == True:
		t.end_fill()
time.sleep(2)



if __name__ == '__main__':
	# mysquare1(50, True)
	mysquare1(150, False)