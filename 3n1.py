print("A program to test the 3n + 1 math problem.")

n = int(input("Please, type an initial number: "))

counter = 1 #It starts in one because the initial number already counts

while True:
    if n % 2 == 0:
        n /= 2
        print("Even: ",end='')
    else:
        n = 3*n + 1
        print("Odd: ", end='')
    print(f'{n:.0f}')
    if n == 1:
        break
    counter += 1
print("=-"*15)
print(f"Times: {counter}")