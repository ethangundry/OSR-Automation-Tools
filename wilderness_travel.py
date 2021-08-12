import random

from dice import roll_dice

class Party:
    """
    Defines an adventuring party to keep track of rations and proficiencies.
    """
    def __init__(self):
        self.rations = 0
        self.survival = False
        self.navigation = False
        self.terrain = ''
        surv = None
        nav = None

        self.rations = int(input("How many rations does your party currently have?"))
        self.consumption = int(input("How many rations does your party consume a day?"))

        while surv not in [1, 2]:
            surv = int(input("Does your party have Survival as a proficiency? 1 for yes, 2 for no."))
        if surv == 1:
            self.survival = True

        while nav not in [1, 2]:
            nav = int(input("Does your party have Navigation as a proficiency? 1 for yes, 2 for no."))
        if nav == 1:
            self.navigation = True

        self.loop()

    def loop(self):
        choice = ''
        while choice != 5:
            choice = int(input("Choose from the following:\n1.New day\n2.Increase rations\n3.Decrease rations\n4.Set ration consumption\n5.Quit"))
            if choice == 1:
                terrain = input("Please input one of the following options: p for plains, m for mountains, h for hills, f for forest, c for coast, s for sea, d for desert, j for jungle, w for swamp")
                self.forage()
                self.get_lost(terrain)
                self.rations -= self.consumption
            elif choice == 2:
                self.rations += input("Increase your rations by how many?")
            elif choice == 3:
                self.rations -= input("Decrease rations by how many?")
            elif choice == 4:
                self.consumption = int(input("How many rations does your party consume a day?"))
            elif choice == 5:
                print("Goodbye!")

            print(f"You now have {self.rations} rations. Your party is consuming {self.consumption} rations per day.")

    def forage(self):
        """
        determines how much food is foraged per day if any. survival is true if
        a character in the party has the survival proficiency.
        """
        target = 18
        if self.survival:
            target -= 4
        if roll_dice(1, 20) >= target:
            food = roll_dice(1, 6)
            print(f"Foraged {food} rations.")
            self.rations += food
        else:
            print("Found no rations today.")

    def get_lost(self, terrain, navigation=False):
        """
        Determines if the characters get lost based on their terrain. Navigation is whether
        a character in the party has the navigation proficiency.
        """
        target = -1
        if terrain == 'p':
            target = 4
        elif terrain in ['m', 'h', 'f', 'c']:
            target = 7
        elif terrain in ['s', 'd', 'j', 'w']:
            target = 11

        if roll_dice(1, 20) >= target:
            print("Not lost.")
        else:
            print(f"Lost. Heading {random.choice('southeast', 'southwest', 'south', 'north', 'northeast', 'northwest')}.")

if __name__ == "__main__":
    x = Party()

