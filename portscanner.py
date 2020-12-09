""" Port Scanner

Programmer: Reece Jones
Date: December, 2020

This script is designed to scan ports on a user-entered IP address.  This scan implements multithreading so that
the scans will run quicker.

"""

import socket
import threading
import concurrent.futures

print("""\
===========================================================


   ___           _     __                                 
  / _ \___  _ __| |_  / _\ ___ __ _ _ __  _ __   ___ _ __ 
 / /_)/ _ \| '__| __| \ \ / __/ _` | '_ \| '_ \ / _ \ '__|
/ ___/ (_) | |  | |_  _\ \ (_| (_| | | | | | | |  __/ |   
\/    \___/|_|   \__| \__/\___\__,_|_| |_|_| |_|\___|_|   
                                                          

                                                            
===========================================================
                    """)

print_lock = threading.Lock()

ip = input("Enter the IP address you want to scan: ")

def scan(ip ,port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(f"[{port}] Opened")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1023):
        executor.submit(scan, ip, port + 1)