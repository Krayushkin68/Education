def MyMoney(start_sum,years,month_money,proc):
    money=start_sum
    for i in range(1,int(years)*12):
        money=money+month_money+(money+month_money)*(proc/1200)
    return int(money)
 
