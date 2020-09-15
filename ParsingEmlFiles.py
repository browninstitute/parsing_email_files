# Importing libraries
from glob import glob
from email import policy
from email.parser import BytesParser
import pdfkit
import pandas as pd
import numpy as np
from rake_nltk import Rake
from bs4 import BeautifulSoup
import subprocess
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

# Setting up input and output paths
print('Please provide the input directory (where the .eml files are located)')
print('Input directory: ', end='')
inputPath = input()
print('\n')
print('Please provide the output directory (where the .pdf, attachments and summary .csv will go')
print('Output directory: ', end='')
outputPath = input()
print('\n')

# Initializing the rake object
r = Rake() # Uses stopwords for english from NLTK, and all punctuation characters.

# Finding `.eml` files to process
files = glob(inputPath + '/*.eml')

# Creating the output dataframe object
df = pd.DataFrame(columns=['fileName','from','to','cc','subject','attachments','attachmentTypes','keywords_10', 'persons', 'orgs', 'nat_rel_polt', 'countries_cities_states', 'laws'])

# Setting up presets to process the emails
options = {
    'no-images': '',
    'enable-local-file-access': None
}

# Looping through the files
counter = 1
for file in files:
    fileName = file.split('/')[-1:][0].split('.')[0]
    print('Processing file:', fileName + '.eml')
    with open(file, 'rb') as msgfile:
        msg = BytesParser(policy=policy.default).parse(msgfile)
    try:        
        attachmentNames = []
        inlineAttachmentNames = []
        inlineContent = []
        attachmentTypes = []
        for part in msg.walk():
            if part.get_content_disposition() == 'attachment':
                attachmentNames.append(part.get_filename())
                attachmentTypes.append(part.get_filename().split('.')[-1:][0])
                attachmentFileName = outputPath + '/' + fileName + '_' + part.get_filename()
                f = open(attachmentFileName, 'wb')
                f.write(part.get_payload(decode=True))
                f.close()
                print('Attachment found: ', part.get_filename())
        to = msg['to']
        fromEmail = msg['from']
        cc = msg['cc']
        subject = msg['subject']
        header = '<div style="background:white;"><b>From</b>: ' + fromEmail + '<br>'
        header += '<b>To</b>: ' + to + '<br>'
        if cc != None:
            header += '<b>CC</b>: ' + cc + '<br>'
        header += '<b>Subject</b>: ' + subject + '<br>'
        if len(attachmentNames) > 0:
            header += '<b>Attachment file name(s)</b>: ' + ', '.join(attachmentNames) + '<br>'
        header += '<br><hr><br></div>'
        simplest = msg.get_body(preferencelist=('html', 'plain')).get_content()
        simplest = header + '\n' + simplest
        pdfkit.from_string(simplest, outputPath + '/' + fileName + '.pdf', options = options)
        try:
            plainText = msg.get_body(preferencelist=('plain')).get_content()
            r.extract_keywords_from_text(plainText)
            keywords = r.get_ranked_phrases()[:10]
            doc = nlp(plainText)
            persons = dict(Counter([x.text for x in doc.ents if x.label_ == 'PERSON']))
            orgs = dict(Counter([x.text for x in doc.ents if x.label_ == 'ORG']))
            norp = dict(Counter([x.text for x in doc.ents if x.label_ == 'NORP']))
            gpe = dict(Counter([x.text for x in doc.ents if x.label_ == 'GPE']))
            laws = dict(Counter([x.text for x in doc.ents if x.label_ == 'LAW']))
        except Exception as e:
            soup = BeautifulSoup(msg.get_body(preferencelist=('html')).get_content(), 'html.parser')
            for script in soup(["script", "style"]):
                script.extract() 
            plainText = soup.getText()
            r.extract_keywords_from_text(plainText)
            keywords = r.get_ranked_phrases()[:10]
            doc = nlp(plainText)
            persons = dict(Counter([x.text for x in doc.ents if x.label_ == 'PERSON']))
            orgs = dict(Counter([x.text for x in doc.ents if x.label_ == 'ORG']))
            norp = dict(Counter([x.text for x in doc.ents if x.label_ == 'NORP']))
            gpe = dict(Counter([x.text for x in doc.ents if x.label_ == 'GPE']))
            laws = dict(Counter([x.text for x in doc.ents if x.label_ == 'LAW']))
        df = df.append({'fileName':fileName+'.eml','from':fromEmail,'to':to,'cc':cc,'subject':subject,'attachments':attachmentNames,'attachmentTypes':attachmentTypes,'keywords_10':keywords,'persons':persons,'orgs':orgs,'nat_rel_polt':norp,'countries_cities_states':gpe,'laws':laws}, ignore_index=True)
        counter += 1
    except Exception as e:
        print(e)
    print('\n')

df.to_csv(outputPath + '/summaryFile.csv', index=False)
print('Done processing', counter, 'files...')
subprocess.call(["open", "-R", outputPath])
