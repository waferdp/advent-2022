import requests
import datetime
import json
import os

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


def createFolder(dayOfMonth):
    directory = os.path.join(os.getcwd(), dayOfMonth)
    if not os.path.exists(directory):
        print(f'{directory} does not exist, creating it...')
        os.mkdir(directory)
    else:
        print(f'{directory} already exists')

dayOfMonth = datetime.date.today().strftime('%d')
createFolder(dayOfMonth)
saveTestInput(dayOfMonth)
saveInput(dayOfMonth)