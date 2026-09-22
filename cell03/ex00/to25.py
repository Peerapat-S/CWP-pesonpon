inp: int = int(input('Enter a number less than 25\n'))

if inp >= 26:
    print(f"error: {inp} is not less than 25")
else:
    for i in range(inp, 26):
        print(f"Inside the loop, my variable is {i}")