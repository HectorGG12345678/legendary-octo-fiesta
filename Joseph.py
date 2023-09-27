    # num1 = int(input('Enter the number 1 :'))
    # num2 = int(input('Enter the number 2: '))
    # num2 = int(input('Enter the number 3: '))
    num1 = 600
    num2 = 300
    num3 = 500

    if num1 < num2:
        if num1 < num3:
            minval = num1
        else:
            minval = num3
    else:
        if num2 < num3:
            minval = num2
        else:
            minval = num3
    print (minval)   