#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for index in range(x):
            print(my_list[i], end="")
            count += 1
    except Exception:
        print()
        return count
    finally:
        print('')
        return count
