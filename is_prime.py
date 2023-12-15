# checking for prime numbers
def is_prime(num):
  for i in range(2,num):
    if (num%i) == 0:
      print(f'{num} is prime')
    else:
        print(f'{num} is not prime')
is_prime(4)