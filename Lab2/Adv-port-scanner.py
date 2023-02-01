#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import optparse
import threading


# # Question 4

# In[4]:


import optparse


def main():
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host", dest="host",
                      help="IP address of the host")
    parser.add_option("-p", "--port", dest="port",
                      help="Port number(s) to scan, separated by commas")

    (options, args) = parser.parse_args()

    if not options.host or not options.port:
        parser.print_help()
        exit(0)

    ports = options.port.split(",")

    for port in ports:
        portScan(options.host, port)


# # Question 4C

# In[5]:


def portScan(host, port):
    try:
        ip = socket.gethostbyname(host)
    except:
        print(f"Could not resolve {host}")
        return

    socket.setdefaulttimeout(1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    thread = threading.Thread(target=scan, args=(s, ip, port))
    thread.start()


def scan(s, ip, port):
    try:
        s.connect((ip, int(port)))
        print(f"Port {port} is open on {ip}")
    except socket.error:
        print(f"Port {port} is closed on {ip}")
    finally:
        s.close()


# # How to run the code :
#
# - python Adv-port-scanner.py -H 192.168.1.1 -p 80,443
#
# OR
#
# - python Adv-port-scanner.py -H 192.168.1.1 -p 80,443
