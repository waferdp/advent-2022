import requests
import datetime
import json

def saveTestInput(dayOfMonth):
    url = f'https://adventofcode.com/2022/day/{int(dayOfMonth)}'
    response = requests.get(url= url)
    if response.ok:
        html = response.content.decode("utf-8")
        start = html.find('<pre>')
        end = html.find('</pre>')
        code = html[(start+11):(end-7)]
        with open(f'{dayOfMonth}/test_input.txt', 'w') as file:
            file.write(code)
    else:
        print(f'{response.status_code}: {response.content}')

def saveInput(dayOfMonth):
    with open('cookies.json') as cookiesFile:
        cookies = json.load(cookiesFile)
    url = f'https://adventofcode.com/2022/day/{int(dayOfMonth)}/input'

    response = requests.get(url= url, cookies= cookies)
    if response.ok:
        with open(f'{dayOfMonth}/input.txt', 'wb') as file:
            file.write(response.content)
    else:
        print(f'{response.status_code}: {response.content}')



dayOfMonth = datetime.date.today().strftime('%d')
saveTestInput(dayOfMonth)
saveInput(dayOfMonth)