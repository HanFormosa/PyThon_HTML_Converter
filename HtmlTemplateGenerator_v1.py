from tkinter import *
from tkinter import messagebox

root = Tk()

def makeTag():

    # get text from entry item, convert to TAG by grabbing the first two letter of each word (if more than 1 words)
    # if only 1 word, take first 2 characters
    entryText = entry_item1.get().upper()
    entry_item1_tag.delete(0, END)
    if (entryText != ""):
        # find the first "space" character
        spaceIndex = entryText.find(" ")
        if spaceIndex == -1:
            # this means can't find the space which also means only one continuous word
            entry_item1_tag.insert(END, "#" + entryText[0:2])
        else:
            # first letter of each word (two)
            entry_item1_tag.insert(END, "#" + entryText[0] + entryText[spaceIndex + 1])

    entryText = entry_item2.get().upper()
    entry_item2_tag.delete(0, END)
    if (entryText != ""):
        # find the first "space" character
        spaceIndex = entryText.find(" ")
        if spaceIndex == -1:
            # this means can't find the space which also means only one continuous word
            entry_item2_tag.insert(END, "#" + entryText[0:2])
        else:
            # first letter of each word (two)
            entry_item2_tag.insert(END, "#" + entryText[0] + entryText[spaceIndex + 1])

    entryText = entry_item3.get().upper()
    entry_item3_tag.delete(0, END)
    if (entryText != ""):
        # find the first "space" character
        spaceIndex = entryText.find(" ")
        if spaceIndex == -1:
            # this means can't find the space which also means only one continuous word
            entry_item3_tag.insert(END, "#" + entryText[0:2])
        else:
            # first letter of each word (two)
            entry_item3_tag.insert(END, "#" + entryText[0] + entryText[spaceIndex + 1])

    entryText = entry_item4.get().upper()
    entry_item4_tag.delete(0, END)
    if (entryText != ""):
        # find the first "space" character
        spaceIndex = entryText.find(" ")
        if spaceIndex == -1:
            # this means can't find the space which also means only one continuous word
            entry_item4_tag.insert(END, "#" + entryText[0:2])
        else:
            # first letter of each word (two)
            entry_item4_tag.insert(END, "#" + entryText[0] + entryText[spaceIndex + 1])
    
    entryText = entry_item5.get().upper()
    entry_item5_tag.delete(0, END)
    if (entryText != ""):
        # find the first "space" character
        spaceIndex = entryText.find(" ")
        if spaceIndex == -1:
            # this means can't find the space which also means only one continuous word
            entry_item5_tag.insert(END, "#" + entryText[0:2])
        else:
            # first letter of each word (two)
            entry_item5_tag.insert(END, "#" + entryText[0] + entryText[spaceIndex + 1])
    
    entryText = entry_item6.get().upper()
    entry_item6_tag.delete(0, END)
    if (entryText != ""):
        # find the first "space" character
        spaceIndex = entryText.find(" ")
        if spaceIndex == -1:
            # this means can't find the space which also means only one continuous word
            entry_item6_tag.insert(END, "#" + entryText[0:2])
        else:
            # first letter of each word (two)
            entry_item6_tag.insert(END, "#" + entryText[0] + entryText[spaceIndex + 1])
            
    entryText = entry_item7.get().upper()
    entry_item7_tag.delete(0, END)
    if (entryText != ""):
        # find the first "space" character
        spaceIndex = entryText.find(" ")
        if spaceIndex == -1:
            # this means can't find the space which also means only one continuous word
            entry_item7_tag.insert(END, "#" + entryText[0:2])
        else:
            # first letter of each word (two)
            entry_item7_tag.insert(END, "#" + entryText[0] + entryText[spaceIndex + 1])
    
def doGenerate():
    print(" i am generate")
    writeFilename = entry_fileName.get() + ".html"
    if entry_fileName.get() == "":
        messagebox.showerror("Error", "No filename specified")
    else:
        # filename is valid
        try:
            writeFile = open(writeFilename, "w")
        except IOError as e:
            print("Cannot open due to I/O error({0}): {1}".format(e.errno, e.strerror))
        else:
            # start writing file
            # <!DOCTYPE html>
            # <html lang="en">
            # <body>
            strPart1 = "<!DOCTYPE html>\n"
            strPart2 = "<html lang=\"en\">\n"
            strPart3 = "<body>\n"

            writeFile.write(strPart1+strPart2+strPart3)

            #  <h3 id="content">MODEL - Schematics/Layout</h3>
            # Decide whether it's Schematic/Layouts or AP PRogram or ??
            if entry_subitem1.get().upper() == "SCHEMATICS":
                strTitleType = "Schematics/Layouts"
            elif entry_subitem1.get().upper() == "":
                strTitleType = "UNKNOWN"
            else:
                strTitleType = entry_subitem1.get()

            strTitle = "<h3 id=\"content\">" + entry_modelName.get() + " - " + strTitleType + "</h3>\n"

            writeFile.write(strTitle)

            strPart1 = "<p>Content</p>\n"
            strPart2 = "<ol>\n"
            # make for loop from item 1 to 7. if not empty, write to file, if empty, stop loop. need to warn if nothing is inside?



