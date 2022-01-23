from random import randint

# task 1
mass = [randint(1, 10) for _ in range(20)]


def cycle_for(m):
    sum = 0
    for i in m:
        sum += i
    return sum


def cycle_while(m):
    sum = 0
    i = 0
    while i < len(m):
        sum += m[i]
        i += 1
    return sum


def recurs(m):
    if len(m) >= 1:
        return m[0] + recurs(m[1:])
    else:
        return 0


# print(cycle_for(mass))
# print(cycle_while(mass))
# print(recurs(mass))


# task 2
# [1,2,3] + [11,22,33] = [1,11,2,22,3,33]
def l_sum(a, b):
    res = []
    if len(a) > len(b):
        add = a[len(b):]
    else:
        add = b[len(a):]
    for i, j in zip(a, b):
        res.append(i)
        res.append(j)
    res.extend(add)
    return res


# print(l_sum([1,2,3],[11,22,33,44,55]))


# task 3

def fib(f, s, count):
    if count == 0:
        return 0
    print(f)
    fib(s, f + s, count - 1)


# fib(1,2,100)

# task 4

n = [61, 28, 9, 773, 7724]
cur_max = max(n)


def comparator(a, b):
    a = list(str(a))
    b = list(str(b))
    for i, j in zip(a, b):
        if i > j:
            return True
        elif i < j:
            return False


for _ in range(len(n) - 1):
    for i in range(len(n) - 1):
        if comparator(n[i + 1], n[i]):
            n[i], n[i + 1] = n[i + 1], n[i]

n = [str(i) for i in n]
# print(''.join(n))


# task 5

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def show_cmb(cmb):
    for i in cmb:
        print(i)


def repr(l):
    last = 0
    nums = []
    opers = []
    for i in range(len(l)):
        if l[i] in ['+', '-']:
            opers.append(l[i])
            num = l[last:i]
            num = [str(j) for j in num]
            nums.append(''.join(num))
            last = i + 1
        if i == len(l) - 1:
            num = l[last:]
            num = [str(j) for j in num]
            nums.append(''.join(num))
    rep = l_sum(nums, opers)
    print(''.join(rep))


def add_plus(m):
    cmb = []
    for i in range(1, len(m)):
        tmp = m.copy()
        tmp1 = m.copy()
        if tmp[i - 1] != '+' and tmp[i] != '+' and tmp[i - 1] != '-' and tmp[i] != '-':
            tmp.insert(i, '+')
            tmp1.insert(i, '-')
        if tmp not in cmb:
            cmb.append(tmp)
        if tmp1 not in cmb:
            cmb.append(tmp1)
    return cmb


def add_dop_plus(cmb):
    res_comb = []
    for i in cmb:
        new_cmb = add_plus(i)
        for j in new_cmb:
            if j not in res_comb:
                res_comb.append(j)
    return res_comb


def calculate(l):
    last = 0
    nums = []
    opers = []
    for i in range(len(l)):
        if l[i] in ['+', '-']:
            opers.append(l[i])
            num = l[last:i]
            num = [str(j) for j in num]
            nums.append(int(''.join(num)))
            last = i + 1
        if i == len(l) - 1:
            num = l[last:]
            num = [str(j) for j in num]
            nums.append(int(''.join(num)))
    res = nums[0]
    for i, n in enumerate(opers):
        if n == '-':
            res = res - nums[i + 1]
        elif n == '+':
            res = res + nums[i + 1]
    return res


f1 = add_plus(l)
f2 = add_dop_plus(f1)
f3 = add_dop_plus(f2)
f4 = add_dop_plus(f3)
f5 = add_dop_plus(f4)
f6 = add_dop_plus(f5)
f7 = add_dop_plus(f6)
f8 = add_dop_plus(f7)
# show_cmb(f8)

print(len(f8))
# Проверка
for i, el in enumerate(f8):
    if el in f8[:i] or el in f8[i + 1:]:
        print('error')

# Окончательный подсчет
for i in f8:
    if calculate(i) == 100:
        repr(i)
