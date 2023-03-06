import string
import random

Name1 = "Marek"
Name2 = "CPU"

Name_list = [Name1, Name2]
possible_values = [1, 2, 3]
possible_values_str = ["1", "2", "3"]
How_many_pencils = input("How many pencils would you like to use: \n")

while True:
    if How_many_pencils.isdigit():
        How_many_pencils = int(How_many_pencils)
    else:
        print("The number of pencils should be numeric and non-negative")
        How_many_pencils = input()
        continue

    if How_many_pencils == 0:
        print("The number of pencils should be positive")
        How_many_pencils = input()
        continue

    Who_will_be_the_first = input(f"Who will be the first ({Name1}, {Name2}) \n")

    while Who_will_be_the_first not in Name_list:
        if Who_will_be_the_first not in Name_list:
            print(f"Choose between {Name1} and {Name2}")
            Who_will_be_the_first = input()
            continue
        else:
            break

    vertical_bars = ("|" * How_many_pencils)

    print(vertical_bars)

    while len(vertical_bars) != 0:
        print(f"{Who_will_be_the_first}'s turn")
        if Who_will_be_the_first == Name1:
            Who_will_be_the_first = Name2
        else:
            Who_will_be_the_first = Name1

        while True:

            if Who_will_be_the_first == Name2:  # (Human player here) remember the change!
                to_remove = input()
                if to_remove in possible_values_str:
                    to_remove = int(to_remove)
                    if to_remove > len(vertical_bars):
                        print("Too many pencils were taken")
                        continue
                    break
                if to_remove not in possible_values or to_remove in string.ascii_letters:
                    print("Possible values: '1', '2', '3'")
                    continue
            else:
                if len(vertical_bars) % 4 == 0:
                    to_remove = 3
                    print(to_remove)
                    break
                if len(vertical_bars) % 2 == 1 and len(vertical_bars) != 1:
                    to_remove = 2
                    print(to_remove)
                    break
                if len(vertical_bars) % 2 == 0:
                    to_remove = 1
                    print(to_remove)
                    break
                if len(vertical_bars) == 1:
                    to_remove = 1
                    print(to_remove)
                    break
                else:
                    to_remove = random.randint(1, 3)
                    print(to_remove)
                    break

        new_bars = len(vertical_bars) - to_remove
        vertical_bars = ("|" * new_bars)
        if len(vertical_bars) > 0:
            print(vertical_bars)
        else:
            if len(vertical_bars) == 0:
                print(f"{Who_will_be_the_first} won!")
                exit()
