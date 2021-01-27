
from tkinter import *
from months import *
from new_time import *
from timer import *

root = Tk()
root.title("Calender")
root.attributes('-alpha', 0.8)

w = root.winfo_screenwidth()  #высота и ширина экрана
h = root.winfo_screenheight() 
w = w//2 - 200 
h = h//2 -150

root.geometry('400x300+{}+{}'.format(w, h))

l1 = Label(text="пн", bg= '#800000', padx = 5, pady = 8, font = ('Verdana', '10'))
l2 = Label(text="вт", bg= '#D2691E', padx = 5, pady = 8, font = ('Verdana', '10'))
l3 = Label(text="ср", bg= '#FFD700', padx = 5, pady = 8, font = ('Verdana', '10'))
l4 = Label(text="чт", bg= '#008000', padx = 5, pady = 8, font = ('Verdana', '10'))
l5 = Label(text="пт", bg= '#1E90FF', padx = 5, pady = 8, font = ('Verdana', '10'))
l6 = Label(text="сб", bg= '#191970', padx = 5, pady = 8, font = ('Verdana', '10'))
l7 = Label(text="вс", bg= '#483D8B', padx = 5, pady = 8, font = ('Verdana', '10'))



l1.place(relx= .19, rely= .15)
l2.place(relx= .28, rely= .15)
l3.place(relx= .37, rely= .15)
l4.place(relx= .46, rely= .15)
l5.place(relx= .55, rely= .15)
l6.place(relx= .64, rely= .15)
l7.place(relx= .73, rely= .15)


dow, m, number = data_time()
start = search_today(dow, int(number))
drow(start, m, int(number))

year = year()
text_ = year +', ' + m
year_label = Label(text=text_, padx = 5, pady = 8, font = ('Verdana', '15'))
year_label.place(relx= .0, rely= .0)

thread_()
root.mainloop()
