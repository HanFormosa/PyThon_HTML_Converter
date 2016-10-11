# from sys import argv
from tkinter import *
from tkinter import filedialog
# from Tkinter import * #try this if in terminal don't work
import datetime
import fileinput
import atexit
from shutil import copyfile


root = Tk()

# script, filename, dataType = argv

# ****** temporary variables ******
# filename = "MT-1000E V2_IC_1.h"
# outputFilename = "DSP_1701.c"

globalErrorFlag = 0  # check this status on convert to see if there's any error

# ******* constants **********
kkPROGRAM = 0
kkPARAM = 1
kkHW = 2

kPROGRAM = "ADI_REG_TYPE Program_Data"
kRepeatPROGRAM = "0x00, 0x00, 0x00, 0x00, 0x01,"

kPARAMETER = "ADI_REG_TYPE Param_Data"
kRepeatPARAM = "0x00, 0x00, 0x00, 0x00,"

kHW_CONFIG = "ADI_REG_TYPE R3_HWCONFIGURATION"

# detection string for output files
k2PROGRAM = "PROGRAM_DATA["
k2PARAMETER = "PARAMETER_DATA["
k2HW_CONFIG = "DSP_Regist["


k3PROGRAMSIZE = "#define PROG_Size"
k3PROGRAMSIZE_COMMENT = " //Program Code"
k3PARAMSIZE = "#define PARA_Size"
k3PARAMSIZE_COMMENT = " //Parameter Code"

# global init
configInputFilename = ""
configOutputFilename = ""
configCheckboxPROGRAM = 0
configCheckboxPARAM = 0
configCheckboxHW = 0

def extractPROGRAM_PARAMETER_HWCONFIG(dataType, filename):
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
        text_log.insert(END, getCurrentTime() + "Cannot open file: {0}\n".format(filename))
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
    inputFilename = filedialog.askopenfilename()
    entry_inputFileName.delete(0, END)
    entry_inputFileName.insert(END, inputFilename)
    # print("i am browse input")
    # text_log.insert(END, "i am browse input\n")
    global configInputFilename
    configInputFilename = entry_inputFileName.get()

def browseOutput():
    outputFilename = filedialog.askopenfilename()
    entry_outputFileName.delete(0, END)
    entry_outputFileName.insert(END, outputFilename)
    # text_log.insert(END, "i am browse output\n")
    global configOutputFilename
    configOutputFilename = entry_outputFileName.get()

def convertAction():
    text_log.delete(1.0, END)  # clear text
    doBackUpOutputFile()
    text_log.insert(END, getCurrentTime() + "Starting extraction\n")

    # check checkbox status
    PROGRAM_STATE = var1.get()
    PARAM_STATE = var2.get()
    HW_STATE = var3.get()

    # export tmp files selected using Extract method with filename as input
    if PROGRAM_STATE == 1:
        text_log.insert(END, getCurrentTime() + "Extracting PROGRAM DATA...\n")
        extractPROGRAM_PARAMETER_HWCONFIG(kkPROGRAM, entry_inputFileName.get())
        copyToOutput(kkPROGRAM, entry_outputFileName.get())
        copyProgSize_ParamSize(kkPROGRAM, entry_outputFileName.get())
        if globalErrorFlag == 1:
            text_log.insert(END, getCurrentTime() + "Error happened during extraction: PROGRAM DATA\n")
        else:
            text_log.insert(END, getCurrentTime() + "PROGRAM DATA...done\n")
    if PARAM_STATE == 1:
        text_log.insert(END, getCurrentTime() + "Extracting PARAMETER DATA...\n")
        extractPROGRAM_PARAMETER_HWCONFIG(kkPARAM, entry_inputFileName.get())
        copyToOutput(kkPARAM, entry_outputFileName.get())
        copyProgSize_ParamSize(kkPARAM,entry_outputFileName.get())
        if globalErrorFlag == 1:
            text_log.insert(END, getCurrentTime() + "Error happened during extraction: PARAMETER DATA\n")
        else:
            text_log.insert(END, getCurrentTime() + "PARAMETER DATA...done\n")
    if HW_STATE == 1:
        text_log.insert(END, getCurrentTime() + "Extracting HARDWARE CONFIG DATA...\n")
        extractPROGRAM_PARAMETER_HWCONFIG(kkHW, entry_inputFileName.get())
        copyToOutput(kkHW, entry_outputFileName.get())
        if globalErrorFlag == 1:
            text_log.insert(END, getCurrentTime() + "Error happened during extraction: HW CONFIG DATA\n")
        else:
            text_log.insert(END, getCurrentTime() + "HARDWARE CONFIG DATA...done\n")


def getCurrentTime():
    dateStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
    return dateStr


