import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
time.sleep(1)
canvas.pack()
time.sleep(1)
canvas.create_rectangle(10, 10, 50, 300)
tk.mainloop()             #进入消息循环（必需组件）
