def decorator(func_to_decorate):
    def decorated_func(arg):
        print('Code before func')
        func_to_decorate(arg)
        print('Code after func')
    return decorated_func


@decorator
def simple_func(name):
    print(f'Hello world, {name}')

# simple_func('ashley')






# Перестановки без повторений
l = [1,2,3,4,5,6,7,8,9]
comb = [l]
for i in range(len(l)):
    for j in range(len(l)):
        if i < j:
            tmp = l.copy()
            add = [l[i]]
            tmp = tmp[:i] + tmp[i+1:j+1] + add + tmp[j+1:]
            if tmp not in comb:
                comb.append(tmp)
        elif i > j:
            tmp = l.copy()
            add = [l[i]]
            tmp = tmp[:j]+add+tmp[j:i]+tmp[i+1:]
            if tmp not in comb:
                comb.append(tmp)

# print(comb)


def func(n):
    for i in range(n):
        a = i+n
        yield a

a = func(10)
print(list(a))

# for i in func(10):
#     print(i)
