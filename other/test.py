# import requests
# from bs4 import BeautifulSoup
# import collections

# r = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html').content.decode()
# content = BeautifulSoup(r, 'html.parser')
# c = collections.Counter([x.text for x in content.find_all(name='code')])
# print(c)

# r = requests.get('https://stepik.org/media/attachments/lesson/209723/5.html').content.decode()
# content = BeautifulSoup(r,'html.parser')
# sum=0
# for e in content.find_all(name='td'):
#     sum+=int(e.text)
# print(sum)


# import re
# a=input()
# b=input()
# c=''
# for i in range(0,len(a)):
#     if a[i:i+len(b)] == b:
#         c+=str(i)+ ' '
# # for i in re.finditer(b,a):
# #     c+=str(i.span()[0])+' '
# if len(c)>0:
#     print(c[:-1])
# else:
#     print('-1')

# rome = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
#
# a = int(input())
# for i in rome:
#     while a - i >= 0:
#         print(rome[i],end='')
#         a -= i

# n = int(input())
# print(n, end=' ')
# while n != 1:
#     if n % 2 == 0:
#         n = int(n/2)
#         print(n, end=' ')
#     else:
#         n = n*3 + 1
#         print(n, end=' ')

# n = int(input())
# pl = list(input().strip())
# alf = " abcdefghijklmnopqrstuvwxyz"
# for i in range(len(pl)):
#     index = alf.find(pl[i])
#     if index + n >= len(alf):
#         while index + n >= len(alf):
#             index -= len(alf)
#         pl[i] = alf[index+n]
#     elif index + n < 0:
#         while index + n < 0:
#             index += len(alf)
#         pl[i] = alf[index+n]
#     else:
#         pl[i] = alf[index + n]
# a = ''.join(pl)
# print(f'Result: \"{a}\"')

# import collections
# l = input().split()
# c = collections.Counter(l)
# print('{0:.2f}'.format(c['A']/len(l)))



# import xml
#
# fin = open('map2.osm', 'r', encoding='utf8')
# xml = fin.read()
# fin.close()
#
# parsedxml = xmltodict.parse(xml)
# c=0
# for el in parsedxml['osm']['node']:
#     # if el.get('@v') == 'fuel':
#     #     c+=1
#     #     continue
#
#     if el.get('tag'):
#         if isinstance(el.get('tag'),list):
#             for i in el.get('tag'):
#                 if i['@k'] == 'amenity' and i['@v'] == 'fuel':
#                     c+=1
#         # elif isinstance(el.get('tag'),dict):
#         #     if i['@v'] == 'fuel':
#         #         c += 1
#         else:
#             # print(el)
#             if el.get('tag')['@v'] == 'fuel':
#                 c += 1
# print(c)


# from bs4 import BeautifulSoup
#
# with open('map2.osm','r', encoding='utf8') as f:
#     xml = f.read()
#     bs_xml = BeautifulSoup(xml,'lxml')
#     print(len(bs_xml.find_all('tag',attrs={'v':'fuel'})))
#     # print(bs_xml.find_all('tag'))

# from collections import Counter
# line = Counter(input().split())
# for i in line:
#     if line[i] > 1:
#         print(i, end=' ')
# print(line)



# znach = {'6':1, '7':2, '8':3, '9':4, '10':5, 'J':6, 'Q':7, 'K':8, 'A':9}
# card_1, card_2 = input().split()
# koz = input()
# if card_1[-1] == koz and card_2[-1] != koz:
#     print('First')
# elif card_1[-1] != koz and card_2[-1] == koz:
#     print('Second')
# elif card_1[-1] == card_2[-1]:
#     if znach[card_1[:-1]] > znach[card_2[:-1]]:
#         print('First')
#     elif znach[card_1[:-1]] < znach[card_2[:-1]]:
#         print('Second')
#     else:
#         print('Error')
# else:
#     print('Error')


# def modify_list(l):
#     new=[]
#     for n in l:
#         if n%2 == 0:
#             new.append(n//2)
#     l[:]=new
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)

# from collections import Counter
# c = Counter(input().lower().split())
# for s,i in c.items():
#     print(s,i)


nums = [int(i) for i in input().split()]
f = int(input())
pl = []
for i,n in enumerate(nums):
    if n==f:
        pl.append(i)
if len(pl)>0:
    print(*pl)
else:
    print('None')




















