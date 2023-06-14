##largest polindrome

#include <stdio.h>

largest= 0

for i in range(900, 1000):
    for j in range(900, 1000):
        num = i * j
        if str(num) == str(num)[::-1]:
            if num > largest:
                largest= num

print(largest)