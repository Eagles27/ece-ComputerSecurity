# Report LAB3

## Anatomy of Malware

## Malware n°1

### a) What is the md5sum? What of interest does VirusTotal Report?

- <u>**md5sum:**</u> 4280aac55c1d3c327a6c00f0f0085677
- The interest is that the file has been flagged as a trojan 57 security vendors

### b) When was the malware compiled?

- 2009-05-14 17:12:41 UTC

### c) List a few imports or sets of imports and describe how the malware might use them

- SHELL32.dll
  - Permission to use the shell of the system (open a file, create a file, etc.)
- KERNEL32.dll
  - Permission to use the kernel of the system (create a thread, create a process, etc.)
- MSVCRT.dll
  - Permission to use the C runtime library of the system (printf, scanf, etc.)
- WS2_32.dll
  - Permission to use the Winsock library of the system (socket, connect, etc.)
  - Used to connect to a remote server
- USER32.dll
  - Permission to use the user32 library of the system (MessageBox, etc.)
  - Used to display a message box

### d) What are a few strings that stick out to you and why? (Use the strings command)

- Get environment variable
  - Get the environment variable of the system
- Set Thread Priority
  - Set the priority of the thread
- Send to server
  - Send data to a remote server : `http://www.ueopen/test.html`

### e) Are there any indications that this malware is packed? What are they? What is it packed with?

- The main indication to know if the malware is packed is the difference between the size of the raw data and virtual size.

### f) What do you think is the purpose of this malware?

- The purpose of this malware is to drop system files and send data to a remote server

---

## Malware n°2

### a) What is the md5sum? What of interest does VirusTotal Report?

- <u>**md5sum:**</u> :02658bc9801f98dfdf167accf57f6a36
- The interest is that the file has been flagged as a trojan 52 security vendors

### b) When was the malware compiled?

- 2008-09-16 08:40:04 UTC

### c) List a few imports or sets of imports and describe how the malware might use them

- KERNEL32.dll
  - Permission to use the kernel of the system (create a thread, create a process, etc.)
- MSVCRT.dll
  - Permission to use the C runtime library of the system (printf, scanf, etc.)
- WININET.dll
  - Permission to use the Wininet library of the system (InternetOpen, InternetConnect, etc.)
  - Used to connect to a remote server

### d) What are a few strings that stick out to you and why? (Use the strings command)

- Get environment variable
  - Get the environment variable of the system
- Set Thread Priority
  - Set the priority of the thread
- Send to server
  - Send data to a remote server : `http://www.ueopen/test.html`

### e) Are there any indications that this malware is packed? What are they? What is it packed with?

- The main indication to know if the malware is packed is the difference between the size of the raw data and virtual size.

### f) What do you think is the purpose of this malware?

- The purpose of this malware is to send data to a remote server
