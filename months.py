from tkinter import *
months = {'Jan' : 31,
          'Feb' : 28,
          'Mar' : 31,
          'Apr' : 30,
          'May' : 31,
          'Jun' : 30,
          'Jul' : 31,
          'Aug' : 31,
          'Sep' : 30,
          'Oct' : 31,
          'Nov' : 30,
          'Dec' : 31}

Day_of_week = {1 : ('Mon', 0.19, '#800000'),
               2 : ('Tue', 0.28, '#D2691E'),
               3 : ('Wed', 0.37, '#FFD700'),
               4 : ('Thu', 0.46, '#008000'),
               5 : ('Fri', 0.55, '#1E90FF'),
               6 : ('Sat', 0.64, '#191970'),
               7 : ('Sun', 0.73, '#483D8B')}


def search_today(day_of_week, day): # текущая дата

    for i in range(1, 8):
        if Day_of_week[i][0] == day_of_week:
            num_day = i

    k = (day % 7) - 1

    if k < num_day:
        start_mon = num_day - k
    elif k > num_day:
        start_mon = 7 - (k - num_day)
    elif k == 0:
        start_mon = num_day

    return start_mon


def drow(start_month, month, number):
    mas_day = [i for i in range(1, months[month] + 1)]

    num_day = start_month
    y = 0.28
    for day in mas_day:
        onex = 5
        if day // 10 == 0:
            onex = 9
            
        if day == number:
            l = Label(text=str(day), bg= Day_of_week[num_day][2], padx = onex, pady = 8, font = ('Verdana', '8'), bd= 3)
            l.place(relx= Day_of_week[num_day][1], rely= y)

        else:
            l = Label(text=str(day), bg= '#BC8F8F', padx = onex, pady = 8, font = ('Verdana', '8'), bd= 3)
            l.place(relx= Day_of_week[num_day][1], rely= y)
        
        num_day += 1

        if num_day == 8:
            num_day = 1
            y += 0.13


