import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 53))

local_ip = s.getsockname()[0]

s.close()

print(local_ip)
print(socket.gethostbyname_ex(socket.gethostname())[2][-1])