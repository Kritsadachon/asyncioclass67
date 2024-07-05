# running a function with arguments in another thread
<<<<<<< HEAD
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
=======
from time import sleep, ctime
from threading import Thread

# a custom function that blocks for a moment
def task(sleep_time, message):
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(f'{ctime()} {message}')

# create a thread
thread = Thread(target=task, args=(1.5, 'New message from another thread'))
# run the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()
>>>>>>> upstream/main
