import time
from datetime import datetime as dt

hosts_temp ="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
#if you add r you'll assume that no break lines
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com", "dub119.mail.live.com", "www.dub119.mail.live.com"]



while True:
    #if dt(dt.now().year,dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day, 16)
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) <dt.now() < dt(dt.now().year, dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
                    #r+ allows you to read/write
            content=file.read()
            for website in website_list:
                if website in content:
                    pass #pass means that it's going to check for other lines
                else:
                    file.write(redirect+" " + website+"\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content=file.readlines()
                #checking items from the website list against host lists
            file.seek(0)
                    #seek shows which line you start on (base 0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() #removes everything after it
        print("Fun hours...")

    time.sleep(5)
