# LAB 4

## Authors

- **Student 1:** Romain DELAYRE
- **Student 2:** Maxime GILLEN

---

## Questions CTF 1

### 1. What is a .pcap file?

```
It's a data file which contain the data captured by a packet analyzer. In our case, it's Wireshark.
```

### 2. What does it contain?

```
It contains all the packets that have been captured by Wireshark.
```

### 3. Which IP address is the source?

```
The source IP address is ** 10.66.10.19 **
```

### 4. Which IP address is the destination?

```
The destination IP address is ** 10.66.10.27 **
```

### 5. What is the protocol used?

```
2 protocols are used : ** HTTP ** and ** TCP **
```

### 6. Which web browser sent the request?

```
The web browser that sent the request is ** Mozilla/5.0 **
```

### 7. What is the default language set in this browser?

```
The default language set in this browser is ** en-US ** but ** fr-FR **  is also accepted.
```

### 8. What are the 3 exchanges that precede this request?

```
The 3 exchanges that precede this request is called ** TCP Handshake ** or ** 3-way handshake **.
It's a process that allows to establish a connection between 2 hosts.

- SYN : The client send a SYN packet to the server to initiate the connection.
- SYN-ACK : The server send a SYN-ACK packet to the client to confirm the connection.
- ACK : The client send an ACK packet to the server to confirm the connection.

```

### 9. What is the frame number of the HTTP response?

```
We don't know what HTTP response we are looking for.
We used the more interesting HTTP response which is the frame number ** 44 **.

```

### 10. What does the answer contain?

```
The answer contains the ** zip file **
```

### 11. How could the IT department have prevented this data leak?

```
The IT department could have prevented this data leak by modifying the ** firewall rules ** .

```

### 12. Is HTTP a secure protocol? Why is it so? What is currently replacing it?

```
HTTP is not a secure protocol because it doesn't use encryption.
Currently, HTTPS is replacing HTTP because it uses encryption.

```

---

## Questions CTF 2

### 1. Date and time of the activity

```
Wed, 31 Oct 2018 15:33:12 GMT
```

### 2. The account name or username of the infected Windows computer

```
   User name: ichabod.crane
```

### 3. The host name of the infected Windows computer

```
Host Name: Headless-PC
```

### 4. The MAC address of the infected machine

```
Physical Address: 00-00-00-00-00-00-00-E0

```

### 5. The SHA256 hash of the malware file from the pcap

```
396223eeec49493a52dd9d8ba5348a332bf064483a358db79d8bb8d22e6eb62c
```

### 6. The type of infection

```
The type of infection is a trojan malware wich means that it's a type of malware that's hidden in files.

```
