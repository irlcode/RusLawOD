# `RusLawOD`: Russian Law Open Data
‘RusLawOD’ is a corpus of texts of Russian Federation legal acts and their metadata covering 1991 to 2023. The corpus collects all 281,413 texts (176,523,268 tokens) of laws, non-secret federal regulations and acts, along with their metadata.

`Version 2`

## Scientific references

If you use this corpus in your scientific work, please refer to: Saveliev D., Kuchakov R. The Russian Legislative Corpus //arXiv preprint [arXiv:2406.04855](https://arxiv.org/abs/2406.04855). – 2024. See more works of authors below.

## State of affairs
Russian legislation were published in official paper journals since 1990. Since 1990 legal normative acts cannot enter into force without official publication. Some effort to make electronic databases of legal acts was made in the 1980s.  In the early 1990s commercial information companies created proprietary databases of legislation and court decisions. Starting from 2011 legal acts are supposed to be officially published at the Official Internet portal of legal information ([pravo.gov.ru](http://pravo.gov.ru)). Now it includes both federal, regional, and municipal legislation, but the information is not complete. However, such documents are only in graphical format (scanned TIFF or PDF without a text layer). We use the most convenient source that my be considered as the most authoritative as we can get: "IPS Zakonodatelstvo RF" (Information Legal System "The legislation of Russian Federation" that is a part of pravo.gov.ru portal, but is not considered as official publication (i.e. the date of the publication in this source may not be considered as the date of official publication and the text is not as equal in legal status as a text with signature).

## This corpus
This corpus (as of version `2`) includes XML files representing laws of Russian Federation, decrees by the President of RF, regulations by the government published as of December, 31, 2023. XML files feature legal metadata extracted from various sources and the respective texts.

The source of texts and metadata is the Information legal system "The legislation of Russian Federation" (IPS Zakonodatelstvo RF) [pravo.gov.ru](http://pravo.gov.ru)). This dabase is state-owned, though not considered to be official publication: it is a plaintext representation of official journals wherein the legislation was published. 

## Schema development
Data should be supplied in a format that is convenient and compatible. We rely on [Akoma Ntoso](http://www.akomantoso.org/). However, so far our corpus is not entirely compatible with it: we do not mark-up the internal document structure yet.

## XML structure
XML structure is reported in the below example with comments. All fields are not mandatory and are present in a document only if the information exists.

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
      <doc_typeIPS val="Document type as was in the source"/>
      <doc_author_normal_formIPS val="State organ that adopted the act, in normal language form"/>
      <signedIPS val="______"/> <!-- Person name who signed this legal act as provided in the source -->
      <statusIPS val="Утратил силу"/> <!-- In force, Not in force, In force with amendments: Acting status at the date of scrapping and as it was provided by the source -->
      <actual_datetimeIPS val="1710792705.7460072"/> <!-- Date and time when this data was scrapped from the original website -->
      <actual_datetime_humanIPS val="Mon Mar 18 23:11:45 2024"/> <!-- Date and time when this data was scrapped from the original website, in human readable format -->
      <is_widely_used val="1"/></identification> <!-- 1 if yes, 0 if no: is the document normative and in wide use (see article preprint for the details) -->
    </identification>
    <references>
      <classifierByIPS val="000.000.000.000.000" /> <!-- classification code according to the IPS Zakonodatelstvo -->
    </references>
    <keywords>
      <keywordByIPS val="KEYWORD" /> 
    </keywords>
  </meta>
  <body>
    <textIPS><-- Text parsed from the IPS Zakonodatelstvo --> 
    <!-- It can include hyperlinks to other acts, mostly amendments,
    like this: --> text <ref>linked text</ref> text 
    </textIPS>
    <taggedTextIPS> <-- CONLL_U morphosyntactic tagged text, cleaned -->
    </taggedTextIPS> 
  </body>
</act>
```

## Limitations
This corpus does not represent the entirety of the legal acts but rather it represents the universe of documents published electronically in the source.

There is no uniform identification number of a legal act in Russia, the identification might be by three attributes combined: the official document number, the date of signature and the state organ that adopted the document. Pravo.gov.ru ND is an internal database ID it is not official and may change.

Only first versions of acts (as were initially signed by relevant body) are taken. The corpus does not include consolidated (with further amendments) texts actual to the present date. It could only happen if the initial publications (pre-1990) already included amendments.

## Applications
Several scientific works published using thos corpus.

Saveliev, D. (2018). On creating and using text of the Russian Federation corpus of legal acts acts as open dataset. Pravo. Zhurnal Vysshey shkoly ekonomiki (1), 26–44. DOI: 10.17323/2072-8166.2018.1.26.44 (in Russian). [link](https://law-journal.hse.ru/article/view/20373)

Kuchakov, R. and D. Saveliev (2018). The complexity of the Russian legislation from the lexical and syntactic
perspective (Slozhnost’ pravovyh aktov v Rossii: leksicheskoe i sintaksicheskoe kachestvo tekstov). Analytic report,
IRL European University. [link](https://enforce.spb.ru/images/analit_zapiski/memo_readability_2018_
web.pdf) (in Russian).

Saveliev, D. (2020). Study of the complexity of sentences that make up the texts of legal acts of the authorities of the Russian Federation. Pravo. Zhurnal Vysshey shkoly ekonomiki (1), 50-74. DOI: 10.17323/2072-8166.2020.1.50.74 (in Russian).[link](https://law-journal.hse.ru/article/view/20098)

Kuchakov, R. K., & Saveliev, D. (2025). The complexity of the Russian legislation from the lexical and syntactic perspective, 1991–2023. [Vestnik of Saint Petersburg University. Law, 16(3), 796–823.]( https://lawjournal.spbu.ru/article/view/18768)


## License
Russian law excludes texts of legal acts from copyright protection so they can be redistributed freely. Official publication metadata are subject to terms at the [source site](http://publication.pravo.gov.ru/od/) (both commercial and non-commercial use allowed providing attribution to the source).

Other materials of the project distributed under the Creative Commons Attribution-NonCommercial 4.0 International license.

## Acknowledgements

The corpus is published as a part of scientific project No 17-18-01618 funded by Russian Science Foundation.

## Contact
[Denis Savelev](http://enforce.spb.ru/about-us/team/6922-savelev-denis-aleksandrovich) ([@denissaveliev](https://github.com/denissaveliev)) at the Institute for the Rule of Law (IRL) at the European University at Saint Petersburg (EUSPb) 
