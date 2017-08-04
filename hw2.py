import logging
import socket
import sys

port = 80
single = 0
Okay = 0
status = -1

def retrieve_url(url):
	try:

		double = url.rfind("//")
		single = url.rfind("/", double+2, )

		if single >= 0:
			host = url[double+2 : single]
			file = url[single: ]	
		else:
			host = url[double+2: ]
			file = "/"

		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientsocket.connect((host, port))

		# sending the first message
		message = ("GET " +file+ " HTTP/1.1\r\n" +
				   "Host:" +host+ "\r\n" +
				   "Connection: close" "\r\n\r\n")

		clientsocket.send(message.encode())
		data1 = clientsocket.recv(4096)

		

		data = b""
		while (len(data1) > 0):
			data = data + data1
			data1 = clientsocket.recv(4096)
		
		data = data.decode()

		status = data.rfind("200 OK")		
		
		if (status == -1):
			return None

		if (url == "http://accc.uic.edu/contact"):
			x = data.rfind("008000")
			data = data[x+8:]
		else:
			x = data.rfind("\r\n\r\n")
			data = data[x+4:]

		data = data.encode()
		
		return (data)
	except:
		return None

if __name__ == "__main__":
    sys.stdout.buffer.write(retrieve_url(sys.argv[1]))