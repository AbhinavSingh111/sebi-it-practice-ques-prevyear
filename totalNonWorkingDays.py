import calendar

def holi(date,holidays):
    mdays=0
    c=0
    cs=0
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    day,month,year = (int(i) for i in date.split(' '))
    daynum = calendar.weekday(year,month,day)
    name=days[daynum]
    leap=0
    if year%400 ==0:
        leap=1
    elif year%100 == 0:
        leap=1
    elif year%4==0:
        leap=1
    list = [1,3,5,7,8,10,12]
    if month in list:
        mdays =31
    elif month==2:
        mdays=28+leap
    else:
        mdays= 30

    for i in range(1,mdays+1):
        d =  calendar.weekday(year,month,i)
        if d == 5 or d==6:
            c+=1

    for i in range(len(holidays)):
        ds =  calendar.weekday(year,month,holidays[i])
        if ds == 5 or d==6:
            cs+=1
    count = len(holidays)+c-cs
    
    return(name,count)

date=input()
holidays=[int(i) for i in input().split(' ')]
print(holi(date,holidays))
