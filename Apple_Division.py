print("Apple Division Task")
n = int(input("Enter the Number of Apples Available : "))
mx = int(input("Enter the Maximum number of Students : "))
mn = int(input("Enter the Minimum number of Students : "))
i = 0
j = 0
if mx - mn > 0:
    for x in range(mn, mx + 1):
        if n % x == 0:
            print(f"{n} Apples are divided by {x}")
            i += 1

        else:
            print(f"{n} Apples are not divided by {x}")
            j += 1

    print(f"\nNumber of times apples are divided {i}")
    print(f"Number of times apples arn't  divided {j}")

elif mx == mn:
    if n % mx == 0:
        print(f"{n} Apples are divided by {mx}")
        i += 1

    else:
        print(f"{n} Apples are not divided by {mx}")
        j += 1

    print(f"\nNumber of times apples are divided {i}")
    print(f"Number of times apples arn't  divided {j}")

else:
    print("Invalid Data")
    exit()

