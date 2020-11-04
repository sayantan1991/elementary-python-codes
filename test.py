def Divisors(n):
    s = 0
    i = 1
    while i < n:
        if (n % i == 0):
            s = s + i
            print(i)
        i = i + 1
    return s


m = int(input(' enter a number'))

sum = Divisors(m)
if (sum == m):
   print(f'sum of the divisor of {m} is the number {m} itself')
print (sum)

