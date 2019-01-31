#!/bin/python3

import sys

def main():
    print("Start...")

    entered_time = input("Enter time:")

    total_mins = 0

    while entered_time != "":
        negative = True if entered_time[0] == "-" else False
        time_parts = [int(s) for s in entered_time.split(':')]
        if not negative:
            total_mins += time_parts[0] * 60 + time_parts[1]
        else:
            total_mins -= abs(time_parts[0]) * 60 + time_parts[1]
            
        print ("Total (mins): %d" % total_mins)

        hours, mins = divmod(total_mins, 60)

        print("Total: %d:%d" % (hours, mins))
        print()
        entered_time = input("Enter time: ")
    return 0

if __name__ == "__main__":
    sys.exit(main())
