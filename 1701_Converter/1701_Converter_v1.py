from sys import argv

#script, first, second, third = argv
script, filename= argv


# ******** constants ************#
kPROGRAM = "Program_Data"
kPARAMETER = "Param_Data"
kHW_CONFIG = "R3_HWCONFIGURATION"


FOUNDPROGRAM = 0
FOUNDPARAM = 0
FOUUNDHWCONFIG = 0

print("the script is called ", script)
print("first object is ", filename)
# print("second object is ", second)
# print("third object is ", third)

# file_object = open(filename, mode) where file_object is the variable to put the file object.
# ----The second argument describes the way in which the file will be used.

# The modes can be:

# 'r' when the file will only be read

# 'w' for only writing (an existing file with the same name will be erased)

# 'a' opens the file for appending; any data written to the file is automatically added to the end.

# 'r+' opens the file for both reading and writing.

# ------------------file read write example -------------------######
# file = open("newfile.txt", "w")
# file.write("I'm a new file 1")
# file.close()

# file = open("newfile.txt", "r")
# print(file.read())
# file.close()

# ------------------ try catch exception example--------------#####
# while True:
# ...     try:
# ...         x = int(raw_input("Please enter a number: "))
# ...         break
# ...     except ValueError:
# ...         print "Oops!  That was no valid number.  Try again..."

def extractProgramData(line):
    print("Extracting program data")

def extractParamData(line):
    print("Extracting parameter data")

def extractHWConfig(line):
    print("Extracting HW config data")


try:
    file = open(filename, "r")
except IOError as e:
    print("Cannot open due to I/O error({0}): {1}".format(e.errno, e.strerror))
else:
    # print(file.readline())
    # j = enumerate(file, 1)
    # print(" j is result of enumerate ", j)

    for num, line in enumerate(file, 1):
        if "line 3" in line:
            print("found at line:", num)

    for line in file:
        # print(line)
        # find key word , if can't find, returned value is -1; index of string starts with 0

        i = line.find(kPROGRAM)

        if i != -1:
            print("kPROGRAM index is ", i)
            FOUNDPROGRAM = 1

            # run extract program data function

            # find ending of program by detecting '};' characters

            # find repeating 0x00, 0x00, 0x00, 0x01,

            # use line number to extract?

            # write to file
            break
        # for x in range(0, len(line)):
        #    char_temp = line[x]

    file.close()






