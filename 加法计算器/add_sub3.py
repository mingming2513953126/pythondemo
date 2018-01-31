#!/usr/bin/env python  

# -*- coding: utf-8 -*-  
from tkinter import *
import random


def main():
	a = random.randint(1, 18)
	if a < 10:
		b = random.randint(10 - a, 9)
		c = a + b
		result = "%d  +  %d" % (a, b)
		return (result, c)
	if a >= 10:
		b = random.randint(a - 9, 9)
		c = a - b
		result = "%d  -  %d" % (a, b)
		return (result, c)


def check():
	if int(result.get()) == int(t[1]):
		h = "恭喜你！回答正确"
		hint.set(h)

	else:
		h = "抱歉！回答错误！"
		hint.set(h)
		result.set('')


def next():
	global t
	t = main()
	e.set(t[0])
	result.set('')
	hint.set('')


master = Tk()
master.geometry('500x500+100+100')
master.title("20以内加减进退位运算")
Label(master, text="题目").grid(row=0)
Label(master, text="答案").grid(row=1)
Label(master, text="信息").grid(row=4)
e = StringVar()
result = StringVar()
hint = StringVar()
e1 = Entry(master, textvariable=e)
e2 = Entry(master, textvariable=result)
e3 = Entry(master, textvariable=hint)
t = main()
e.set(t[0])
result.get()

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=4, column=1)

btn = Button(master, text='确定', command=check)
btn2 = Button(master, text='下一题', command=next)
btn.grid(row=2, column=2)
btn2.grid(row=2, column=4)

master.mainloop()  