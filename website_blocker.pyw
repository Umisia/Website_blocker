import time
from datetime import datetime as dt

host_temp = r"C:\Users\Tugeza\Desktop\Python\WebsiteBlocker\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com", "facebook.com", "kwejk.pl", "www.kwejk.pl"]

while True:
    if  dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("WORK")
        with open(host_path, "r+") as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website+ "\n")

    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print("FUN")
    time.sleep(5)
