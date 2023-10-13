# Neon Number Program -- sum of digits of  square of a number is equal to that number (check from 0 to 100) 
def is_neon_number(number):
    sq = number ** 2
    sum_d = 0
    while sq != 0:
        sum_d = sum_d + sq % 10
        sq = sq // 10  # Use // for integer division
    return sum_d == number

print("Neon Numbers from 0 to 100:")
for i in range(101):
    if is_neon_number(i):
        print(i)
