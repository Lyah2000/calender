import time
from tkinter import *
import threading

def Time_():
    seconds = time.time()
    new_time = time.ctime(seconds).split()[3]
    timer_Label = Label(text=new_time, padx = 5, pady = 8, font = ('Verdana', '15'))
    timer_Label.place(relx= .71, rely= .0)
    time.sleep(1)
    Time_()
    
def thread_():
    t = threading.Thread(target=Time_, daemon= True)
    t.start()
    
    #Time_()

