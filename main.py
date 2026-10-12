def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def sortArray(arr):
    return sorted(arr)
def countPrime(numbers):
    return sum(1 for num in numbers if isPrime(num))


# Nhận một chuỗi các số nguyên từ người dùng, cách nhau bởi dấu cách
input_str = input("Enter a list of numbers separated by space: ")

# Tách chuỗi thành các chuỗi con và chuyển đổi chúng thành số nguyên
numbers = [int(num) for num in input_str.split()]
print("The list of numbers is:", numbers)
print("Sorted list:", sortArray(numbers))

# Đếm số lượng số nguyên tố
prime_count = countPrime(numbers)
print(f"Number of prime numbers: {prime_count}")

# Test the function on the first number of the list if it exists
if numbers:
    num_to_check = numbers[0]
    if isPrime(num_to_check):
        print(f"{num_to_check} is a prime number.")
    else:
        print(f"{num_to_check} is not a prime number.")
else:
    print("No numbers entered.")

