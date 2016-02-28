import sys
import json

import HB
import server

HB_thread = None
server_thread = None

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
   
server_thread = server.start_server(config) 

HB_thread.join()
server_thread.join()




