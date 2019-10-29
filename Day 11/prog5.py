from Tkinter import *
root = Tk()
def left(event):
    print('Left')
def right(event):
    print('Right')
def middle(event):
    print('Middle')
frame = Frame(root, width = 300, height = 250)
frame.bind("<Button-1>", left)
frame.bind("<Button-2>", middle)
frame.bind("<Button-3>", right)
frame.pack()
root.mainloop()
