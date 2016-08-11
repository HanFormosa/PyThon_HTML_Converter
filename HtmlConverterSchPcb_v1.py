from tkinter import *
from tkinter import filedialog
#from Tkinter import * #try this if in terminal don't work

root = Tk()

# ****** constants *******
kVERSION = 0
kBOOTLOADER = 1
kRELEASE = 2

kBOARD1 = "1.MAIN POWER"
kBOARD2 = "2.POWER AMP"
kBOARD3 = "3.BGM"
kBOARD4 = "4.ETHERNET"
kBOARD5 = "5.PRIORITY"
kBOARD6 = "6.FRONT PANEL"
kBOARD7 = "7.SPS BOARD"
kBOARD8 = "8.SPEAKER BOARD"
kBOARD9 = "9.POWER SW"

def selectBoard(x):
    entry_board.delete(0, END)  # clear text box widget
    if x == 1:
        entry_board.insert(0, kBOARD1)
    elif x == 2:
        entry_board.insert(0, kBOARD2)
    elif x == 3:
        entry_board.insert(0, kBOARD3)
    elif x == 4:
        entry_board.insert(0, kBOARD4)
    elif x == 5:
        entry_board.insert(0, kBOARD5)
    elif x == 6:
        entry_board.insert(0, kBOARD6)
    elif x == 7:
        entry_board.insert(0, kBOARD7)
    elif x == 8:
        entry_board.insert(0, kBOARD8)
    else:
        entry_board.insert(0, kBOARD9)

def doGenerate():
    text_Converted.delete(1.0, END) #clear text box widget
    str_modelName = entry_modelName.get()

    str_version = entry_version.get()
    str_version_sub1 = entry_version_sub1.get()

    str_Date = entry_Date.get()

    str_board = entry_board.get()

    str_rel = entry_rel.get()
    str_rel_sub1 = entry_rel_sub1.get()

    tr_line = "  <tr>\n"
    td_line1 = "\t<td><a href=\"" + str_modelName + "/" +  str_board + "/" + str_version + "/" +str_version_sub1 + "\" download>" + str_version + "</a></td>\n"
    td_line2 = "\t<td><a href=\"" + str_modelName + "/" + str_board + "/" + str_rel_sub1 + "\" target=_blank>" + str_rel + "</a></td>\n"
    td_line3 = "\t<td>" + str_Date + "</td>\n"
    tr_end_line = "  </tr>\n"

    final_str = tr_line + td_line1 + td_line3 + td_line2 + tr_end_line

    text_Converted.insert(END, final_str)

def browseVersion():
    file_path = filedialog.askopenfilename()
    entry_version_sub1.delete(0, END)
    # add some magic to display only file name, by detecting the last "/"
    numberOfStrokes = file_path.count('/') # find total number of strokes, used this in for loop later
    strokeCount = 0
    for x in range(0, len(file_path)):
        str_temp = file_path[x]
        # iterate through each characters, and count up once a stroke is found.
        if str_temp is '/':
            strokeCount += 1
            # when number of strokes count reaches the expected total stroke counts,this means this is the last stroke in the string.
            if strokeCount == numberOfStrokes:
                # extract the strings from the last stroke till end of file, to get the file name only
                fileName = file_path[x+1:]
                entry_version_sub1.insert(0, fileName)
                break
    #if fileType == kVERSION:
    #    entry_version_sub1.insert(0, fileName)  # display text in entry box
    #elif fileType == kBOOTLOADER:
    #    entry_BL_sub1.insert(0, fileName)
    #elif fileType == kRELEASE:
    #    entry_rel_sub1.insert(0,fileName)
    #else:
    #    print("E: did not specify which text box")

