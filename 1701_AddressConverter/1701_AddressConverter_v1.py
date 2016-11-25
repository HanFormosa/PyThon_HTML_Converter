from tkinter import *

root=Tk()

sizex = 600
sizey = 400
posx  = 0
posy  = 0
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

labels = []
entries_Variable = []
entries_Alias = []
entries_Address = []



def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=300, height=300)


def myClick():
    del labels[:] # remove any previous labels from if the callback was called before
    for i in range(80):
        labels.append(Label(frame, text=str(i+1)))
        labels[i].grid(row= i, column=0)

        entries_Variable.append(Entry(frame))
        entries_Variable[i].grid(row= i, column =1)

        entries_Alias.append(Entry(frame))
        entries_Alias[i].grid(row=i, column=2)

        entries_Address.append(Entry(frame))
        entries_Address[i].grid(row=i, column=3)

def myClick2():
    if len(entries_Variable) > 0:
        entries_Variable[0].insert(0, variables[0])
        entries_Variable[1].insert(0, variables[1])
    #if len(labels) > 1:

def readVariableList():
    with open("DSP_VARIABLES.txt", 'r+') as f:
        line = f.readlines()
        for i in range(len(line)):
            entries_Variable[i].delete(0,END)
            entries_Variable[i].insert(0, line[i].strip("\n"))
myframe = Frame(root, width=400, height=300, bd=2, relief=GROOVE)
myframe.place(x=10, y=10)

canvas = Canvas(myframe)
frame = Frame(canvas)
myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right", fill="y")
canvas.pack(side="left")
canvas.create_window((0, 0), window=frame, anchor='nw')
frame.bind("<Configure>", myfunction)


mybutton=Button(root,text="OK",command=myClick)
mybutton.place(x=420,y=10)

mybutton2=Button(root,text="Change",command=readVariableList)
mybutton2.place(x=420,y=80)

myvalue=Entry(root)
myvalue.place(x=450,y=10)

text_log = Text(root, height=20, width=60)
text_log.place(x=420,y=120)
root.mainloop()
