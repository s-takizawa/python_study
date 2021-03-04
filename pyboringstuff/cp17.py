import subprocess
import time
import datetime
import threading

print('start')

# time
now = time.time()
print(time.ctime(now))

time.sleep(1)
now = time.time()
print(time.ctime(now))

print('-------------')
# datetime
now_dt = datetime.datetime.now()
print(now_dt)
print(datetime.datetime.fromtimestamp(time.time()))

dt = datetime.datetime(2019, 9, 27, 13, 30, 2)
print(dt)
print('year:' + str(dt.year) + ' month:' + str(dt.month))

print('-------------')
# strftime: datetime.datetime => str
dt = datetime.datetime.now()
dt_str = dt.strftime('%Y/%m/%d %H:%M:%S')
print(type(dt_str))
print(dt_str)
dt_str = dt.strftime('%Y/%m/%d %p %I:%M')
print(dt_str)

print('-------------')
# strptime: str => datetime.datetime
str_dt = '2019/05/16 16:02:30'
dt = datetime.datetime.strptime(str_dt, '%Y/%m/%d %H:%M:%S')
# これはエラーになる[ValueError]
#dt = datetime.datetime.strptime(str_dt, '%Y/%m/%d')
print(type(dt))
print(dt)


print('-------------')
# thread

print('start prog')


def take_anap():
    time.sleep(1)
    print('wake up!')


t_obj_1 = threading.Thread(target=take_anap)
t_obj_1.start()

print('end prog')

t_obj_2 = threading.Thread(
    target=print, args=['Cats', 'Dogs'], kwargs={'sep': '&'})
t_obj_2.start()


print('-------------')
# subprocess
with open(r'input_data\py17.txt', 'w', newline='') as f:
    f.write('hello,world!')

proc = subprocess.Popen(['start', r'input_data\py17.txt'], shell=True)
print('pid:' + str(proc.pid))
time.sleep(3)
proc.terminate()

print('end')
