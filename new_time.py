import time

def data_time():
    seconds = time.time()
    local_time = time.ctime(seconds).split()
    return local_time[0], local_time[1], local_time[2]

def year():
    seconds = time.time()
    local_time = time.ctime(seconds).split()
    return local_time[4]





# print("Сейчас.")
# time.sleep(2.4)
# print("Через 2.4 секунды.")