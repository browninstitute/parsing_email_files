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
4. Install `Pandas`, `Numpy`, `NLTK`, `Rake_NLTK`, `Beautiful Soup`, and `pdfkit`:

```bash
pip3 install pandas
pip3 install numpy
pip3 install nltk
pip3 install rake-nltk
pip3 install bs4
pip3 install pdfkit
```

## Running the scripts

To run the scripts do: `python3 [script name]`

## Todo

* [ ] Add entity extraction