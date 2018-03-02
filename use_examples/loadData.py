# -*- coding: utf-8 -*- 
# By Denis A.Saveliev
# This script loads RusLawOD data for a given year to a Pandas DataFrame
# It works in Python 3

import pandas as pd
import xml.etree.ElementTree as ET
import glob

year = '2011' # valid years 1991- 
datasetdir = 'xml-texts/' #your path here

#different types of work for different types of data 
fieldsid = ['authorByOP',  'docDateByOP',  'docNumberByOP',   'pravogovruNd',  'IssuedByIPS',  'DocDateIPS' ,  'DocNumberIPS']
fieldsop = ['opdate',  'opnumber', 'opweekcode']
fieldshd = ['headingIPS', 'docTitleByOP', 'docTypeByOP']
fieldstxt = ['textOCR',  'textIPS']
fieldsclass = ['classifierByIPS',  'keywordByIPS']
alldata = [] #we will collect dictionaries to this in order to make a Data Frame of it

#iterate through XML files, parse a file into a dictionary and add to alldata
for inputfilename in glob.glob(datasetdir + str(year) + '*.xml'):
    tree = ET.parse(inputfilename)
    root = tree.getroot()
    bufferdict = {}
    bufferdict['fileid'] = inputfilename[-15:]
    for field in fieldsid:
        try:
            bufferdict[field] = root.find("./meta/identification/" + field).get('val')
        except:
            bufferdict[field] = None

    for field in fieldsop:
        try:
            bufferdict[field] = root.find("./meta/publication/").get(field)
        except:
            bufferdict[field] = None
            
    for field in fieldshd:
        try:
            bufferdict[field] = root.find("./meta/identification/" + field).text
        except:
            bufferdict[field] = None

    for field in fieldstxt:
        try:
            bufferdict[field] = root.find("./body/" + field).text
        except:
            bufferdict[field] = None
    #then since we can have multiple values from classifier and keywords field we have to represent lists of them via semicolon
    kwall = ''
    try:
        kw = root.findall("./meta/keywords/keywordByIPS")    
        for i in kw:
            kwall = kwall + ';' + i.get('val')
        if kwall[0] == ';':
            bufferdict['keywordByIPS'] = kwall[1:]        
    except:
        bufferdict['keywordByIPS'] = None
    clasall = ''
    try:
        cla = root.findall("./meta/references/classifierByIPS")    
        for i in cla:
            clasall = clasall + ';' + i.get('val')
        if clasall[0] == ';':
            bufferdict['classifierByIPS'] = clasall[1:]        
    except:
        bufferdict['classifierByIPS'] = None
            
    alldata.append(bufferdict)

# finally make a dataframe
df = pd.DataFrame(alldata,  columns = ['fileid']+ fieldsid + fieldsop + fieldshd + fieldstxt + fieldsclass)
# print some results:
print(df.info())
print(df['classifierByIPS'])
