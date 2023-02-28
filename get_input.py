import requests
import datetime
import json
import os
import sys

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

def updateTestSettings(dayOfMonth):
    
    with open('./.vscode/settings.json', 'r') as file:
        settings = json.load(file)
    if f'./{dayOfMonth}' not in settings['python.testing.unittestArgs']:
        print('Adding todays folder to settings unittestArgs')
        settings['python.testing.unittestArgs'] = [
            "-v",
            "-s",
            f"./{dayOfMonth}",
            "-p",
            "test*.py"
        ]
        with open('./.vscode/settings.json', 'w') as file:
            json.dump(settings , file, indent=4)
    else:
        print('Todays folder already in settings unittestArgs')

args = sys.argv[1:]
if len(args) > 0:
    dayOfMonth = args[0]
else:
    dayOfMonth = datetime.date.today().strftime('%d')
createFolder(dayOfMonth)
saveTestInput(dayOfMonth)
saveInput(dayOfMonth)
updateTestSettings(dayOfMonth)