"""Defines a Menu class that allows users to pick from a list of options."""

from typing import List

class Menu:
    def __init__(self, choices: List[str]):
        self.choices = choices

    def get_choice(self):
        print("Please choose one of the following options by entering the "
              "corresponding number: ")
        i = 0
        for item in self.choices:
            i += 1
            print(f"{i}. {item}")

        selection = -1
        while selection not in range(1, len(self.choices) + 1):
            try:
                selection = int(input())
            except Exception:
                print("Please input a valid choice.")
        choice = self.choices[selection - 1]

        return choice
