import requests
import datetime
import json

dayOfMonth = datetime.date.today().strftime('%d')
url = f'https://adventofcode.com/2022/day/{int(dayOfMonth)}/input'

with open('cookies.json') as cookiesFile:
    cookies = json.load(cookiesFile)

response = requests.get(url= url, cookies= cookies)
if response.ok:
    with open(f'{dayOfMonth}/input.txt', 'wb') as file:
        file.write(response.content)
    
else:
    print(f'/response.status_code {response.status_code}: {response.content}')