def init():
    entry_item1.insert(END, "MAIN POWER")
    entry_item2.insert(END, "MAIN POWER")
    entry_item3.insert(END, "MAIN POWER")
    entry_item4.insert(END, "MAIN POWER")
    entry_item5.insert(END, "MAIN POWER")
    entry_item6.insert(END, "MAIN POWER")
    entry_item7.insert(END, "MAIN POWER")

    entry_fileName.insert(END, "SVS1000D")
    entry_modelName.insert(END, "SVS-1000D")
    entry_subitem1.insert(END, "Schematics")
# ******** label *********
label_fileName = Label(text="File Name (.html):")
label_modelName = Label(text="Model Name:")
label_Menu = Label(text="Menu")
label_item1 = Label(text="1.")
label_item2 = Label(text="2.")
label_item3 = Label(text="3.")
label_item4 = Label(text="4.")
label_item5 = Label(text="5.")
label_item6 = Label(text="6.")
label_item7 = Label(text="7.")

label_subMenu = Label(text="Sub Menu")

label_subitem1 = Label(text="1.")
label_subitem2 = Label(text="2.")

# ****** user input textbox *******
entry_fileName = Entry(root)
entry_modelName = Entry(root)

entry_item1 = Entry(root)
entry_item1_tag = Entry(root)

entry_item2 = Entry(root)
entry_item2_tag = Entry(root)

entry_item3 = Entry(root)
entry_item3_tag = Entry(root)

entry_item4 = Entry(root)
entry_item4_tag = Entry(root)

entry_item5 = Entry(root)
entry_item5_tag = Entry(root)

entry_item6 = Entry(root)
entry_item6_tag = Entry(root)

entry_item7 = Entry(root)
entry_item7_tag = Entry(root)

# in each section (Schematics/Layout or none)
entry_subitem1 = Entry(root)
entry_subitem1_tag = Entry(root)
entry_subitem2 = Entry(root)
entry_subitem2_tag = Entry(root)

# *******Buttons ******* TODO: add command
button_MakeTag = Button(text="Make Tag", command=makeTag)
button_generate = Button(text="Generate", command=doGenerate)

# ****** positioning in grid *********
label_fileName.grid(row=0, sticky=E)
entry_fileName.grid(row=0, column=1)

label_modelName.grid(row=1, sticky=E)
entry_modelName.grid(row=1, column=1)

label_Menu.grid(row=2, column=0, columnspan=4)

label_item1.grid(row=3, sticky=E)
entry_item1.grid(row=3, column=1)
entry_item1_tag.grid(row=3, column=2)

label_item2.grid(row=4, sticky=E)
entry_item2.grid(row=4, column=1)
entry_item2_tag.grid(row=4, column=2)

label_item3.grid(row=5, sticky=E)
entry_item3.grid(row=5, column=1)
entry_item3_tag.grid(row=5, column=2)

label_item4.grid(row=6, sticky=E)
entry_item4.grid(row=6, column=1)
entry_item4_tag.grid(row=6, column=2)

label_item5.grid(row=7, sticky=E)
entry_item5.grid(row=7, column=1)
entry_item5_tag.grid(row=7, column=2)

label_item6.grid(row=8, sticky=E)
entry_item6.grid(row=8, column=1)
entry_item6_tag.grid(row=8, column=2)

label_item7.grid(row=9, sticky=E)
entry_item7.grid(row=9, column=1)
entry_item7_tag.grid(row=9, column=2)

button_MakeTag.grid(row=9, column=3)

label_subMenu.grid(row=10, columnspan=4)

label_subitem1.grid(row=11, sticky=E)
entry_subitem1.grid(row=11, column=1)

label_subitem2.grid(row=12, sticky=E)
entry_subitem2.grid(row=12, column=1)

button_generate.grid(row=13, columnspan=4)

init()
root.mainloop()
