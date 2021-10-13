import requests

csv = 'john@doe.com,John,Doe,unknown'
csv = input('Enter test line in csv format:')

website = f"http://www.{csv.split(',')[0].split('@')[1]}"

headers = {'user-agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
r = requests.get(website, headers=headers)
if r.status_code == 200:
    print(f'Page {website} received')

keyword = input('Enter keyword: ')

if r.text.find(keyword) != -1:
    print('Yes')
else:
    print('No')

