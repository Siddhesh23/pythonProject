import json

import requests

yearWiseDataList = []
percentRise = []
years = []
response_API = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
assert response_API.status_code == 200

data = response_API.text

populationData = json.loads(data)
numOfYears = (len(populationData['data']))
idNation = populationData['data'][0]['ID Nation']
nation = populationData['data'][0]['Nation']
for index in range(0, numOfYears):
    yearWiseDataList.append(populationData['data'][index]['Population'])
    years.append(populationData['data'][index]['Year'])
yearWiseDataList = yearWiseDataList[::-1]
years = years[::-1]

for index in range(1, len(yearWiseDataList)):
    rise = yearWiseDataList[index] - yearWiseDataList[index - 1]
    percentRise.append((rise * 100) / yearWiseDataList[index - 1])
print(percentRise)

print((percentRise.index(max(percentRise))) + 1)

maxRiseYear = years[(percentRise.index(max(percentRise))) + 1]
minRiseYear = years[(percentRise.index(min(percentRise))) + 1]
print('According to', idNation, 'in ', numOfYears, ' years from ', years[0], ' to', years[len(years) - 1],
      ' peak population was ', max(percentRise), '% in ', maxRiseYear, ' and lowest population increase was ',
      min(percentRise), '% in ', minRiseYear, '.')
