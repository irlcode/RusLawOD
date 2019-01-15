# `RusLawOD`: Russian Law Open Data
‘RusLawOD’ is a corpus of texts of Russian Federation legal acts and their metadata.

`Version 0.5`

## State of affairs
Russian legislation is published in official paper journals. Since 1990 legal normative acts cannot enter into force without official publication. Some effort to make electronic databases of legal acts was made in the 1980s.  In the early 1990s commercial information companies created proprietary databases of legislation and court decisions. Starting from 2011 legal acts are supposed to be officially published at the Official Internet portal of legal information ([pravo.gov.ru](http://pravo.gov.ru)). Now it includes both federal, regional, and municipal legislation, but the information is not complete. However, such documents are only in graphical format (scanned TIFF or PDF without a text layer). Only a small share of data are published in structured fashion in well-defined XML format.

## This corpus
This corpus (as of version `0.5`) includes 458,884 XML files representing laws of Russian Federation, decrees by the President of RF, regulations by the government and acts of subjects of the country as well as some municipal regulations published as of December, 2017. XML files feature legal metadata extracted from various sources and the respective texts.

To the moment we combine texts and metadata from two major sources (both from [pravo.gov.ru](http://pravo.gov.ru)): Official electronic publication of graphical scans of documents and IPS Zakonodatelstvo. The latter is a plaintext representation of official journals wherein the legislation was published.
 We relied on [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) to obtain texts from scanned images. Some texts consist of more than 500 pages (actually, we have some texts more than 15000 pages) representing only financial, geographical information in tables of digits or such. We decided to cut OCR of such texts on page 500. See more in Limitations. 

## Importance of schema development
Data should be supplied in a format that is convenient and compatible. We rely on Akoma Ntoso (http://www.akomantoso.org/). However, so far our corpus is not entirely compatible with it: we do not mark-up the internal document structure yet.

## XML structure
XML structure is reported in the below example with comments.All fields are not mandatory and are present in a document only if the information exists.

```xml
<act> <!-- Legal act as the type of a document -->
  <meta> <!-- major sections are metadata and text -->
    <identification> <!-- see the Limitations on information about legal act identification in Russia -->
      <pravogovruNd val="000000000" /> <!-- document internal number at the IPS Zakonodatelstvo 
      website at the moment of download. It may be subject to change -->
      <issuedByIPS val="Entity that issued the act according to the IPS Zakonodatelstvo" />
      <docdateIPS val="00.00.0000" /> <!-- document day of signature according to the IPS 
      Zakonodatelstvo, date format is dd.mm.yyyy-->
      <docNumberIPS val="000" /> <!-- document number at signature according to the IPS Zakonodatelstvo -->
      <headingIPS>title of the document in the IPS Zakonodatelstvo.</headingIPS> 
      <docTypeByOP val="document type according to the Official publication website" /> 
      <authorByOP val="body that issued the act according to the Official publication website" /> 
      <docDateByOP val="00.00.0000" /> <!-- document adoption data by official publication site date format dd.mm.yyyy-->
      <docNumberByOP val="000" /> <!-- document number at signature-->
      <docTitleByOP> title of the document according to official publication site </docTitleByOp> 
    </identification>
    <references>
      <classifierByIPS val="000.000.000.000.000" /> <!-- classification code according to the IPS Zakonodatelstvo -->
    </references>
    <keywords>
      <keywordByIPS val="KEYWORD" /> 
    </keywords>
    <publication>
      <pravogovruOfficial opdate="00.00.0000" opnumber="0000000000000000" opweekcode="0000000000000" /> 
      <!-- official publication number and official publication week code date format dd.mm.yyyy-->
    </publication>
  </meta>
  <body>
    <textIPS><-- Text parsed from the IPS Zakonodatelstvo --> 
    <!-- It can include hyperlinks to other acts, mostly amendments,
    like this: --> text <ref>linked text</ref> text 
    </textIPS>
    <textOCR> <-- Text from OCR of official publication scan -->
    </textOCR> 
    <textOCR truncated="yes"> <-- Text from OCR if it was truncated while OCR -->
    </textOCR> 
  </body>
</act>
```

## Limitations
This corpus does not represent the entirety of the legal acts but rather it represents the universe of documents published electronically in official sources. OCRed texts are not manually adjusted so that they do contain errors if the underlying image is of low quality. Because we have texts exceeding 1000 pages in length we report only the texts up to its 500th page. Some  texts are limited to 25 pages (those that contain numeric tables). Metadata is gathered from official sources and can reflect the errors therein.

There is no uniform identification number of a legal act in Russia, so we use the official publication number instead. Since not every act features this number, there might be duplicates.

Only first versions of acts (as were initially signed by relevant body) are taken. The corpus does not include consolidated (with further amendments) texts actual to the present date. It could only happen if the initial publications (pre-1990) already included amendments.

## Applications
We have published a policy memo “The Complexity of Legal Acts in Russia. Lexical and Syntactic Quality of Texts" (In Russian)

Using the methods of computational linguistics we have analyzed the dynamics of changes in the lexical and syntactic quality of texts of legal acts. It was concluded that in Russia there is a deterioration in the quality of texts of federal and regional legal acts for perception - a drop in lexical diversity, a complication in the structure of sentences. In recent years, this trend has intensified. It is noted that the most complex constructions of sentences are found in the texts of the Constitutional Court of the Russian Federation, as well as the authorities associated with the financial and budgetary sphere of regulation. We compared it to a dynamics of a newspaper corpus metrics and concluded that the newspaper texts at the same time became simpler.
 
Full text of the memo in PDF format is available [here](http://enforce.spb.ru/images/analit_zapiski/memo_readability_2018_web.pdf)

## License
Russian law excludes texts of legal acts from copyright protection so they can be redistributed freely. Official publication metadata are subject to terms at the source site (both commercial and non-commercial use allowed providing attribution to the source at http://publication.pravo.gov.ru/od/).

Other materials of the project distributed under the Creative Commons Attribution-NonCommercial 4.0 International license.

## Contact
[Denis Savelev](http://enforce.spb.ru/about-us/team/6922-savelev-denis-aleksandrovich) ([@denissaveliev](https://github.com/denissaveliev)) at the Institute for the Rule of Law (IRL) at the European University at Saint-Petersburg (EUSPb) 
