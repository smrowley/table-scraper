#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from collections import defaultdict

def loadTable(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')

    headers = []
    thead = table.find('thead')
    for th in thead.find_all('th'):
        headers.append(th.text.strip())

    rows = []
    tbody = table.find('tbody')
    for tr in tbody.find_all('tr'):
        row = [td.text.strip() for td in tr.find_all('td')]
        rows.append(row)

    return headers, rows




_, medicalRows = loadTable('http://www.mainstreethospital.com/medical.php')
_, medicalCodeRows = loadTable('http://www.coderepository.com/codes.php?type=cpt,icd')
_, claimsRows = loadTable('http://www.communalinsurance.com/insurance.php')
_, votersRows = loadTable('http://www.nationalvoterregistration.com/voter.php')

people = []

# brute force data joining, just a quick and dirty impl
for voter in votersRows:
    person = {}
    person['id'], person['first'], person['last'], person['dob'], person['dod'], person['gender'], person['zip'], person['ethnicity'], person['party'], person['registered'], person['last_voted'] = voter

    people.append(person)