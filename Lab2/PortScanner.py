# %% [markdown]
# # Exercice 1

# %%
import socket
from colorama import Fore

# %%


# Define the port on which you want to connect
port = 5000

# Connect to my physical IP
IP = "127.0.0.1"

# %%


def PortScannerV1(port):
    # Create a socket object
    sock = socket.socket()
    if sock.connect_ex((IP, port)):
        print("Port is closed")
    else:
        print("Port is open")


# %%
PortScannerV1(port)

# %%


def PortScannerV2():
    # Create a socket object
    sock = socket.socket()
    for port in range(1, 5002):
        if sock.connect_ex((IP, port)):
            print(Fore.RED + "Port", port, "is closed")
        else:
            print(Fore.GREEN + "Port", port, "is open")


# %%
PortScannerV2()
