                #1
#a=[1,1,2,3,5,8,13,21,34,55,89]
#b=[]
#for elem in a:
#    if elem<5:
#        b.append(elem)
#print(b)

                #2
#a=[1,1,2,3,4,8,13,21,34,55,89]
#b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
#c=[]
#for ia in a:
#    if ia in b:
#        c.append(ia)
#print(c)

                #3
#import operator
#d={1:2,3:4,4:3,2:1,0:0}
#result=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
#print(result)

                #4
#dict_a={1:10,2:20}
#dict_b={3:30,4:40}
#dict_c={5:50,6:60}
#result={}
#for d in (dict_a,dict_b,dict_c):
#    result.update(d)
#print(result)

                #5
#my_dict={'a':500,'b':5874,'c':560,'d':400,'e':5874,'f':20}
#result=list(sorted(my_dict,key=my_dict.get,reverse=True))[:3]
#print(result)

                #6
#def intr(a,s):
#    print(int(a,s))

                #
#n=input('vvod: ')
#print(int(n)+int(n*2)+int(n*3))

