import time 
inicio = time.time()
p = 1
a = 1
b = 1

for i in range(1, 100):
	p = i * p

for i in range(1, 1000):
	a = i * a

for i in range(1, 2000):
	b = i * b

fin = time.time()
print(fin-inicio)


