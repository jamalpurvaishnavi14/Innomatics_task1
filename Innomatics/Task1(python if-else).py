n = int(input().strip())

if n%2 == 0:
    # If n is even and in the inclusive range of 2 to 5 
    if n in range(2,6):
        print("Not Weird")
    # If n is even and in the inclusive range of 6 to 20
    elif n in range(6,21):
        print("Weird")
    # If n is even and greater than 20
    elif n > 20:
        print("Not Weird")
# If n is odd
else:
    print("Weird")
