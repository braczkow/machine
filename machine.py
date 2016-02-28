import sys
import json

import HB
import machine_server

HB_thread = None
machine_thread = None

config_file_name = "./config.json"

config = None

try:
    config_file = open(config_file_name)
    config = json.load(config_file)
except:
    print 'Cannot read config.json. Bye bye.'
    sys.exit()
    
if 'name' not in config:
    print 'Name not set'
else:
    print 'config[ name ] = ' + config['name']
    HB_thread = HB.start_HB(config)
   
machine_thread = machine_server.start_machine(config) 

HB_thread.join()
machine_thread.join()




