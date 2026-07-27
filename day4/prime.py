def is_prime(number):
  """Return True if number is prime, otherwise False"""
  for i in range(2, number//2+1):
    if number % i == 0:
      return False
  return True

def print_next_prime(number):
  """Print the closest prime number"""
  index = number
  while True:
    index += 1
    if is_prime(index):
      print(index)
      return index

if __name__ == "__main__":
  n = int(input("Input number:"))
  print_next_prime(n)