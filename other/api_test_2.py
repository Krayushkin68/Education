from datetime import datetime
import requests
import json

credentials = {
    'client_id': 'Otisco_Mm_AP1',
    'client_secret': '8uvJ9qDePsZ8XPxA',
    'grant_type': 'password',
    'username': 'Otisco',
    'password': 'Portal2030$',
    'scope': 'minimax.si'}

headers = {'Content-type': 'application/x-www-form-urlencoded'}
req_token = requests.post(r'https://moj.minimax.hr/HR/AUT/OAuth20/Token', headers=headers, data=credentials)
if req_token.status_code == 200:
    req_token_data = json.loads(req_token.content)
    access_token = req_token_data['access_token']
    print(access_token)


headers = {'Authorization': f'Bearer {access_token}'}

r = requests.get(r'https://moj.minimax.hr/HR/API/api/currentuser/orgs', headers=headers)
print(r.content)

r = requests.get(r'https://moj.minimax.hr/HR/API/api/orgs/6004', headers=headers)
print(r.content)

params = {'DateFrom': datetime(year=2021, month=1, day=1)}
r = requests.get(r'https://moj.minimax.hr/HR/API/api/orgs/6004/journals', headers=headers, params=params)
print(r.content)
json.dump(json.loads(r.content), open(r'data\journal.json', 'wt', encoding='utf-8'), ensure_ascii=False)

# r = requests.get(r'https://moj.minimax.hr/HR/API/api/orgs/6004/journals/journal-entries', headers=headers)
# print(r.content)
# json.dump(json.loads(r.content), open(r'data\journal_entries.json', 'wt', encoding='utf-8'), ensure_ascii=False)