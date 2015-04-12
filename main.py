import os
import sys
import json
from tkinter import *
from tkinter import filedialog


import hashgen
import FileScan

def fileProcessing(filePath):
    md5 = hashgen.CheckSum.md5Checksum(filePath)
    jsonPath = filePath + '_report.json'
    f = open(jsonPath, 'wb')
    f.write (FileScan.Report.retriveReport(md5))
    f.close()
    jsonFile = open(jsonPath, 'r')
    jsonDict =  (json.loads(jsonFile.read()))
    jsonFile.close()
    return jsonDict

def parser(jsonDict):
    result = ['Report:']
    if jsonDict['response_code'] == 0:
        result.append('No file info at VT')
    else:
        for av in jsonDict['scans']:
            if jsonDict['scans'][av]['detected'] == True:
               result.append('  ' + av + ' : ' + jsonDict['scans'][av]['result'])
    return result

def window_deleted():
    root.quit()

root = Tk()
root.title('VT Checker')
# root.geometry('500x400+300+200')
root.protocol('WM_DELETE_WINDOW', window_deleted)
root.resizable(True, False)
filePath=filedialog.askopenfilename(parent=root)
outputText = '\n'.join(parser(fileProcessing(filePath)))
label1=Label(root,text=outputText,font='arial 10',justify='left',compound='left')
label1.pack(side = 'top')
root.mainloop()





