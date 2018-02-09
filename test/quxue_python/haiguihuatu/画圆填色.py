import turtle, time
t = turtle.Pen()
def mysircle(red, green, blue):
	t.color(red, green, blue)
	t.begin_fill()
	t.circle(50)
	t.end_fill()

"""
if __name__ == '__main__':
	mysircle(0, 1, 0)
	time.sleep(2)
"""