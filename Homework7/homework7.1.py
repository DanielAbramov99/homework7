counter_positive = 0
counter_negative = 0
counter_zero = 0
counter_divide_seven = 0
negative_number = None
positive_number = None
for num in range(10):
    number: int = int(input("enter number:"))
    if number < -1000 or number > 1000:
        continue
    if number == -999:
        break
    else:
        if number < 0:
            counter_negative += 1
            negative_number = number
        if number > 0:
            counter_positive += 1
            positive_number = number
        if number == 0:
            counter_zero += 1
        elif number % 7 == 0:
            counter_divide_seven += 1
        num += 1
    if num == 10:
        print(f"the amount of negative numbers are:{counter_negative}")
        print(f"the amount of positive numbers are:{counter_positive}")
        print(f"the amount of zeroes are:{counter_zero}")
        print(f"the amount of numbers that can be divided by seven are:{counter_divide_seven}")
        print(f"the last positive number is:{positive_number}")
        print(f"the last negative number is:{negative_number}")
