# Created by Gtain(유재준), 2025-11-30
import socket
from datetime import datetime
import time
import os

if os.name == "nt":
    import msvcrt
    def user_input():
        return msvcrt.getch().decode("utf-8").upper()
else:
    def user_input():
        return input().upper()

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def log(a):
    with open("Port Check Result.txt", "a", encoding="utf-8") as f:
        f.write(a + "\n")

print("[Port Scanner v1.0]\nby Gtain")
print("-"*50)
target = input("Please enter any web address. >>>>")

clear_screen()
print(target)
print("-"*50)

while True:
    print("Enter Ports do you want.\nFor Example:25565 443 22 80\n-> Result will be 25565, 443, 22, 80.")
    port_to_scan = list(map(int, input("Ports >>>>").split()))
    print(f"You just entered {port_to_scan}.")
    print("Is it right?(Y/N)")
    val = user_input()

    if val == "Y":
        break
    
    else:
        clear_screen()
        print("Retrying...")
        time.sleep(0.7)
        clear_screen()
        print(target)
        pass

print("Scanning will be start soon...")

for i in range (5, 0, -1):
    time.sleep(1)
    print(i)

clear_screen()

try:
    target_ip = socket.gethostbyname(target)

    print("-"*50)
    print(f"Scanning Target: {target} ({target_ip})")
    print(f"Time started {datetime.now()}")
    print("-"*50)

    log(f"Scanning Target: {target} ({target_ip})")
    log(f"Time started {datetime.now()}\n")

    for port in port_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(0.5)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port{port}: OPEN")
            log(f"Port{port}: OPEN")
        else:
            print(f"Port{port}: CLOSED")
            log(f"Port{port}: CLOSED")

        s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
except socket.gaierror:
    print("Hostname couldn't be resolved.")
except socket.error:
    print("Couldn't connect to server.")

print("-"*50)
print("Scan Completed.")
input()
