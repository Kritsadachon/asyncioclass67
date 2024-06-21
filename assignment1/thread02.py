# running a function with arguments in another thread
from time import sleep, ctime 
from threading import Thread

def task(sleep_time, message):
    #block for a moment
    sleep(sleep_time)
    #then display msg
    print(f'{ctime()} {message}')

thread = Thread(target=task, args=(1.5, 'Hello Kub'))
#run thread
thread.start()
print(f'{ctime()} Waiting for the thread...')
thread.join()