from tkinter import *
from tkinter import messagebox

root = Tk()
# ========= constants ==========
kITEM1 = 0
kITEM2 = 1
kITEM3 = 2
kITEM4 = 3
kITEM5 = 4
kITEM6 = 5
kITEM7 = 6

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

def insertTable(item):
    if item == kITEM1:
        strItem = entry_item1.get()
    elif item == kITEM2:
        strItem = entry_item2.get()
    elif item == kITEM3:
        strItem = entry_item3.get()
    elif item == kITEM4:
        strItem = entry_item4.get()
    elif item == kITEM5:
        strItem  = entry_item5.get()
    elif item == kITEM6:
        strItem = entry_item6.get()
    elif item == kITEM7:
        strItem = entry_item7.get()
    else:
        strItem = ""
    # ============ TAble generation item 1 =======================
    strTable1 = "<h3 id=\"" + entry_item1_tag.get() + "\"><b>1." + entry_item1.get() + "</b></h3>\n"
    if entry_subitem1.get().upper() == "SCHEMATICS":
        strTable2 = "<p><u>Schematics</u></p>\n"
        strTable3 = "<table>\n"
        #    strTable4 = "\t<table>\n"
        strTable5 = "\t<tr>\n"
        strTable6 = "\t\t<th>Version</th>\n"
        strTable7 = "\t\t<th>Date</th>\n"
        strTable8 = "\t\t<th>Release Note</th>\n"
        strTable9 = "\t</tr>\n"
        strTable10 = "\t<tr>\n"
        strTable11 = "\t\t<td>N/A</td>\n"
        strTable12 = "\t\t<td>N/A</td>\n"
        strTable13 = "\t\t<td>N/A</td>\n"
        strTable14 = "\t</tr>\n"
        strTable15 = "</table>\n\n"

        strTotalTable1 = strTable1 + strTable2 + strTable3 + strTable5 + strTable6 + strTable7 + strTable8 + strTable9 + strTable10 + strTable11 + strTable12 + strTable13 + strTable14 + strTable15
        # writeFile.write(strTable1 + strTable2 + strTable3 + strTable5 + strTable6 + strTable7 + strTable8 + strTable9 + strTable10 + strTable11 + strTable12 + strTable13 + strTable14 + strTable15)
        strTable2 = "<p><u>Layouts</u></p>\n"
        strTable3 = "<table>\n"
        #    strTable4 = "\t<table>\n"
        strTable5 = "\t<tr>\n"
        strTable6 = "\t\t<th>Version</th>\n"
        strTable7 = "\t\t<th>Date</th>\n"
        strTable8 = "\t\t<th>Release Note</th>\n"
        strTable9 = "\t</tr>\n"
        strTable10 = "\t<tr>\n"
        strTable11 = "\t\t<td>N/A</td>\n"
        strTable12 = "\t\t<td>N/A</td>\n"
        strTable13 = "\t\t<td>N/A</td>\n"
        strTable14 = "\t</tr>\n"
        strTable15 = "</table>\n\n"

        strTotalTable2 = strTable2 + strTable3 + strTable5 + strTable6 + strTable7 + strTable8 + strTable9 + strTable10 + strTable11 + strTable12 + strTable13 + strTable14 + strTable15
        # writeFile.write(strTable2 + strTable3 + strTable5 + strTable6 + strTable7 + strTable8 + strTable9 + strTable10 + strTable11 + strTable12 + strTable13 + strTable14 + strTable15)

        strTotal = strTotalTable1 + strTotalTable2

        return strTotal
    else:
        # when it's not schematics
        strTable2 = "<p><u>" + entry_subitem1.get() + "</u></p>\n"
        strTable3 = "<table>\n"
        #    strTable4 = "\t<table>\n"
        strTable5 = "\t<tr>\n"
        strTable6 = "\t\t<th>Version</th>\n"
        strTable7 = "\t\t<th>Date</th>\n"
        strTable8 = "\t\t<th>Release Note</th>\n"
        strTable9 = "\t</tr>\n"
        strTable10 = "\t<tr>\n"
        strTable11 = "\t\t<td>N/A</td>\n"
        strTable12 = "\t\t<td>N/A</td>\n"
        strTable13 = "\t\t<td>N/A</td>\n"
        strTable14 = "\t</tr>\n"
        strTable15 = "</table>\n\n"

        # writeFile.write(strTable1 + strTable2 + strTable3 + strTable5 + strTable6 + strTable7 + strTable8 + strTable9 + strTable10 + strTable11 + strTable12 + strTable13 + strTable14 + strTable15)
        strTotal = strTable1 + strTable2 + strTable3 + strTable5 + strTable6 + strTable7 + strTable8 + strTable9 + strTable10 + strTable11 + strTable12 + strTable13 + strTable14 + strTable15
        return strTotal

