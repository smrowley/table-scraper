#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from collections import defaultdict

baseUrl = 'http://www.homesandmore.com/report1.php?type='


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


_, employeeRows = loadTable('employee')
_, durationRows = loadTable('duration')
_, salaryByStateRows = loadTable('salarybystate')
_, salaryByDurationRows = loadTable('salarybyduration')

employees = {}
stateCounts = defaultdict(int)
durationCounts = defaultdict(int)

# create relevant employee info
for employee in employeeRows:
    employeeInfo = {}
    employeeInfo['state'] = employee[6]
    employees[employee[0]] = employeeInfo

    stateCounts[employee[6]] += 1

# add employee duration
for employee in durationRows:
    employees[employee[1]]['duration'] = employee[3]

    durationCounts[employee[3]] += 1

for empId in employees:
    employees[empId]['stateNeighbors'] = stateCounts[employees[empId]['state']]
    employees[empId]['durationNeighbors'] = durationCounts[employees[empId]['duration']]

    employee = employees[empId]

    if employee['stateNeighbors'] < 3 and employee['durationNeighbors'] < 3:
        print(empId + " --- ")
        print(employees[empId])
        print("#######")