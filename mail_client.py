from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserv
mailserver = ("smtp.office365.com", 587)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)


recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after connection request:" + recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("Message after HeLO command:" + recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

clientSocket.send(('starttls\r\n').encode())
recv_tls = clientSocket.recv(1024)
print(recv_tls.decode())

#Info for username and password
username = "dhirtitapa.ray@sjsu.edu"
password = "******"
authMsg = "AUTH LOGIN\r\n"
clientSocket.send(authMsg.encode())
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())

clientSocket.send(username.encode())
clientSocket.send("\r\n".encode())
recv_user = clientSocket.recv(1024)
print("Response after sending username: "+recv_user.decode())

clientSocket.send(password.encode())
clientSocket.send("\r\n".encode())
recv_pass = clientSocket.recv(1024)
print("Response after sending password: "+recv_pass.decode())

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM:<dhirtitapa.ray@sjsu.edu>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: "+recv2)


# Send RCPT TO command and print server response. 
rcptTo = "RCPT TO:<risha.ray@outlook.com>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print("After RCPT TO command: "+recv3)

# Send DATA command and print server response. 
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print("After DATA command: "+recv4)

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body:"+recv_msg.decode())

# Send QUIT command and get server response.
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
clientSocket.close()

