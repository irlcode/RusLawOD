# -*- coding: utf-8 -*- 
# By Denis A.Saveliev
# This script loads RusLawOD data to a Pandas DataFrame
# It works in Python 3

import pandas as pd
import xml.etree.ElementTree as ET
import glob
import pyarrow

work_dir = ''  # path
datasetdir = work_dir + 'corpus_xml_full/'  # your path here

# different types of work for different types of data 
fieldsid = ['pravogovruNd',
            'issuedByIPS',
            'docdateIPS' ,
            'docNumberIPS',
            'doc_typeIPS',
            'headingIPS',
            'doc_author_normal_formIPS',
            'signedIPS',
            'statusIPS',
            'actual_datetimeIPS',
            'actual_datetime_humanIPS',
            'is_widely_used',
            ]
fieldshd = ['headingIPS', ]
fieldstxt = ['taggedtextIPS',  'textIPS']
fieldsclass = ['classifierByIPS',  'keywordsByIPS']

def parse_file(inputfilename):
    tree = ET.parse(inputfilename)
    root = tree.getroot()
    bufferdict = {}
    for field in fieldsid:
        try:
            bufferdict[field] = root.find(
                "./meta/identification/" + field).get('val')
        except:
            bufferdict[field] = None


    for field in fieldstxt:
        try:
            bufferdict[field] = root.find("./body/" + field).text
        except:
            bufferdict[field] = None
    # then since we can have multiple values from classifier and keywords
    # field we have to represent lists of them via semicolon
    kwall = ''
    try:
        kw = root.findall("./meta/keywords/keywordsByIPS")    
        for i in kw:
            kwall = kwall + ';' + i.get('val')
        if kwall[0] == ';':
            bufferdict['keywordsByIPS'] = kwall[1:]        
    except:
        bufferdict['keywordsByIPS'] = None
    clasall = ''
    try:
        cla = root.findall("./meta/reference/classifierByIPS")    
        for i in cla:
            clasall = clasall + ';' + i.get('val')
        if clasall[0] == ';':
            bufferdict['classifierByIPS'] = clasall[1:]        
    except:
        bufferdict['classifierByIPS'] = None
            

    return bufferdict

if __name__ == "__main__":
    alldata = []  # we will collect dictionaries to this in order to
    # make a Data Frame of it
    counter = 0
    # iterate through XML files, parse a file into a dictionary and add to alldata
    for inputfilename in glob.glob(datasetdir  + '*.xml'):
        bufferdict = parse_file(inputfilename)
        alldata.append(bufferdict)
        counter += 1
        if counter % 30000 == 0:
            print(counter)
            df = pd.DataFrame(alldata,
                              columns = fieldsid + fieldstxt + fieldsclass)
            df.to_parquet(work_dir + 'ruslawod' + str(counter) + '.parquet',
                          engine='pyarrow')
            alldata = []

    print(counter)
    df = pd.DataFrame(alldata,  columns = fieldsid + fieldstxt + fieldsclass)
    df.to_parquet(work_dir + 'ruslawod' + str(counter)  + '.parquet',
                  engine='pyarrow')
