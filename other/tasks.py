import math
def arithmetic(x,y,z):
    if z == '+':
        return x+y
    elif z == '--':
        return x-y
    elif z == '*':
        return x*y
    elif z == '/':
        return x/y
    else: return 'Unknown'
    

def is_year_leap(date):
    try:
        a = int(date[-4:])%4
    except Exception:
        return 'Invalid date'
    if a == 0:
        return 'This year is leap'
    else:
        return 'This year is not leap'

def square(x):
    a=(4*x, x*x, math.sqrt(2)*x,)
    return 'P={0[0]}, S={0[1]}, Diag={0[2]:.4}'.format(a)

def season(n):
    if n in (12,1,2):
        return 'winter'
    elif n in (3,4,5):
        return 'spring'
    elif n in (6,7,8):
        return 'summer'
    elif n in (9,10,11):
        return 'autumn'
    else: return 'Incorrect month number'

def bank(sum,year,pr):
    res=sum
    for i in range(1,int(year)+1):
        res=res+res*(pr/100)
        print('Summa posle {0} goda: {1}'.format(i,int(res)))
    return 

def is_prime(x):
    for i in range(2,int(x/2)+1):
        if x%i==0:
            return 'not prime {}'.format(i)
    return 'prime'

def date(d,m,g):
    if d >=1 and d<=31 and m in [1,3,5,7,8,10,12] and g>0:
        return 'right date'
    elif d >=1 and d<=30 and m in [4,6,9,11] and g>0:
        return 'right date'
    elif d >=1 and d<=29 and m == 2 and g%4==0:
        return 'right date'
    elif d >=1 and d<=28 and m == 2 and g%4!=0:
        return 'right date'
    else: return 'incorrect date'

def XOR_cipher(path,key):
    f=open(path,'rb')
    pl=f.read()
    pl=bytearray(pl)
    f.close()
    key=key.encode(encoding='utf-8')
    #b=bytearray(pl, encoding='utf-8')
    for i in range(0,len(pl)):
        pl[i]=pl[i]^key[0]
    f=open(path,'wb')
    f.write(pl)
    #cip=b.decode(encoding='utf-8')
    f.close()
    return
