from sys import argv

script, filename = argv

# ******* constants **********
kPROGRAM = "ADI_REG_TYPE Param_Data"
kRepeatPROGRAM = "0x00, 0x00, 0x00, 0x00,"

# ADI_REG_TYPE Param_Data
# 0x00, 0x00, 0x00, 0x00,
# ADI_REG_TYPE Program_Data
# 0x00, 0x00, 0x00, 0x00, 0x01,
kPARAMETER = "Param_Data"
kRepeatPARAM = ""

kHW_CONFIG = "R3_HWCONFIGURATION"


try:
    myFile = open(filename, "r")
    writeFile = open("newwriteFile.txt", "w")
except IOError as e:
    print("Cannot open due to I/O error({0}): {1}".format(e.errno, e.strerror))
else:
    # find iFrom (beginning)
    for i, line in enumerate(myFile):
        if kPROGRAM in line:
            print("{0} found at line {1}".format(line, i+1))
            break
    iFrom = i + 2 # offset is 2
    myFile.close() # so that the next enumeration won't continue adding up

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
    repeatCount = 10 # how many times repetition considered as repetition
    for i, line in enumerate(myFile):
        if i >= int(iFrom) - 1 and i < int(iParenthesis):
            if kRepeatPROGRAM in line:
                # print("{0} found at line {1}".format(line, i+1))
                iDiff = i+1 - iPrev
                if iDiff == 1:
                    print("{0} found at line before repeat at line {1}".format(line, i-1))
                    iDiffCount += 1 # increment for repeating same line
                # if more than 4 lines repeating
                if iDiffCount > repeatCount:
                    print("{0} found at 4 lines after repeat at line {1}".format(line, i - 1))
                    break
                iPrev = i+1
    iTo = i-1-repeatCount
    print("iTo is {0}".format(iTo))
    myFile.close()


    # extract by line number
    myFile = open(filename, "r")
    for i, line in enumerate(myFile):
        if i >= int(iFrom)-1 and i < int(iTo):
            # copy to new file
            writeFile.write(line)

        elif i >= int(iTo):
            break

    myFile.close()
    writeFile.close()




