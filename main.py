import random
import os
import time


list = []
list2 = []


def main():
    team = 0
    player = int(input("Zadej počet hráčů: "))
    if player % 2 == 0 and player <= 10:
        x = input("Zadej jmena hráčů: ")
        list = x.split()
        while team < player / 2:
            team1 = random.choice(list)
            list2.append(team1)
            list.remove(team1)
            team += 1

        print(f"\nTeam 1 je: {list2}")
        print(f"\nTeam 2 je: {list}")
        map()
    else:
        print("Špatný počet hráču")
        time.sleep(3)
        os.system("cls")
        main()


def map():
    map_random = ["Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze"]
    print(f"\nmapa je: {random.choice(map_random)}")
    time.sleep(90)


if __name__ == "__main__":
    main()
