import turtle, time
t = turtle.Pen()
t.reset()
for i in range(1, 19):
	t.forward(100)
	time.sleep(1)
	if i % 2 == 0:
		t.left(175)
	else:
		t.left(225)
time.sleep(2)