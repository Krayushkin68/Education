import base64
import hashlib
from  cryptography import  fernet


class Case:
    def __init__(self):
        self.key = hashlib.sha3_256('qwe123'.encode()).digest()
        self.cipher = fernet.Fernet(key=base64.urlsafe_b64encode(self.key))
        self.case = []
        self.cur_usd = float()
        self.cur_eur = float()

    def save(self):
        rep = str()
        for i in self.case:
            rep += f'{i.save()}\n'
        rep += f'\nu\t{self.cur_usd}\n'
        rep += f'e\t{self.cur_eur}\n'
        cypher_text = self.cipher.encrypt(rep.encode())
        with open('инв.txt', 'wb') as f:
            f.write(cypher_text)

    def load(self):
        c.case.clear()
        with open('инв.txt', 'rb') as f:
            plain_text = self.cipher.decrypt(f.read())
            plain_text = str(plain_text, encoding='utf-8')
        for el in plain_text.splitlines():
            i = el.strip().split('\t')
            if len(i) == 3:
                tmpi = Invest(*i)
                self.case.append(tmpi)
            elif i[0] == 'e':
                self.cur_eur = float(i[1])
            elif i[0] == 'u':
                self.cur_usd = float(i[1])

    def __repr__(self):
        rep = str()
        for n, i in enumerate(self.case):
            rep += f'{n:<3} {i}\n'
        rep += f'\nusd {self.cur_usd}\n'
        rep += f'eur {self.cur_eur}\n'
        return rep


class Invest:
    def __init__(self, name, cost, change):
        self.name = name
        self.cost = float(cost)
        self.change = change

    def __repr__(self):
        rep = f'{self.name:<25} {round(self.cost):<10} {self.change}'
        return rep

    def save(self):
        rep = f'{self.name}\t{self.cost}\t{self.change}'
        return rep

    def sale(self, printer=True):
        if self.change[0] == '+':
            proc = float(self.change[1:])
            sum_proc = self.cost*0.003
            sum_nalog = self.cost*proc*0.01*0.13
            sum = self.cost - sum_proc - sum_nalog
            if printer:
                print(f'Продажа \'{self.name}\'  {self.cost}\nПолучишь: {sum}, проценты: {sum_proc}, налог: {sum_nalog}')
            return sum
        else:
            sum_proc = self.cost * 0.003
            sum = self.cost - sum_proc
            if printer:
                print(f'Продажа \'{self.name}\'  {self.cost}\nПолучишь: {sum}, проценты: {sum_proc}')
            return sum

    def sum_change(self, printer=True):
        proc = float(self.change[1:])
        sum = self.cost * proc * 0.01
        if self.change[0] == '+':
            if printer:
                print(f'Изменение цены \'{self.name}\': +{sum}')
            return sum
        else:
            if printer:
                print(f'Изменение цены \'{self.name}\': -{sum}')
            return -sum


if __name__ == '__main__':
    c = Case()
    c.load()
    print(c)
    # x = c.case[4].sale()
    # print(x*c.cur_eur)
    # c.case[7].sale()

    # a = Invest('Продать 3 и 4', c.case[4].sale(False)+c.case[3].sale(False), '+6')
    # a.sum_change()
    # loose = c.case[4].sum_change(False) + c.case[3].sum_change(False)
    # print(f'Потеря {loose}')

    # a = Invest('Вкинуть 400', 400000, '+6')
    # a.sum_change()
    # a.cost = a.cost + a.sum_change(False)
    # a.sale()

    sum = 0
    sum_ob = 0
    for i in range(0, len(c.case)):
        if i in [2,6]:
            sum += c.case[i].sum_change(False)*c.cur_usd
            sum_ob += c.case[i].sale(False) * c.cur_usd
        else:
            sum += c.case[i].sum_change(False)
            sum_ob += c.case[i].sale(False)
    print(sum, sum_ob)

    # print(sum(c.case[i].sale(False) for i in [9,10]))
