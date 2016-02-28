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
    
    name = config['name']
    platform_IP = config['platform_IP']
    platform_port = config['platform_port']
    
    print 'name: ' + name + ' platform_IP: ' + platform_IP + ' platform_port: ' + platform_port
    
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            print 'HB socket create failed. Bye Bye.'
            return
    
        print 'HB socket created.' 
        print 'HB waiting for platform connect...'
        
        s.connect((platform_IP , int(platform_port)))
        
        print 'HB platform connected.' 
        
        message = '{"name": "' + name + '"}'
        print 'HB message: ' + message
        
        while True:
            print 'about to send heart-beat '
            try:
                s.sendall(message)
            except Exception:
                print 'platform unreachable'
                break
                
            sleep(1)

def start_HB(config):
    print 'starting heart-beat'
    HB_thread = Thread(target = HB_worker, args=[config])
    HB_thread.start()
    return HB_thread

def stop_HB():
    pass