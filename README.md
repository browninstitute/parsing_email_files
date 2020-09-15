# Python Scripts to Parse Email Files

This repository contains different Python scripts to parse email files. The scripts output single `pdf` files for each email file and attachment as well as a summary `csv` file with email details and keywords.

So far this repository includes scripts to parse:

* `.eml` files ([`ParsingEmlFiles.py`](https://github.com/browninstitute/parsing_email_files/blob/master/ParsingEmlFiles.py))

These scripts were created by Juan Francisco Saldarriaga at the [Brown Institute for Media Innovation](https://brown.columbia.edu/)

## Installation instructions

The scripts require `Python 3.x` and the following libraries:

* `Pandas`
* `Numpy`
* `NLTK`
* `Rake_NLTK`
* `Beautiful Soup`
* `pdfkit`

When working on MacOS we suggest you install the necessary packages through [Homebrew](https://brew.sh/):

1. Install Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
2. Install Python 3.x: `brew install python`
3. Install `wkhtmltopdf` (pre-requisite for `pdfkit`: `brew install Caskroom/cask/wkhtmltopdf`
4. Install `Pandas`, `Numpy`, `NLTK`, `Rake_NLTK`, `Beautiful Soup`, `pdfkit`:

```bash
pip3 install pandas
pip3 install numpy
pip3 install nltk
pip3 install rake-nltk
pip3 install bs4
pip3 install pdfkit
python3 -m spacy download en_core_web_sm
```

## Running the scripts

To run the scripts download the script files and do: `python3 <script name>`.

When prompted for the input and output paths, please type (or copy and paste) the full absolute path. Something like `/Users/juanfrans/Google Drive/08_Brown/00_TestingGroundMagicGrants/01_DocumentingCovid19/01_ParsingEmails/01_ParsingEML/input`.

Note that the input files must be unzipped.

The scripts will produce an output `pdf` file with the same file name as the original email file. In addition, it will also output the attachments with the name of the original email file pre-appended to their name.

The script will also produce a file called `summaryFile.csv` which contains the following fields:

* `fileName`: the name of the original email file
* `from`: the sender's email address
* `to`: the receiver's email address
* `cc`: any cc'd email address
* `subject`: the email subject
* `attachments`: the names of any attachment files in the email
* `attachmentTypes`: the types of attachments in the email
* `keywords_10`: the 10 most important keywords in the email, according to the [rake-nltk library](https://github.com/csurfer/rake-nltk)
* `persons`: a list of persons (and the number of times) mentioned in the email, based on [SpaCy](https://spacy.io/) named entity recognition model
* `orgs`: a list of organizations (and the number of times) mentioned in the email, based on [SpaCy](https://spacy.io/) named entity recognition model
* `nat_rel_polt`: a list of nationalities, religious or political groups (and the number of times) mentioned in the email, based on [SpaCy](https://spacy.io/) named entity recognition model
* `countries_cities_states`: a list of countries, cities or states (and the number of times) mentioned in the email, based on [SpaCy](https://spacy.io/) named entity recognition model
* `laws`: a list of laws (and the number of times) mentioned in the email, based on [SpaCy](https://spacy.io/) named entity recognition model

## Parsing `.pst` files

To parse `.pst` files, open Microsoft-Outlook and import them by selecting `File / Import / Outlook for Windows archive file (.pst)`. Once the messages are imported, select all the messages and drag them to a finder window on the folder where you wish to save the files. This should convert them to `.eml` files.