def storeCheckBoxStates(dataType):
    # print("PROGRAM state {0}\nPARAM state {1}\nHW_CONFIG {2}\n ".format(var1.get(), var2.get(), var3.get()))
    varType = int(dataType)
    if varType == kkPROGRAM:
        global configCheckboxPROGRAM
        configCheckboxPROGRAM = var1.get()
    elif varType == kkPARAM:
        global configCheckboxPARAM
        configCheckboxPARAM = var2.get()
    elif varType == kkHW:
        global configCheckboxHW
        configCheckboxHW = var3.get()

def copyToOutput(dataType, outputFilename):
    varType = int(dataType)  # depend on user selection, default is zero
    if varType == kkPROGRAM:
        varTypeText = k2PROGRAM
        tmpFileName = "_PROGRAM.tmp"
    elif varType == kkPARAM:
        varTypeText = k2PARAMETER
        tmpFileName = "_PARAM.tmp"
    elif varType == kkHW:
        varTypeText = k2HW_CONFIG
        tmpFileName = "_HWCONFIG.tmp"
    # open output filename
    try:
        outputFile = open(outputFilename, "r+")
    except IOError as e:
        print("Cannot open due to I/O error({0}): {1}".format(e.errno, e.strerror))
        text_log.insert(END, getCurrentTime() + "Cannot open file: {0}\n".format(outputFilename))
    else:
        # find PROGRAM if datatype is PROGRAM
        # if found, check if TMP file available, then open TMP file ,delete and replace with _PROGRAM.tmp content
        # find iFrom (beginning)
        for i, line in enumerate(outputFile):
            if varTypeText in line:
                print("OutputFile: {0} found at line {1}".format(line, i + 1))
                break
        iFrom = i + 2  # offset is 2
        outputFile.close()  # so that the next enumeration won't continue adding up

        # find iOpenParenthesis ( in case iFrom is different line from "open parenthesis")
        outputFile = open(outputFilename, "r+")
        for i, line in enumerate(outputFile):
            if i >= int(iFrom) - 2:  # TODO: 2 or 1?
                if "{" in line:
                    print("OutputFile: {0} found at line {1}".format(line, i + 1))
                    break
        iOpenParenthesis = i + 1  # offset is 1
        print("iOpenParenthesis is {0}".format(iOpenParenthesis))
        outputFile.close()  # so that the next enumeration won't continue adding up

        # find iParenthesis (end of program data)
        outputFile = open(outputFilename, "r+")
        for i, line in enumerate(outputFile):
            if i >= int(iFrom) - 1:
                if "};" in line:
                    print("{0} found at line {1}".format(line, i + 1))
                    break

        iParenthesis = i + 1
        print("iParenthesis is {0}".format(iParenthesis))
        outputFile.close()

        if varType != kkHW: # HWconfig need special treatment. not basic delete and replace.
            # remove lines
            for line in fileinput.input(outputFilename, inplace=True):
                if fileinput.lineno() > iOpenParenthesis and fileinput.lineno() < iParenthesis:
                    continue
                print(line, end='')

            # read from tmp file
            outputtmpFile = open(tmpFileName, "r")
            contents = outputtmpFile.readlines()
            outputtmpFile.close()

            # print(contents[0:2])
            tmpStr = ''.join(contents)
            #print("content as string {0}".format(tmpStr))
            # add new text in files

            # myinsert="""new line1\nnew line2\nnew line3"""
            for line in fileinput.input(outputFilename, inplace=1):
                linenum = fileinput.lineno()
                # if linenum==1 or linenum>4 :
                #    line=line.rstrip()
                if linenum == iOpenParenthesis:
                    line = line + tmpStr
                print(line, end='')
        else:
            # check for "//" characters between "{" and "}"., if not commented, comment it.
            for line in fileinput.input(outputFilename, inplace=1):
                linenum = fileinput.lineno()
                if linenum > iOpenParenthesis and linenum < iParenthesis:
                    if "0x" or "0X" in line:
                        if not ("//") in line:
                            line = line.replace(line, "//" + getCurrentTime() + "//" + line)
                print(line, end='')

            # read from tmp file: HW config
            outputtmpFile = open(tmpFileName, "r")
            contents = outputtmpFile.readlines()
            outputtmpFile.close()

            tmpStr = ''.join(contents)
            # insert line from HW CONFIG tmp file
            for line in fileinput.input(outputFilename, inplace=1):
                linenum = fileinput.lineno()
                if linenum == iParenthesis -1:  # insert 1 line before close parenthesis
                    line = line + tmpStr
                print(line, end='')

def copyProgSize_ParamSize(dataType, outputFilename):
    varType = int(dataType)  # depend on user selection, default is zero
    if varType == kkPROGRAM:
        tmpFileName = "_PROGRAM.tmp"
        tmpDetString = k3PROGRAMSIZE
        tmpDetComment = k3PROGRAMSIZE_COMMENT
    elif varType == kkPARAM:
        tmpFileName = "_PARAM.tmp"
        tmpDetString = k3PARAMSIZE
        tmpDetComment = k3PARAMSIZE_COMMENT
    # get file size of _PARAM or _PROGRAM tmp files
    with open(tmpFileName) as f:
        for i, l in enumerate(f):
            pass
    fileSize = i + 1
    #print("file size is : {0}".format(fileSize))
    text_log.insert(END, getCurrentTime() + tmpDetComment + " : " + str(fileSize) + "\n")
    # find #define PRog_Size and insert fileSize
    for line in fileinput.input(outputFilename, inplace=1):
        if tmpDetString in line:
            if (line.find("/") > len(tmpDetString)) or (line.find("/") == -1):
                line = line.replace(line, tmpDetString + "\t" + str(fileSize) + tmpDetComment + "\n")
        print(line, end='')