def browseRel():
    file_path = filedialog.askopenfilename()
    entry_rel_sub1.delete(0, END)
    # add some magic to display only file name, by detecting the last "/"
    numberOfStrokes = file_path.count('/')  # find total number of strokes, used this in for loop later
    strokeCount = 0
    for x in range(0, len(file_path)):
        str_temp = file_path[x]
        # iterate through each characters, and count up once a stroke is found.
        if str_temp is '/':
            strokeCount += 1
            # when number of strokes count reaches the expected total stroke counts,this means this is the last stroke in the string.
            if strokeCount == numberOfStrokes:
                # extract the strings from the last stroke till end of file, to get the file name only
                fileName = file_path[x + 1:]
                entry_rel_sub1.insert(0, fileName)
                break

# ******** label *********

label_modelName = Label(text="Model Name")
label_version = Label(text="Version")
label_Date = Label(text="Date")
label_rel = Label(text="Release Note")

label_fileName = Label(text="File Name")

label_board = Label(text="Board")

# ****** user input textbox *******

entry_modelName = Entry(root)
entry_modelName.insert(0, "MODEL")

entry_version = Entry(root)
entry_version.insert(0, "V1.0")
entry_version_sub1 = Entry(root)
entry_version_sub1.insert(0, "schematic.sch")

entry_Date = Entry(root)
entry_Date.insert(0, "2016-mm-dd")


entry_rel = Entry(root)
entry_rel.insert(0, "Release Note")
entry_rel_sub1 = Entry(root)
entry_rel_sub1.insert(0, "release.pdf")


entry_board = Entry(root)
entry_board.insert(0, "1.MAIN POWER")

# ****** Text Box *********
text_Converted = Text(root)

# *******Buttons ******* TODO: add command
button_BrowseVersion = Button(text="...", command=browseVersion)
button_BrowseRel = Button(text="...", command=browseRel)
button_Generate = Button(text="Generate", command=doGenerate)

# -- radio button  --
v = IntVar()

Radiobutton(root, text=kBOARD1, variable=v, value=1, command=lambda: selectBoard(1)).grid(row=1, column=1, sticky=W)
Radiobutton(root, text=kBOARD2, variable=v, value=2, command=lambda: selectBoard(2)).grid(row=1, column=2, sticky=W)
Radiobutton(root, text=kBOARD3, variable=v, value=3, command=lambda: selectBoard(3)).grid(row=1, column=3, sticky=W)

Radiobutton(root, text=kBOARD4, variable=v, value=4, command=lambda: selectBoard(4)).grid(row=2, column=1, sticky=W)
Radiobutton(root, text=kBOARD5, variable=v, value=5, command=lambda: selectBoard(5)).grid(row=2, column=2, sticky=W)
Radiobutton(root, text=kBOARD6, variable=v, value=6, command=lambda: selectBoard(6)).grid(row=2, column=3, sticky=W)

Radiobutton(root, text=kBOARD7, variable=v, value=7, command=lambda: selectBoard(7)).grid(row=3, column=1, sticky=W)
Radiobutton(root, text=kBOARD8, variable=v, value=8, command=lambda: selectBoard(8)).grid(row=3, column=2, sticky=W)
Radiobutton(root, text=kBOARD9, variable=v, value=9, command=lambda: selectBoard(9)).grid(row=3, column=3, sticky=W)

# ****** positioning in grid *********

label_modelName.grid(row=0, sticky=E)
entry_modelName.grid(row=0, column=1)

label_board.grid(row=1, sticky=E)

entry_board.grid(row=4,column=1)

label_fileName.grid(row=4, column=2)

label_version.grid(row=5, sticky=E)
entry_version.grid(row=5, column=1)
entry_version_sub1.grid(row=5, column=2)
button_BrowseVersion.grid(row=5, column=3)

label_Date.grid(row=6, sticky=E)
entry_Date.grid(row=6, column=1)


label_rel.grid(row=7, sticky=E)
entry_rel.grid(row=7, column=1)
entry_rel_sub1.grid(row=7, column=2)
button_BrowseRel.grid(row=7, column=3)

button_Generate.grid(row=8, column=1, columnspan=2)

text_Converted.grid(row=9, column=0, columnspan=4)


root.mainloop()

