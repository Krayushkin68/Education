RC = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
      100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

CR = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
      'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}


def arab_to_rome(a):
    r = ''
    while a > 0:
        for i in sorted(list(RC.keys()), reverse=True):
            if a >= i:
                r += RC.get(i)
                a -= i
                break
    print(r)


def rome_to_arab(r):
    a = 0
    while len(r) > 1:
        if CR.get(r[0]) >= CR.get(r[1]):
            a += CR.get(r[0])
            r = r[1:]
        else:
            a += CR.get(r[:2])
            r = r[2:]
    if len(r) > 0:
        a += CR.get(r[0])
    print(a)


num = input('Enter number:\n')
if num.isdigit():
    arab_to_rome(int(num))
else:
    rome_to_arab(num)
