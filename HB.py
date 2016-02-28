from threading import Thread
from time import sleep

import socket


def HB_worker(config):
    if 'platform_IP' not in config:
        print 'platform_IP not defined'
        return
    if 'platform_port' not in config:
        print 'platform_port not defined'
        return
    if 'name' not in config:
        print 'name not defined'
        return
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        return

    print 'HB socket created'
    
    s.connect((config['platform_IP'] , int(config['platform_port']))) 
    
    message = '{"name": "{}"}'.format(config['name'])
    print 'HB message: ' + message
    
    while True:
        print 'HB_worker'
        s.sendall(message)
        sleep(10)

def start_HB(config):
    print 'starting heart-beat'
    HB_thread = Thread(target = HB_worker, args=[config])
    HB_thread.start()
    return HB_thread

def stop_HB():
    pass