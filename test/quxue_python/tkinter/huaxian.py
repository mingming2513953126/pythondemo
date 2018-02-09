import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
# time.sleep(2)
canvas.pack()
# time.sleep(2)
canvas.create_line(0,0,500,500)
tk.mainloop()             #进入消息循环（必需组件）

