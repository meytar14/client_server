# import section
import socket
import time

# open UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# set the socket time out to be 1 sec
sock.settimeout(1)

#server's features
server_IP = "192.168.1.28"
server_port = 12000
server_addr = (server_IP, server_port)

# try to send a message
try:
    for i in range(1, 11):
        start = time.time()
        message = str(i) + " " + time.ctime(start)
        try:
            # using sendto func to send the wanted msg
            sent = sock.sendto(message.encode(), server_addr)
            # show that we sent the msg
            print("Sent " + message)
            # recive msg 
            data, server = sock.recvfrom(4096)
            # show the recived msg
            print("Received " + str(data))
            end = time.time();
            # calc the elapsed (rtt)
            rtt = end - start
            print("RTT: " + str(rtt) + " seconds\n")
        except socket.timeout:
            print("Request " + str(i) + " Timed out\n")

finally:
    # close the socket
    print("closing socket")
    sock.close()
