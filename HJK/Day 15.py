from tkinter import *

window = Tk()

def feedback():
    button["text"] = "시작 하겠습니다"
    
def feedback2():
    button2["text"] = "나가 겠습니다"

label = Label(text = "Hello", font = 35)
label.pack()
button = Button(text = "start", height = 5, width = 10, command = feedback)
button.pack(side = LEFT)
button2 = Button(text = "Get out", height = 5, width = 10, command= feedback2)
button2.pack()








window.mainloop()
