from sys import argv

script, filename, iFrom, iTo = argv


try:
    myFile = open(filename, "r")
    writeFile = open("newwriteFile.txt", "w")
except IOError as e:
    print("Cannot open due to I/O error({0}): {1}".format(e.errno, e.strerror))
else:
    for i, line in enumerate(myFile):
        if i >= int(iFrom)-1 and i < int(iTo):
            # print(line)
            # copy to new file
            writeFile.write(line)

        elif i >= int(iTo):
            break
    myFile.close()
    writeFile.close()

