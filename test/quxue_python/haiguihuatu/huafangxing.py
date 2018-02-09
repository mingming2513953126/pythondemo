import turtle, time
t = turtle.Pen()
def mysquare(size):
	for i in range(1, 5):
		# t.color(1, 0, 0)
		t.forward(size)
		t.left(90)


if __name__ == '__main__':
	mysquare(50)
	mysquare(75)
	mysquare(100)

	time.sleep(2)