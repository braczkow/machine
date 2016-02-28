from threading import Thread
from time import sleep
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])


def machine_worker(config):
    print 'machine_worker'
    machine_IP = get_ip_address('eth0')
    machine_port = 8888
    
    print 'machine_IP: ' + machine_IP
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((machine_IP, machine_port))
    sock.listen(1)
    
    while True:
        print 'wait for platform connection'
        connection, client_address = sock.accept()
        print 'accepted from: ' + str(client_address)
        msg = connection.recv(256)
        print 'msg: ' + msg
        
        sleep(2)
        
def start_machine(config):
    print 'starting machine'
    global machine_thread
    machine_thread = Thread(target = machine_worker, args=[config])
    machine_thread.start()
    return machine_thread

