#range(start,stop,step)
#for i in range(1,51,1):
 # print(i)
for i in range(1, 51):
    if i % 15 == 0:
       print(f"{i}FizzBuzz")
    elif i % 5 == 0:
        print(f"{i}Buzz")
    elif i % 3 ==0:
        print(f"{i}Fizz")
    else:
        print(i)

