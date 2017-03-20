#Import modules configparser to include config.ini and psutil for gathering computer stats
import datetime
import time
import configparser
import schedule
import psutil

ini_file = configparser.ConfigParser()
#Config file
'''it looks like:
[common]
output = txt
interval = 5
'''
ini_file.read('config.ini')
output = ini_file.get('common', 'output')
interval = ini_file.get('common', 'interval')
#A variable which reflects the snapshot number
snap_id = 0

#A parent class which contains the computer indicators
class sysdata:
    def __init__(self):
        tm = time.time()
        self.cpu = ('Overall CPU load: '+str(psutil.cpu_percent(0, 0))+' %')
        self.vm = ('Overall VM usage: '+str((psutil.virtual_memory().used/1024/1024).__round__(2))+' MB')
        self.swap = ('Overall SWAP usage: '+str((psutil.swap_memory().used/1024/1024).__round__(2))+' MB')
        self.io_read = ('I/O info (READ FROM DISK): '+str((psutil.disk_io_counters()[3]/1024/1024).__round__(2))+' MB')
        self.io_write = ('I/O info (WRITTEN TO DISK): '+str((psutil.disk_io_counters()[4]/1024/1024).__round__(2))+' MB')
        self.net_s = ('Network info (SENT: '+str((psutil.net_io_counters(pernic=False)[0]/1024/1024).__round__(2))+' MB')
        self.net_r = ('Network info (RECEIVED): ' + str((psutil.net_io_counters(pernic=False)[1] / 1024 / 1024).__round__(2))+' MB')
        self.timestamp = datetime.datetime.fromtimestamp(tm).strftime('%Y-%m-%d %H:%M:%S')

#A child class which writes the stats to output file app.txt
class text (sysdata):

    def __init__(self):
        super().__init__()

    def sumup(self, filename = 'app.txt'):
# A variable which reflects the snapshot number
        global snap_id
        snap_id += 1
        f = open(filename, 'a+')
        f.write('SNAPSHOT {0}: {1}'.format(snap_id, self.timestamp))
        f.write('\n' + '===========================================================')
        f.write('\n' + self.cpu)
        f.write('\n' + self.vm)
        f.write('\n' + self.swap)
        f.write('\n' + self.io_read)
        f.write('\n' + self.io_write)
        f.write('\n' + self.net_s)
        f.write('\n' + self.net_r + '\n'+'\n')
        f.close()

def out():
    if output == 'txt':
        out_text = text()
        out_text.sumup()
    else:
        quit()

#A schedule will be performed accoring to the value in config file
schedule.every(int(interval)).minutes.do(out)

while True:
    schedule.run_pending()