def doGenerate():
    print(" i am generate")
    writeFilename = entry_fileName.get() + ".html"
    if entry_fileName.get() == "":
        messagebox.showerror("Error", "No filename specified")
    elif entry_item1_tag == "":
        messagebox.showerror("Error", "Please press Make Tag button")
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
            strPart2 = "<html>\n"
            strPart3 = "<head>\n"
            strPart4 = "<link rel=\"stylesheet\" type=\"text/css\" href=\"_common.css\">\n"
            strPart5 = "</head>\n"
            strPart6 = "<body>\n\n"

            writeFile.write(strPart1+strPart2+strPart3+strPart4+strPart5+strPart6)

            #  <h3 id="content">MODEL - Schematics/Layout</h3>
            # Decide whether it's Schematic/Layouts or AP PRogram or ??
            if entry_subitem1.get().upper() == "SCHEMATICS":
                strTitleType = "Schematics/Layouts"
            elif entry_subitem1.get().upper() == "":
                strTitleType = "UNKNOWN"
            else:
                strTitleType = entry_subitem1.get()

            strTitle = "<h3 id=\"content\">" + entry_modelName.get() + " - " + strTitleType + "</h3>\n\n"

            writeFile.write(strTitle)

            strPart1 = "<p><b>&#30446;&#37636;</b><p>\n"
            strPart2 = "<ol type=\"1\">\n"

            writeFile.write(strPart1 + strPart2)
            # make for loop from item 1 to 7. if not empty, write to file, if empty, stop loop. need to warn if nothing is inside?
            if entry_item1.get() != "" or entry_item1_tag != "":
                strWrite = "\t<li><a href=\"" + entry_item1_tag.get() + "\">" + entry_item1.get() + "</a></li>\n"
                writeFile.write(strWrite)
            if entry_item2.get() != "" or entry_item2_tag != "":
                strWrite = "\t<li><a href=\"" + entry_item2_tag.get() + "\">" + entry_item2.get() + "</a></li>\n"
                writeFile.write(strWrite)
            if entry_item3.get() != "" or entry_item3_tag != "":
                strWrite = "\t<li><a href=\"" + entry_item3_tag.get() + "\">" + entry_item3.get() + "</a></li>\n"
                writeFile.write(strWrite)
            if entry_item4.get() != "" or entry_item4_tag != "":
                strWrite = "\t<li><a href=\"" + entry_item4_tag.get() + "\">" + entry_item4.get() + "</a></li>\n"
                writeFile.write(strWrite)
            if entry_item5.get() != "" or entry_item5_tag != "":
                strWrite = "\t<li><a href=\"" + entry_item5_tag.get() + "\">" + entry_item5.get() + "</a></li>\n"
                writeFile.write(strWrite)
            if entry_item6.get() != "" or entry_item6_tag != "":
                strWrite = "\t<li><a href=\"" + entry_item6_tag.get() + "\">" + entry_item6.get() + "</a></li>\n"
                writeFile.write(strWrite)
            if entry_item7.get() != "" or entry_item7_tag != "":
                strWrite = "\t<li><a href=\"" + entry_item7_tag.get() + "\">" + entry_item7.get() + "</a></li>\n"
                writeFile.write(strWrite)

            strPart1 = "</ol>\n\n"
            strPart2 = "<hr>\n\n"
            writeFile.write(strPart1 + strPart2)

            strReturned = insertTable(kITEM1)
            writeFile.write(strReturned)
            # ==================  END body =================
            strEnd1 = "</body>\n"
            strEnd2 = "</html>\n"
            writeFile.write(strEnd1 + strEnd2)
            writeFile.close()

def init():
    entry_item1.insert(END, "MAIN POWER")
    entry_item2.insert(END, "BGM")
    entry_item3.insert(END, "POWER SUPPLY")
    entry_item4.insert(END, "POWER AMP")
    entry_item5.insert(END, "STK")
    entry_item6.insert(END, "PRIORITY")
    entry_item7.insert(END, "ETHERNET")

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
entry_subitem2 = Entry(root)

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
