start = int(input("enter the start of the range"))
end = int(input("enter the end of the range"))

print(f"Prime number between {start} to {end} are: ")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
                print(num)




