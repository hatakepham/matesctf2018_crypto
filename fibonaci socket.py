import socket

host = "125.235.240.167"
port = 12345

computed = {0:0,1:1}
result = 0

def recv():
	global s;
	recv=s.recv(1024).strip()
	if (recv==''):
		recv = s.recv(1024).strip()
	return recv

def send(mess):
	global s;
	s.send(str(mess)+'\n')

def greet():
	global s
	print recv();
	print recv();
	send(1);
	print recv();
	send(1);
	print recv();
	send(2);
	print recv();
	send(3);
	print recv();
	send(5);
	
def fibo(number):
	global computed
	if number<0: 
		n=-number;
	else:
		n=number
	if n not in computed:
		length = len(computed)
		for i in range (length,n+1):
			computed[i] = computed[i-2] + computed[i-1]

	return -computed[n] if (number<0 and number%2 == 0) else computed[n];

def fuckThis():
	global s
	global result
	n = recv()
	if (n=='Incorrect.'):
		print "Fail"
		print result
		return 0
	print n
	result = fibo(int(n))
	send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print "[+] Connected to bind shell!\n"
greet();
while 1:
	if (fuckThis() == 0): break;
