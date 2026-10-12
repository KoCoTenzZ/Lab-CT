print("hello, world")

def isPrime(n):
	if n <= 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

print("hello, world")
num_to_check = 7
if isPrime(num_to_check):
	print(f"{num_to_check} is a prime number.")
else:
	print(f"{num_to_check} is not a prime number.")