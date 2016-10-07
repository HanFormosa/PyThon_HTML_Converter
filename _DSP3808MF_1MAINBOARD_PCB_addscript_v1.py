# from sys import argv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import errno
# from Tkinter import * #try this if in terminal don't work
import datetime
import fileinput
import atexit
from shutil import copyfile


root = Tk()

# ******* constants ******
saveFileLocation = "/"
inputFilename = ""

def browseInput():
    inputFilename = filedialog.askopenfilename()
    entry_file.delete(0, END)
    entry_file.insert(END, inputFilename)
#def editReleaseNote():
#    print("release")
# /Volumes/Macintosh HD/Formosa/SoftwareReleases/SupportingFile/DSP3808MF/v1.47_unified.hex

def doUpload():

    # upload means copy file from input filename to default location
    strModelRoot = "/Volumes/Macintosh HD/Formosa/SoftwareReleases/SupportingFile/DSP3808MF/1.MAIN BOARD/PCB/"
    strVersion = entry_version.get()
    strTotal = strModelRoot + strVersion
    print(strTotal)

    if not os.path.exists(strTotal):
        try:
            os.makedirs(strTotal)
        except OSError as exception:
            messagebox.showerror("Error", "OS Error: {0}".format(exception.strerror))
            #if exception.errno != errno.EEXIST:
            #    raise
        else: # if no OS error
            # extract Filename
            file_path = entry_file.get()
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
                        # entry_rel_sub1.insert(0, fileName)
                        print(strTotal + "/" + fileName)
                        break



    #try:
    #    copyfile(entry_file.get(), tmpDST)
    #except IOError as e:
    #    print("Destination file not writable. I/O error({0}): {1}".format(e.errno, e.strerror))

    # after complete upload, open excel file release note for editing.

    # include macro in excel file to create .htm file when excel file closed

# ******** label *********
label_Title = Label(text="DSP3808MF")
label_SubTitle = Label(text="1.MAIN BOARD")

label_version = Label(text="Version")
label_file = Label(text="File")

# ****** user input textbox *******
entry_version = Entry(root)
entry_file = Entry(root)

# *******Buttons *******
button_BrowseInput = Button(text="...", command=browseInput)

# button_editReleaseNote = Button(text="Edit", command=editReleaseNote)

button_upload = Button(text="Upload", command=doUpload)


# ********* text log *********** TODO: add text log to warn if directory can't be found.

# ********** positioning *************
label_Title.grid(row=0, columnspan=3)
label_SubTitle.grid(row=1, columnspan=3)

label_version.grid(row=2, sticky=E)
entry_version.grid(row=2, column=1)

label_file.grid(row=3, sticky=E)
entry_file.grid(row=3, column=1)
button_BrowseInput.grid(row=3, column=2)

button_upload.grid(row=4, columnspan=3)

# initial value
entry_version.insert(END, "V1.0")

root.mainloop()

