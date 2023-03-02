# Module 2 Challenge Loan Qualifier Application

This is a python command-line interface application that allows users to see qualifying loans from lenders quickly and easily. The application works by taking in a `daily_rate_sheet` of loan criteria from various loan providers, asking the user a number of questions to evaluate their loan eligibility, and then returning to them a list of qualifying loans. The challenge was essentially to create and save 'qualifying_loans.csv'.


--- 

## Technologies

This project uses Python 3.7 with packages installed
The packages installed and imported are 
[fire]
[questionary]

---

## Installation Guide

To install the packages listed above you would have to type in the following commands into your terminal/gitbash under python
''' Python
    pip install fire
    pip install questionary
'''

---

## Usage

to use the loan qualifier application clone this repository and run the 'app.py' with python
'''Python 
python app.py'''

The following imports were made to import the neccesary libraries and functions from other path files
![Imports for app.py](https://github.com/reiccv/Module_2_challenge/blob/main/images_for_readme/imports2.PNG)
---
Function to load bank data
![Function to load bank data](https://github.com/reiccv/Module_2_challenge/blob/main/images_for_readme/def_loadbank.PNG)

Function to get applicant info
![Function to get applicant info](https://github.com/reiccv/Module_2_challenge/blob/main/images_for_readme/def_getapp_info.PNG)

Function to find qualifying loans
![Function to find qualifying loans](https://github.com/reiccv/Module_2_challenge/blob/main/images_for_readme/def_qualifyingloans.PNG)

Function to save qualifying loans
![Function to save qualifying loans](https://github.com/reiccv/Module_2_challenge/blob/main/images_for_readme/def_save_loans.PNG)

Function to run the program
![Function to run the program](https://github.com/reiccv/Module_2_challenge/blob/main/images_for_readme/def_run.PNG)

Function to load the csv
![Function to load the csv](https://github.com/reiccv/Module_2_challenge/blob/main/images_for_readme/def_loadcsv.PNG)

Function to save csv
![Function to save csv](https://github.com/reiccv/Module_2_challenge/blob/main/images_for_readme/def_savecsv.PNG)
This code is able to create and save a csv file and allows the user to see how many loans they have qualified for.

An applicants saved csv file containing all of their qualified loans
![Saved csv](https://github.com/reiccv/Module_2_challenge/blob/main/images_for_readme/save_results.PNG)
## Contributors

No other contributors

---

## License

Public

