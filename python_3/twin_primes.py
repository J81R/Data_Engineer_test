
from timer import timer_ms

def is_prime(num):
   if num == 1:
      return False

   for i in range(2, int(num**0.5)+1):
      if num % i == 0:
         return False
   return True

@timer_ms
def twin_prime_numbers(num_list):
    prime_nums = [num for num in num_list if is_prime(num)]
    prime_nums.sort()
    return [(prime_nums[i],prime_nums[i+1]) for i in range(len(prime_nums)-1) if prime_nums[i] +2 == prime_nums[i+1]]


