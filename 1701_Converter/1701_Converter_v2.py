from sys import argv

script, filename = argv

try:
    myFile = open(filename, "r")
    writeFile = open("newwriteFile.txt", "w")
except IOError as e:
    print("Cannot open due to I/O error({0}): {1}".format(e.errno, e.strerror))
else:
    # find iFrom
    for i, line in enumerate(myFile):
        if "ADI_REG_TYPE Program_Data" in line:
            print("{0} found at line {1}".format(line, i+1))
            break
    iFrom = i + 2 # offset is 2
    iTo = 48 # TODO: remove when iTo is done
    myFile.close() # so that the next enumeration won't continue adding up

    # find iParenthesis (end of program data)
    myFile = open(filename, "r")
    for i, line in enumerate(myFile):
        if "};" in line:
            print("{0} found at line {1}".format(line, i+1))
            break
    iParenthesis = i + 1
    myFile.close()

    # find repeat start
#    myFile = open(filename, "r")
#    iPrev = 0
#    for i, line in enumerate(myFile):
#        if "0x00, 0x00, 0x00, 0x00, 0x01," in line:
#            print("{0} found at line {1}".format(line, i+1))
#            iPrev = i
#            break
#    iParenthesis = i
#    myFile.close()


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




