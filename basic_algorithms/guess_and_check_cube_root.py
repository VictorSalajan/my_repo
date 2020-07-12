while True:
    try:
        cube = int(input("Enter an integer: "))
        guess = 0

        while guess ** 3 < abs(cube):
            guess += 1
        if guess ** 3 != abs(cube):
            print(cube, "is not a perfect cube")
            break
        else:
            if cube < 0:
                guess = -guess
            print("Cube root of", cube, "is:", guess)
            break       
    except ValueError:
        print("You have not entered an integer")
