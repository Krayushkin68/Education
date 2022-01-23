import json


class PC:
    parts = {'Материнская плата': [], 'Процессор': [], 'Оперативаная память': [], 'Видеокарта': [],
             'Жесткий диск': [], 'SSD': [], 'Блок питания': [], 'Корпус': [], 'Кулер': [], 'Дополнительное': []}

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def enter_parts(self):
        print('Ввод комплектующих пк:\n')
        for i in self.parts.items():
            print(f'{i[0]}: ')
            col = input('   Количество: ')
            part = []
            try:
                if int(col) > 0:
                    for j in range(int(col)):
                        name = input('   Наименование: ')
                        cost = int(input('   Цена: '))
                        part.append([name, cost])
                    self.parts[i[0]] = part
            except Exception:
                print('Ошибка ввода!!!')

    def show(self):
        # print(f'\n{self.name}, состав:')
        sostav = f'\n{self.name}, состав:\n'
        for p in self.parts.items():
            if len(p[1]) > 0:
                # print(f'{p[0]}: ')
                sostav += f'{p[0]}: \n'
                for pp in p[1]:
                    # print(f'    {pp[0]}, {pp[1]}')
                    sostav += f'    {pp[0]}, {pp[1]}\n'
        print(sostav)

    def price(self):
        s = 0
        for p in self.parts.items():
            if len(p[1]) > 0:
                for pp in p[1]:
                    s += int(pp[1])
        print(f'\n{self.name}, цена: {s}')
        # return s

    def to_jsons(self):
        jsons = {'__PC__': True, 'Name': self.name, 'Parts': self.parts}
        return jsons

    def from_json(self, fname='pc.json'):
        with open(fname, 'rt', encoding='utf-8') as jpc:
            self.parts = json.load(jpc)


class PCEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, PC):
            return z.to_jsons()
        else:
            super().default(self, z)


def pc_to_json(pc, fname='pc.json'):
    with open(fname, 'wt', encoding='utf-8') as jpc:
        json.dump(pc, jpc, cls=PCEncoder)


def decode_pc(dct):
    if "__PC__" in dct:
        pc = PC(dct['Name'])
        pc.parts = dct['Parts']
        return pc
    return dct


def pc_from_json(fname='pc.json'):
    with open(fname, 'rt', encoding='utf-8') as jpc:
        data = jpc.read()
        pc = json.loads(data, object_hook=decode_pc)
    return pc


if __name__ == '__main__':
    print('Команды:\n'
          'pc = PC(<name>) - создать пк\n'
          'pc.enter_parts() - ввести комплектующие пк\n'
          'pc.show() - показать состав пк\n'
          'pc.price() - цена пк\n'
          'pc_from_json(<filename>) - загрузить пк из json\n'
          'pc_to_json(<pc>, <filename>) - сохранить пк в json\n')
    pcs = pc_from_json()
    # pcs[0].enter_parts()
    print(pcs)
    # pcs[0].price()
    # pc_to_json(pcs)
