# from sys import argv
from tkinter import *
from tkinter import filedialog
# from Tkinter import * #try this if in terminal don't work
import datetime


root = Tk()

# script, filename, dataType = argv

# ****** temporary variables ******
filename = "MT-1000E V2_IC_1.h"
outputFilename = "DSP_1701.c"

# ******* constants **********
kkPROGRAM = 0
kkPARAM = 1
kkHW = 2

kPROGRAM = "ADI_REG_TYPE Program_Data"
kRepeatPROGRAM = "0x00, 0x00, 0x00, 0x00, 0x01,"

kPARAMETER = "ADI_REG_TYPE Param_Data"
kRepeatPARAM = "0x00, 0x00, 0x00, 0x00,"

kHW_CONFIG = "ADI_REG_TYPE R3_HWCONFIGURATION"

def extractPROGRAM_PARAMETER_HWCONFIG(dataType):
    varType = int(dataType)  # depend on user selection, default is zero
    if varType == kkPROGRAM:
        writeFileName = "_PROGRAM.tmp"
        varTypeText = kPROGRAM
        varTypeTextRepeat = kRepeatPROGRAM
    elif varType == kkPARAM:
        writeFileName = "_PARAM.tmp"
        varTypeText = kPARAMETER
        varTypeTextRepeat = kRepeatPARAM
    elif varType == kkHW:
        writeFileName = "_HWCONFIG.tmp"
        varTypeText = kHW_CONFIG

    try:
        myFile = open(filename, "r")
        writeFile = open(writeFileName, "w")
    except IOError as e:
        print("Cannot open due to I/O error({0}): {1}".format(e.errno, e.strerror))
    else:
        # find iFrom (beginning)
        for i, line in enumerate(myFile):
            if varTypeText in line:
                print("{0} found at line {1}".format(line, i + 1))
                break
        iFrom = i + 2  # offset is 2
        myFile.close()  # so that the next enumeration won't continue adding up

        # find iParenthesis (end of program data)
        myFile = open(filename, "r")
        for i, line in enumerate(myFile):
            if i >= int(iFrom) - 1:
                if "};" in line:
                    print("{0} found at line {1}".format(line, i + 1))
                    break

        iParenthesis = i + 1
        print("iParenthesis is {0}".format(iParenthesis))
        myFile.close()

        # find repeat start, and find iTo
        if varType != kkHW:  # HW config no need to find repetition, so skip through this
            myFile = open(filename, "r")
            iPrev = 0
            iDiffCount = 0
            iFlag = 0
            repeatCount = 6  # how many times repetition considered as repetition
            for i, line in enumerate(myFile):
                if i >= int(iFrom) - 1 and i < int(iParenthesis):
                    if varTypeTextRepeat in line:
                        # print("{0} found at line {1}".format(line, i+1))
                        iDiff = i + 1 - iPrev
                        if iFlag == 1:  # "watch out for repeat" flag to catch continuous repeat
                            if iDiff != 1:
                                iDiffCount = 0  # clear repeat counter
                                iFlag = 0  # clear "watch out for repeat" flag
                        if iDiff == 1:
                            # print("{0} found at line before repeat at line {1}".format(line, i-1))
                            iDiffCount += 1  # increment for repeating same line
                            iFlag = 1
                        # if more than 4 lines repeating
                        if iDiffCount > repeatCount:
                            print("{0} found at 10 lines after repeat at line {1}".format(line, i - 1))
                            break
                        iPrev = i + 1
            iTo = i - 1 - repeatCount
            print("iTo is -{0} lines, {1}".format(repeatCount, iTo))
            myFile.close()
        else:  # this is if equal to HW_CONFIG, assign iTo to line before Parenthesis
            iTo = iParenthesis - 1

        # extract by line number
        myFile = open(filename, "r")
        for i, line in enumerate(myFile):
            if i >= int(iFrom) - 1 and i < int(iTo):
                # copy to new file
                writeFile.write(line)

            elif i >= int(iTo):
                break

        # file size is just total number of lines
        fileSize = iTo - iFrom + 1  # TODO: confirm is need to + 1, line number count starting with 1 or 0
        print("File Size is {0}".format(fileSize))
        myFile.close()
        writeFile.close()

def browseInput():
    filename = filedialog.askopenfilename()
    entry_inputFileName.delete(0, END)
    entry_inputFileName.insert(END, filename)
    # print("i am browse input")
    # text_log.insert(END, "i am browse input\n")

def browseOutput():
    print(" i am browse output")
    outputFilename = filedialog.askopenfilename()
    entry_outputFileName.delete(0, END)
    entry_outputFileName.insert(END, outputFilename)
    # text_log.insert(END, "i am browse output\n")

def convertAction():
    print("i am convert button")
    checkCheckBoxStates()
    text_log.insert(END, getCurrentTime() + "i am bconvert\n")

def getCurrentTime():
    dateStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
    return dateStr

def checkCheckBoxStates():
    print("PROGRAM state {0}\nPARAM state {1}\nHW_CONFIG {2}\n ".format(var1.get(), var2.get(), var3.get()))
# extractPROGRAM_PARAMETER_HWCONFIG(dataType)

# ******** label *********

label_inputFileName = Label(text="Input")
label_outputFileName = Label(text="Output")

# ****** user input textbox *******

entry_inputFileName = Entry(root, width=70)
entry_outputFileName = Entry(root, width=70)

# ****** Text Box *********
text_log = Text(root, height=20, width=80)

# *******Buttons ******* TODO: add command
button_BrowseInput = Button(text="...", command=browseInput)
button_BrowseOutput = Button(text="...", command=browseOutput)

button_Convert = Button(text="Convert", command=convertAction)


# ****** Check button ***********
var1 = IntVar()
Checkbutton(root, text="PROGRAM", variable=var1).grid(row=2, sticky=W)
var2 = IntVar()
Checkbutton(root, text="PARAM", variable=var2).grid(row=3, sticky=W)
var3 = IntVar()
Checkbutton(root, text="HW CONFIG", variable=var3).grid(row=4, sticky=W)

# ****** positioning in grid *********

label_inputFileName.grid(row=0, sticky=E)
entry_inputFileName.grid(row=0, column=1)
button_BrowseInput.grid(row=0, column=2)

label_outputFileName.grid(row=1, sticky=E)
entry_outputFileName.grid(row=1, column=1)
button_BrowseOutput.grid(row=1, column=2)

button_Convert.grid(row=5, columnspan=3)

text_log.grid(row=6, columnspan=3)

root.mainloop()
