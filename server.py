from threading import Thread
from time import sleep


def server_worker(config):
    while True:
        print 'server_worker'
        sleep(2)
        
def start_server(config):
    print 'starting server'
    global server_thread
    server_thread = Thread(target = server_worker, args=[config])
    server_thread.start()
    return server_thread

