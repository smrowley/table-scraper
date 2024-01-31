#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

baseUrl = 'http://homesandmore.com/report1.php?type='


#class Row:
#
#class Table:
#    def __init__(self, headers, rows):
#        self.headers = headers
#        self.rows = rows
#
#    def getRow


def loadTable(name):
    response = requests.get(baseUrl + name)
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