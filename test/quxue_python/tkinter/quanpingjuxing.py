import time
from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
# time.sleep(1)
canvas.pack()
# time.sleep(1)
def random_rectangle(width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = x1 + random.randrange(width)
	y2 = y1 + random.randrange(height)
	canvas.create_rectangle(x1, y1, x2, y2)
	tk.mainloop()                                           # 进入消息循环（必需组件）




if __name__ == '__main__':
	for i in range(0, 100):
		random_rectangle(400, 400)
