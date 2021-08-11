"""Automatically generates a random OSR character."""

from typing import List

# Used to present a list of choices to the user.
#from cursesmenu import CursesMenu, SelectionMenu

from dice import roll_dice
from menu import Menu

class Character:
    def __init__(self):
        self.stats = dict(zip(["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"], self.roll_stats()))
        self.class_ = self.class_choice()
        self.gold = self.starting_gold()

    def roll_stats(self) -> List[int]:
        """Rolls 3d6 in order to generate a character's stats."""
        stats = []
        for i in range(6):
            # Rolls 3d6 6 times, and adds each to the list.
            stats.append(roll_dice(3, 6))

        return stats

    def class_choice(self) -> str:
        """
        Prints a list of classes that the character's stats qualify them for,
        then prompts the user to either select the class they want or randomly
        decide.

        :return str: The name of the class chosen.
        """
        # Used to contain all classes the character qualifies for.
        classes = self.available_classes()
        # TODO: Add demi-human & Advanced Fantasy classes.

        # TODO: Use color-coding to highlight classes based on the XP benefit
        # each gains from the class' Prime Requisite.
        print(f"Your stats so far are:\n{self.show_stats()}")
        choices = Menu(classes)
        choice = choices.get_choice()

        return choice

    def available_classes(self) -> List[str]:
        classes = []

        if self.stats["Strength"] >= 9:
            classes.append("Fighter")
            if self.stats["Dexterity"] >= 9:
                classes.append("Explorer")

        if self.stats["Dexterity"] >= 9:
            classes.append("Thief")

        if self.stats["Intelligence"] >= 9:
            classes.append("Mage")
            if self.stats["Strength"] >= 9:
                classes.append("Elven Spellsword")
                if self.stats["Dexterity"] >= 9:
                    classes.append("Elven Ranger")

        if self.stats["Wisdom"] >= 9:
            classes.append("Cleric")

        if self.stats["Constitution"] >= 9:
            if self.stats["Strength"] >= 9:
                classes.append("Dwarven Vaultguard")
            if self.stats["Wisdom"] >= 9:
                classes.append("Dwarven Craftpriest")

        if min(self.stats.values()) >= 11:
            classes.append("Nobiran")
        if any(self.stats.values()) == 18 and min(self.stats) >= 9:
            classes.append("Chosen")

        if len(classes) == 0:
            classes.append("0-level")
        return classes

    def prime_requisites_xp(self) -> List[str]:
        """Determines the prime requisites for each stat"""
        pass

    def starting_gold(self) -> int:
        """
        Rolls 3d6 x 10 gold for a starting character.

        :return int: The amount of gold for the character.
        """
        return roll_dice(3, 6) * 10

    def show_stats(self) -> str:
        """Used to neatly output the character's stats."""
        formatted_stats = ""
        for stat, value in self.stats.items():
            formatted_stats += (f"{stat}: {value}\n")

        return formatted_stats

    def __str__(self):
        stats = self.show_stats()
        return f"\n{stats}\nClass: {self.class_}\nGold: {self.gold}."

