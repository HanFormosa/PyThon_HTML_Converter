from sys import argv

script, filename, dataType = argv

# ******* constants **********
kkPROGRAM = 0
kkPARAM = 1
kkHW = 2

kPROGRAM = "ADI_REG_TYPE Program_Data"
kRepeatPROGRAM = "0x00, 0x00, 0x00, 0x00, 0x01,"

kPARAMETER = "ADI_REG_TYPE Param_Data"
kRepeatPARAM = "0x00, 0x00, 0x00, 0x00,"

kHW_CONFIG = "R3_HWCONFIGURATION"

varType = int(dataType)  # depend on user selection, default is zero
if varType == kkPROGRAM:
    writeFileName = "PROGRAM.txt"
    varTypeText = kPROGRAM
    varTypeTextRepeat = kRepeatPROGRAM
elif varType == kkPARAM:
    writeFileName = "PARAM.txt"
    varTypeText = kPARAMETER
    varTypeTextRepeat = kRepeatPARAM
elif varType == kkHW:
    writeFileName = "HWCONFIG.txt"

try:
    myFile = open(filename, "r")
    writeFile = open(writeFileName, "w")
except IOError as e:
    print("Cannot open due to I/O error({0}): {1}".format(e.errno, e.strerror))
else:
    # find iFrom (beginning)
    for i, line in enumerate(myFile):
        if varTypeText in line:
            print("{0} found at line {1}".format(line, i+1))
            break
    iFrom = i + 2  # offset is 2
    myFile.close()  # so that the next enumeration won't continue adding up

    # find iParenthesis (end of program data)
    myFile = open(filename, "r")
    for i, line in enumerate(myFile):
        if i >= int(iFrom)-1:
            if "};" in line:
                print("{0} found at line {1}".format(line, i + 1))
                break

    iParenthesis = i + 1
    print("iParenthesis is {0}".format(iParenthesis))
    myFile.close()

    # find repeat start, and find iTo
    myFile = open(filename, "r")
    iPrev = 0
    iDiffCount = 0
    iFlag = 0
    repeatCount = 6 # how many times repetition considered as repetition
    for i, line in enumerate(myFile):
        if i >= int(iFrom) - 1 and i < int(iParenthesis):
            if varTypeTextRepeat in line:
                # print("{0} found at line {1}".format(line, i+1))
                iDiff = i+1 - iPrev
                if iFlag == 1: # "watch out for repeat" flag to catch continuous repeat
                    if iDiff != 1:
                        iDiffCount = 0  # clear repeat counter
                        iFlag = 0  # clear "watch out for repeat" flag
                if iDiff == 1:
                    # print("{0} found at line before repeat at line {1}".format(line, i-1))
                    iDiffCount += 1 # increment for repeating same line
                    iFlag = 1
                # if more than 4 lines repeating
                if iDiffCount > repeatCount:
                    print("{0} found at 10 lines after repeat at line {1}".format(line, i - 1))
                    break
                iPrev = i+1
    iTo = i-1-repeatCount
    print("iTo is -{0} lines, {1}".format(repeatCount, iTo))
    myFile.close()


    # extract by line number
    myFile = open(filename, "r")
    for i, line in enumerate(myFile):
        if i >= int(iFrom)-1 and i < int(iTo):
            # copy to new file
            writeFile.write(line)

        elif i >= int(iTo):
            break

    # file size is just total number of lines
    fileSize = iTo - iFrom # TODO: confirm is need to + 1, line number count starting with 1 or 0
    print("File Size is {0}".format(fileSize))
    myFile.close()
    writeFile.close()




