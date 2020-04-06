import time
from datetime import datetime as dt

# path to access the hosts file on windows
# hosts_path = r'C;\Windows\System32\drivers\etc

# path to access the hosts file on linux
hosts_path = r'/etc/hosts'

#  website list to block the access to internet
website_list = ['www.facebook.com', 'facebook.com', 'www.instagram.com', 'instgram.com']

# time when the user is supposed to start working
start_time = dt(dt.now().year, dt.now().month, dt.now().day, 8)
# time when the user is supposed to finish working
finish_time = dt(dt.now().year, dt.now().month, dt.now().day, 16)
while True:
    if start_time > finish_time:
        print('Working hours...')
    else:
        print('Fun hours...')
    time.sleep(5)
