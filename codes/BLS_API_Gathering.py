import requests
import json
import prettytable
import pandas as pd

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['CEU0800000003'],"startyear":"2018", "endyear":"2022"})
url1 = 'https://api.bls.gov/publicAPI/v1/timeseries/data/CEU0800000003' # using the employment series
p1 = requests.post(url1, data=data, headers=headers)
json_data = json.loads(p1.text)

for series in json_data['Results']['series']:
    x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']
        footnotes=""
        for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ','
    
        if 'M01' <= period <= 'M12':
            x.add_row([seriesId,year,period,value,footnotes[0:-1]])
    output = open(seriesId + '.txt','w')
    output.write (x.get_string())
    output.close()

data = requests.get(url1).json()
print('Status: ' + data['status'])
print(p1.content)