import socket

host = "125.235.240.167"
port = 12345

compute = {0:0, 1:1}
resault = 0

def recv():
	global s
	# bien global
	recv=s.recv(1024).strip()
	if recv == '':
		recv = s.recv(1024).strip()
	return recv

	# nhan du lieu

def  send(mess):
	global s
	s.send(str(mess) + '\n')
	# gui du lieu

def greet():
	global s
	print recv()
	print recv()
	send(1)
	print recv()
	send(1)
	print recv()
	send(2)
	print recv()
	send(3)
	print recv()
	send(5)


def fibo(number):
	global compute
	# bien global
	if number < 0:
		n = -number
	else:
		n = number
	# ko thay doi gia tri number
	
	if  n not in compute:
		length = len(compute)
		for  i in range(length, n+1):
			compute[i] = compute[i-2] + compute[i-1]
	return -compute[n] if (number < 0 and (number % 2) == 0) else compute[n]

def flag():
	global s
	global resault
	n = recv()
	print n
	if n=='Incorrect.':
		print "fail"
		print resault
		return 0

	resault = fibo(int(n))
	send(resault)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

print " ket noi thanh cong"
greet()
while 1:
	if (flag())==0:
		break