def exit_handler():
    # print('My application is ending!')
    # write to 1701_Converter.config file
    writeFile = open("1701_Converter.config", "w")
    writeFile.write(configInputFilename + "\n")
    writeFile.write(configOutputFilename + "\n")
    writeFile.write(str(configCheckboxPROGRAM) + "\n")  # PROGRAM Checkbox (bear in mind when reading, these are strings)
    writeFile.write(str(configCheckboxPARAM) + "\n")  # PARAM checkbox
    writeFile.write(str(configCheckboxHW) + "\n")  # HW CONFIG checkbox
    writeFile.close()

def initialiseFromConfig():

    # initialise global variable
    global configInputFilename
    global configOutputFilename
    global configCheckboxPROGRAM
    global configCheckboxPARAM
    global configCheckboxHW

    with open("1701_Converter.config") as f:
        for i, l in enumerate(f):
            if i == 0:
                # print(l.strip('\n'))
                entry_inputFileName.insert(0, l.strip('\n'))
                configInputFilename = entry_inputFileName.get()
            elif i == 1:
                # print(l.strip('\n'))
                entry_outputFileName.insert(0, l.strip('\n'))
                configOutputFilename = entry_outputFileName.get()
            elif i == 2:
                # print(l.strip('\n'))
                cbState = int(l.strip('\n'))
                if cbState == 1:
                    var1.set(1)
                else:
                    var1.set(0)
                configCheckboxPROGRAM = cbState
            elif i == 3:
                cbState = int(l.strip('\n'))
                if cbState == 1:
                    var2.set(1)
                else:
                    var2.set(0)
                configCheckboxPARAM = cbState
            else:
                cbState = int(l.strip('\n'))
                if cbState == 1:
                    var3.set(1)
                else:
                    var3.set(0)
                configCheckboxHW = cbState
    # remember to save to global after read file.

def doBackUpOutputFile():
    tmpDST = entry_outputFileName.get().strip("\n") + ".backup"
    text_log.insert(END, getCurrentTime() + "Making backup file: {0}".format(tmpDST) + "\n")
    try:
        copyfile(entry_outputFileName.get(), tmpDST)
    except IOError as e:
        print("Destination file not writable. I/O error({0}): {1}".format(e.errno, e.strerror))
        text_log.insert(END, getCurrentTime() + "Destination file not writable.: {0}\n".format(tmpDST))

# ******* register handler at program exit*************
atexit.register(exit_handler)

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
Checkbutton(root, text="PROGRAM", variable=var1, command=lambda: storeCheckBoxStates(kkPROGRAM)).grid(row=2, sticky=W)
var2 = IntVar()
Checkbutton(root, text="PARAM", variable=var2, command=lambda: storeCheckBoxStates(kkPARAM)).grid(row=3, sticky=W)
var3 = IntVar()
Checkbutton(root, text="HW CONFIG", variable=var3, command=lambda: storeCheckBoxStates(kkHW)).grid(row=4, sticky=W)

# ****** positioning in grid *********

label_inputFileName.grid(row=0, sticky=E)
entry_inputFileName.grid(row=0, column=1)
button_BrowseInput.grid(row=0, column=2)

label_outputFileName.grid(row=1, sticky=E)
entry_outputFileName.grid(row=1, column=1)
button_BrowseOutput.grid(row=1, column=2)

button_Convert.grid(row=5, columnspan=3)

text_log.grid(row=6, columnspan=3)



# WINDOWS
#entry_inputFileName.insert(0,"C:/_FORMOSA/GitLocal/PythonProjects/firstProject/1701_Converter/MT-1000E V2_IC_1.h")
#entry_outputFileName.insert(0, "C:/_FORMOSA/GitLocal/PythonProjects/firstProject/1701_Converter/DSP1701.c")

# MAC
#entry_inputFileName.insert(0,"/Volumes/Macintosh HD/Formosa/PYThonProjects/PyThon_HTML_Converter/1701_Converter/MT-1000E V2_IC_1.h")
#entry_outputFileName.insert(0,"/Volumes/Macintosh HD/Formosa/PYThonProjects/PyThon_HTML_Converter/1701_Converter/DSP1701.c")


# initialise from config file.
initialiseFromConfig()
# global configInputFilename
# configInputFilename = entry_inputFileName.get()
# configOutputFilename = entry_outputFileName.get()


root.mainloop()

