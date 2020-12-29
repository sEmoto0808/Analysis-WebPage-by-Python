import requests
from bs4 import BeautifulSoup

with open('sample.csv','w') as f:
    result = requests.get('https://newspicks.com/')
    data_1 = BeautifulSoup(result.text, 'html.parser')
    data_2 = data_1.find_all("div", class_="title _ellipsis")

    for item in data_2:
        f.write('{0}\n'.format(item.getText()))
        print(item.getText())
