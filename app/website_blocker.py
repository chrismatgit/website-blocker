import time
from datetime import datetime as dt

# path to access the hosts file on windows
# hosts_path = r'C;\Windows\System32\drivers\etc

# path to access the hosts file on linux
hosts_path = r'/etc/hosts'

# redirect at localhost
redirect = '127.0.0.1'

# temp host file path
hosts_temp = r'/media/root/5090E5C090E5ACA2/Users/CHRIS/Documents/ten project/website-blocker/app/hosts'

#  website list to block the access to internet
website_list = ['www.facebook.com', 'facebook.com', 'www.instagram.com', 'instgram.com']

# time when the user is supposed to start working
start_time = dt(dt.now().year,dt.now().month,dt.now().day,8)
# time when the user is supposed to finish working
finish_time = dt(dt.now().year,dt.now().month,dt.now().day,16)
while True:
    if start_time < dt.now() < finish_time:
        print('Working hours...')
        # access the content file
        with open(hosts_temp,'r+') as file: # 'r+' means read and append something in the file
            # read the content file
            content = file.read()
            for website in website_list:
                # checking if the website are in the host file
                if website in content:
                    pass
                else:
                    # write the websites in the host file
                    file.write('\n'+redirect+' '+website+'\n')
    else:
        # access the content file
        with open(hosts_temp,'r+') as file: # 'r+' means read and append something in the file
            # read the content of lines in within the file
            content = file.readlines()
            # seek() will put the cursor on the o position of the first line
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            # delete everthing that comes after the loop
            file.truncate()
        print('Fun hours...')
    time.sleep(5)
