from tkinter import *

root=Tk()

sizex = 1000
sizey = 500
posx  = 0
posy  = 0
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

labels = []
entries_Variable = []
entries_Alias = []
entries_Address = []



def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=550, height=300)


def myClick():
    del labels[:] # remove any previous labels from if the callback was called before
    for i in range(70):
        labels.append(Label(frame, text=str(i+1)))
        labels[i].grid(row= i, column=0)

        entries_Variable.append(Entry(frame))
        entries_Variable[i].grid(row= i, column =1)

        entries_Alias.append(Entry(frame))
        entries_Alias[i].grid(row=i, column=2)

        entries_Address.append(Entry(frame))
        entries_Address[i].grid(row=i, column=3)

def readVariableList():
    with open("DSP_VARIABLES.txt", 'r+') as f:
        line = f.readlines()
        for i in range(len(line)):
            entries_Variable[i].delete(0,END)
            entries_Variable[i].insert(0, line[i].strip("\n"))

    with open("DSP_ALIAS.txt", 'r+') as f2:
        line = f2.readlines()
        for i in range(len(line)):
            entries_Alias[i].delete(0,END)
            entries_Alias[i].insert(0, line[i].strip("\n"))

def extract():
    with open("DSP_ALIAS.txt") as f:
        for i, l in enumerate(f):
            pass
    totalline = i + 1
    for i in range(0, totalline):
        with open("MT-3000E.params", 'r+') as f3:
            for line in f3:
                if entries_Alias[i].get() in line:
                    tmp_line = line[20:-1]  # check for whole word
                    if entries_Alias[i].get() != tmp_line:
                        print("no matching whole word detected. Found :" + tmp_line)
                    else:
                        line = f3.readline() # read next line
                        print(line.strip("\n"))
                        address = line[20:-1] # extract
                        hex_address = hex(int(address))
                        print(hex_address)
                        entries_Address[i].delete(0, END)
                        entries_Address[i].insert(0, hex_address)
                        break

def convert():
    text_log.delete(1.0, END)  # clear text
    with open("DSP_ALIAS.txt") as f:
        for i, l in enumerate(f):
            pass
    totalline = i + 1
    for i in range(totalline):
        myStr = "#define\t" + entries_Variable[i].get() + "\t" + entries_Address[i].get() + "\n"
        text_log.insert(END, myStr)
myframe = Frame(root, width=400, height=500, bd=2, relief=GROOVE)
myframe.grid(row=0, column=0)

canvas = Canvas(myframe)
frame = Frame(canvas)
myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right", fill="y")
canvas.pack(side="left")
canvas.create_window((0, 0), window=frame, anchor='nw')
frame.bind("<Configure>", myfunction)


#mybutton=Button(root,text="OK",command=myClick)
#mybutton.grid(row=1, column=0)

myClick()

mybutton2=Button(root,text="Read",command=readVariableList)
mybutton2.grid(row=2, column=0)

buttonExtract=Button(root,text="Extract",command=extract)
buttonExtract.grid(row=3, column=0)

buttonConvert=Button(root, text="Convert",command=convert)
buttonConvert.grid(row=4, column=0)

text_log = Text(root, height=20, width=50)
text_log.grid(row=0, column=1)
root.mainloop()
