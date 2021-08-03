
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("192.168.1.28", 12000)
sock.settimeout(1)

try:
    for i in range(1, 11):
        start = time.time()
        message = str(i) + " " + time.ctime(start)
        try:
            sent = sock.sendto(message.encode(), server_addr)
            print("Sent " + message)
            data, server = sock.recvfrom(4096)
            print("Received " + str(data))
            end = time.time();
            elapsed = end - start
            print("RTT: " + str(elapsed) + " seconds\n")
        except socket.timeout:
            print("#" + str(i) + " Requested Time out\n")

finally:
    print("closing socket")
    sock.close()