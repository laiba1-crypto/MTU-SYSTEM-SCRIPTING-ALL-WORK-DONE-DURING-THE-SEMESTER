def converge(n):
    if n == 1:
        return n
    elif n % 2 == 0:
        print(n)
        return converge(n // 2)
    else:
        print(n)
        return converge(3 * n + 1)

while True:
    try:
        n = int(input("Enter an integer number: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

converge(n)