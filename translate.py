# python 2
# script for multiple find/replace pairs for all HTML/TXT files in a directory.

import os,sys,csv,re, codecs

inputDir = "default"
translateCSV = "dada-mail-translation-de-formal.csv"

#filename;original,translation
data = csv.reader(open(translateCSV,'rU'),delimiter=';')

findReplace = []

for items in data:
    findReplace.append(items)

#sort the list, to first replace long strings
findReplace.sort(key=lambda t: len(t[1]), reverse=True)

def replaceStringInFile(filePath):
   "replaces all findStr by repStr in file filePath"
   tempName = filePath+'~~~'

   inputFile = open(filePath)
   outputFile = open(tempName, 'w')
   fContent = unicode(inputFile.read(), "utf-8")

   for aPair in findReplace:
    if len(aPair[2].decode("utf-8")) > 0: #ignore empty translations
      outputText = re.sub(re.escape(aPair[1].decode("utf-8")), aPair[2].decode("utf-8"), fContent, count=0, flags=0)

   outputFile.write(outputText.encode("utf-8"))

   outputFile.close()
   inputFile.close()

   print "translated {}".format(filePath)
   os.rename(tempName, filePath)

def fileFilter(dummyArg, thisDir, dirChildrenList):
    for thisChild in dirChildrenList:
        if '.html' == os.path.splitext(thisChild)[1] and os.path.isfile(thisDir+'/'+thisChild):
            replaceStringInFile(thisDir+'/'+thisChild)
        if '.txt' == os.path.splitext(thisChild)[1] and os.path.isfile(thisDir+'/'+thisChild):
            replaceStringInFile(thisDir+'/'+thisChild)


os.path.walk(inputDir, fileFilter, None)