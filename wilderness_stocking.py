"""Stocks wilderness hexes as laid out in Axioms Issue 8."""
import random

from dice import roll_dice

def hex_input():
    """Prompts the user to input the type of hex being traversed."""
    terrain = -1
    while terrain not in [1, 2, 3]:
        terrain = int(input("Please enter the digit corresponding to the type of terrain being traversed:"
                           "\n  1. Clear, Grass, Scrub \n  2. Hills, Woods, River, Ocean\n 3. Barren, Desert, Swamp, Jungle\n"))
    roll_stocking(terrain)

def roll_stocking(table):
    """Table is int 1-3, based on hex_input."""
    roll = roll_dice(1, 20)
    print(f"Roll is {roll}")
    #TODO: Link to Wilderness Encounter tables.
    if table == 1:
        unique = [1, 2]
        dangerous = range(3, 8)
        valuable = range(13, 18)
        encounter = range(18, 21)
    elif table == 2:
        unique = [1, 2]
        dangerous = range(3, 7)
        valuable = range(10, 14)
        encounter = range(14, 21)
    elif table == 3:
        unique = [1]
        dangerous = range(2, 5)
        valuable = range(8, 11)
        encounter = range(11, 21)
    else:
        raise ValueError("You have to pick one of the three tables!")
    if roll in unique:
        unique_terrain()
    elif roll in dangerous:
        dangerous_terrain()
    elif roll in valuable:
        valuable_terrain()
    elif roll in encounter:
        print("wilderness encounter\n")
    else:
        print("No encounter.\n")

# TODO: Adjust treasure tables to match the terrain.

def unique_terrain():
    """Generates a Unique Terrain roll."""
    roll = roll_dice(1, 12)
    if roll == 1:
        # TODO: Roll treasure table for this, AND determine value, finally using that to determine distance.
        print("Complex Map: The adventurers find a location that is in itself a treasure map. An example might look similar to Stonehenge. It can be difficult to decipher the map, or even to learn that it is a map at all. If deciphered, it leads to a treasure. The treasure is 1 hex away per 1,000 gp value (the Judge may use the average value and roll the actual contents of the treasure later). Roll 1d6 to determine the treasure type the map points to.")
        print("(See Axioms Compedium I pg. 257 for table)")
    elif roll == 2:
        print("Curse: The adventurers find a cursed place or object. Roll on the Curse table to get some idea of what sort of curse has been found, and how it may affect the party. Some of the curses on the Curse table reflect their transmission or methodology, while others suggest what penalty the curse inflicts. If a penalty is not suggested, use the Bestow Curse spell as a starting point, or use any curse the Judge has in mind.")
        # TODO: Add Curse table roll.
        print("(See pg. 257 of Axioms Compendium I for table)")
    elif roll == 3:
        print("Empowering Place: The adventurers find a place capable of temporarily empowering non-magical items with the powers of a magical item. Choose or roll a magic item that the place is ca- pable of duplicating, then choose a method by which the terrain can deliver this power. (For example, a cliff might empower the boots of someone who leaps off it with the powers of boots of levitation.) Only a non-magical item may be empowered, and only one such item may be empowered at a time. The empow- ered item will serve as the magical item for 1d6 days, but will then be destroyed. (It does not merely become nonmagical; the physical item is destroyed.) If desired, the Judge can roll on the Structure table when placing an empowering place.")
    elif roll == 4:
        print("Lesser Terrain: The adventurers find something that appears unique at first, but turns out not to be. Roll on the Valuable or Dangerous terrain tables instead (50% chance of either). The terrain found will appear more fantastic than usual, but will function as normal.")
        if roll_dice(1, 2) == 1:
            print("You found a fantastical valuable terrain.")
            valuable_terrain()
        else:
            print("You found a fantastical dangerous terrain.")
            dangerous_terrain()
    elif roll == 5:
        print("Magical Place: The adventurers find a place that is capable of duplicating the effect of a spell of some kind. Choose or roll the source of the magic (arcane, divine, eldritch, etc.), then choose or roll a spell from their spell list. Unless the Judge wishes to choose something, a good default is to roll as if it were a scroll found. Then choose a method by which this place can duplicate the spell. For example, a pool may cast Cure Light Wounds on anyone who bathes in it under the moonlight. The place is ca- pable of creating the spell effect with a frequency determined by the level of spell, but never more often than once per day per target. If desired, the Judge can roll on the structure table when placing a Magical Place.")
        print("(1st lvl: 5/day\n2nd level: 3/day\n 3rd level: 1/day\n4th level: 1/wk\n5th level: 1/month\n6th level:1/year\n7th level and higher: 1 decade or longer)")
        # TODO: Determine random spell or magical source for this.
    elif roll == 6:
        print("Magical Resource: The adventurers find a naturally-occurring magical resource. Treat as a special component or magical compound of the Judge’s choice (or roll on the encounter ta- ble to find out what creature it counts as a component from). The magical resource does not require metamphora to store. It weighs 1 stone per 10 gp value and the adventurers find an amount worth 3d6 x 1,000gp. If the party returns later, they will find that more has grown; the Judge may assign a growth rate (a reasonable average is approximately 33 months to restore the full amount) or reroll its value.")
        # TODO: Randomly roll the magical resource.
    elif roll == 7:
        print("Monstrous Shadow: A nearby terrible monster casts a shadow over the area (or brightens the area, if the monster is Lawful). Roll a random encounter for the terrain to determine the type of terrible monster. If the encounter includes multiple monsters, only one of them is the terrible monster, and it leads the others. The terrible monster is always in a lair - even if its type does not normally make lairs. If the terrible monster has less than 11 HD, increase its HD to 11 as a result of the powers it has been infused with. For each HD of increase, the monster’s AC improves by ½ and the monster deals an average of 2 hp more damage di- vided among all its attacks. Increase the monster’s size by one category, to a minimum of Large (ogre-sized). If its alignment is Neutral, change it to Chaotic. The terrible monster’s lair is a shadowed (minor) sinkhole of evil (or equivalent pinnacle of good, if Lawful). If it is slain, the sinkhole of evil (or pinnacle of good) will disperse in 1d4 days. The creature rarely goes far from its lair, but otherwise acts as normal for a creature of its type. The lair will have normal treasure for the monster’s type, plus additional treasure by terrain type.")
        # TODO: Automate the level of the sinkhole based on the monster generated and its HD.
    elif roll == 8:
        # TODO: Automate rolling.
        print("Place of Power: The adventurers find a place of power of some kind. Roll to determine the type and power. If desired, the Judge can roll on the Structure table when placing a place of power.")
        print("(roll on table, Axioms Compendium I pg. 259)")
    elif roll == 9:
        print("Portal: The adventurers find a portal linking two locations. The portal may transfer only sensory information (sight and/or sound), or may allow travel through it. The portal may be always active, or may be limited in some fashion (such as functioning only during an eclipse). A portal that allows travel is always limited in some fashion (though a portal may be always active for sight and/or sound, but allow travel only in limited circum- stances). The Judge should choose a location for the other end of the portal that is appropriate for his setting. Note that the two ends of the portal may have different conditions for when they activate – for instance, one end might activate during a lunar eclipse while the other end activates during a solar eclipse – and the other end is not guaranteed to be a safe destination, making travel through an unknown portal extremely dangerous. At the Judge’s discretion, the portal link may manifest in other ways than an actual portal (such as treating the two locations as the same for the purposes of spellcasting range).")
        # TODO: Low priority. Automate where the portal links to.
    elif roll == 10:
        print("Relic: The adventurers find a relic of a time long gone. The relic is not necessarily magical, but is valuable. Roll as for a Regalia (1d100+80 on Jewelry table in ACKS Core) to determine its val- ue. 10% of relics are also magical (choose or roll a magic item); of those that are magical, 10% are cursed (Judge’s choice).")
        # TODO: Automate rolling of this.
    elif roll == 11:
        print("Truly Unique: The adventurers find something truly unique. This category is a catch-all for anything the Judge wishes to place in this hex (usually something they saw in another source and thought was awesome). If the Judge justifiably feels that the point of a random table is to keep from having to invent things whole cloth like this, choose another result or reroll!")
        # TODO: Build up a database of 'truly unique' hex encounters then randomly roll on it.
    elif roll == 12:
        print("Doubles! If this was already rolled before, ignore it; there cannot be more than two Unique Terrains in a hex.")
        unique_terrain()
        unique_terrain()

def dangerous_terrain():
    """Generates a Dangerous Terrain roll."""
    roll = roll_dice(1, 12)
    if roll == 1:
        print("Enshrouding Terrain: The adventurers locate terrain that makes it very difficult to see what is going on, such as a deep valley surrounded on all sides by forest. An army that enters mass combat while positioned in the enshrouding terrain is in trouble. Each commander in such an army suffers a penalty to their Strategic Ability. The Judge may choose the penalty or roll 1d3. In addition, each commander in the army suffers a penalty to their Leadership Ability, again chosen or rolled on 1d3. The penalties may be identical or different. (Of course, if the adven- turers ambush an enemy while they travel through the area, it is they that would suffer the penalties!)")
    elif roll == 2:
        print("Fearful Despoiling: Roll once on the Valuable Terrain table. The adventurers find that result, but despoiled, desecrated, or otherwise destroyed. This calamity is fearful enough to neces- sitate a Morale roll for followers (but not for henchmen); see table.")
        print("(Table: 2-: Flee, 3-5: Tender resignation, 6-8: No effect, 9-11: Renewed zeal, 12+: Filled with fire)")
        print("Flee: The affected followers drop whatever they were holding and flee in a panic. Tender resignation: The affected followers immediately tender their resignation, but continue to serve until they have a safe opportunity to leave. No effect: The affected followers are shaken, but recover. Renewed zeal: The affected followers harden themselves against this kind of shock, and automatically succeed on their next mo- rale roll during this expedition. Filled with fire: The affected followers take this as a personal cru- sade, and automatically succeed on all morale rolls made during this expedition.")
    elif roll == 3:
        print("Foul Water: The adventurers are unable to find any water that is safe to drink on their day’s journey. Unless the expedition carried water with it, the adventurers begin to suffer the pen- alties of dehydration. Foul water is rarely confined to only a single place; until a member of the party succeeds on a hunting or foraging proficiency throw on a subsequent day (or it rains), the adventurers remain unable to find any safe water.")
    elif roll == 4:
        print("Foul Weather: The weather is foul, whatever that means for the season and terrain the adventurers are in. Foul weather caus- es the adventurers to move at most at half speed for 1d6 days. If this result is rolled again before the previous foul weather expires, the weather becomes even worse for the overlapping duration. At the Judge’s discretion, depending on the season and terrain, the weather may totally stop the adventurers or may be dangerous (such as a blizzard). Rolling this result mul- tiple times can create truly life-threatening weather such as ice storms, nor’easters, hurricanes, and monsoons.")
    elif roll == 5:
        print("Plague: The party is exposed to a disease of some sort. When this occurs, the type of disease is determined with a roll of 1d100 on the Disease Type table. Subtract 10 if the party is in a swamp or jungle hex, and add 10 if the party is in a clear, glass, or scrublands hex. Once the disease is identified, each 30 fol- lowers, each henchman, and each adventurer must then make a saving throw versus Death against the disease. Certain diseases, being less acute, offer a saving throw bonus.")
        # TODO: Add Disease Type table.
        print("See table in book - pg. 256 of Axioms Compendium I")
    elif roll == 6:
        # TODO: Add poison roll.
        print("Poison: The adventurers find something poisonous. Roll on the Poisons table to determine what type of poison was found in what quantity. The poison may be disguised, and appear to be useful herbs or other valuable commodity. A character with Nat- uralism proficiency throw (or another appropriate proficiency) can identify the find with a proficiency throw of 11+. However, if the find is probed without proper caution, the adventurer is exposed to the poison and must succeed on a saving throw vs. Poison or suffer its effects.")
        print("If correctly identified, the poison can be harvested. Harvesting poison properly requires a Naturalism proficiency throw for a plant toxin and an Animal Husbandry proficiency throw for a creature venom. In either case, the required target value is listed on the table below. On a roll of a natural 1, the gatherer has been exposed to the poison, and must succeed on a saving throw v. Poison or suffer its effects. Harvesting the poison takes 1 turn per dose. (If using the optional Campaign Activities rules, har- vesting 6 doses of poison counts as a minor strenuous activity.) Doubling the harvest time increases the proficiency throw by +4, tripling it increases the proficiency throw by +8. Each dose harvested counts as one item for encumbrance purposes.")
        print("See book, pg. 257 of Axioms Compedium I, for poisons table.")
    elif roll == 7:
        print("Quagmire: The adventurers run across some sort of terrain that delays their travel, such as fallen trees, a wildfire off in the distance, or even a literal quagmire. Whatever the reason, the adventurers make no further progress today, and move at half speed the next day.")
    elif roll == 8:
        # TODO: Determine if it guards treasure and roll if so.
        print("Snare: The adventurers find a trap intended to catch, rather than kill. Determine the trap as if it were a dungeon of level 5 (that is, very effective). 25% of snares guard treasure; if this snare guards treasure, determine the treasure type as per Cache by consulting the Treasure Type by Terrain table.")
    elif roll == 9:
        print(f"Spoilage: Some event or terrain feature (a wagon throwing an axle, a horse throwing a hoof, a bag falling into the swamp, etc.) causes the adventurers to lose stored rations. Their expedition loses {roll_dice(1, 8) * 5}% of its stored rations.")
    elif roll == 10:
        # TODO: Determine if it guards treasure and roll if so.
        print("Trap: The adventurers find a deadly trap of some kind. Deter- mine the trap as if it were a dungeon of level 5 (which is to say extraordinarily fatal). 25% of deadly traps guard treasure; if this trap guards treasure, determine the treasure type by consulting the Treasure Type by Terrain table.")
    elif roll == 11:
        print("Wasteland: The hex is dead and barren. Reduce its Land Value by 1, to a minimum of 3. This result stacks if rolled multiple times in the same hex.")
    elif roll == 12:
        print("Doubles!")
        dangerous_terrain()
        dangerous_terrain()

def valuable_terrain():
    """Generates a Valuable Terrain roll."""
    roll = roll_dice(1, 12)
    if roll == 1:
        print("Cache: The adventurers find a hidden stash of loot or other unguarded treasure. Roll for treasure as per the Treasure Type by Terrain table.")
    if roll == 2:
        print("Food: The adventurers find an easily-accessible source of food;"
              " perhaps the adventurers found a fruit grove, a deer leapt "
              "across their path, or they stumbled upon a patch of delicious mushrooms."
              f"Gain {roll_dice(4, 10)} rations.")
    if roll == 3:
        print("Hidden Settlement: The adventurers find a hidden settlement. Roll "
              "randomly on the encounter table for the terrain to discover what "
              " type of creatures live there. Regardless of the result, the "
              "creatures will not be actively hostile. (If they are unintelligent,"
              " they may simply not mind the party’s presence; if they are Chaotic,"
              "they may be hiding and just want to be left alone. The details "
              "of why this particular group is not actively hostile are left to "
              "the Judge.) A hidden settlement of intelligent creatures may be "
              "treated as a Class VI market with only half the normal number of items available (rounded up).")
    if roll == 4:
        print("Monster Carcass: The adventurers find a dead monster or mon- sters. "
              "Roll as for a random encounter in the hex. The adventur- ers find "
              "the result rolled dead in their path. The corpse’s age in days is "
              f"{roll_dice(1, 4)} divided by the terrain movement modifier for the hex. "
              "The monster may have salvageable parts, as per Lairs & Encounters, at the Judge’s discretion.")
    if roll == 5:
        print("Perfect Weather: The adventurers hit a patch of perfect weather, "
              "whatever that means for the season and location the adventur- ers "
              "are in. This makes their travel much easier. The adventurers may "
              "either choose to count this day’s journey as a day of rest, or the"
              " adventurers may force march this day without penalty.")
    if roll == 6:
        # TODO: Create Merchandise table to roll on.
        print("Resource: The adventurers find that the hex has a valuable resource in it. Increase the land value of the hex by 1, to a maximum of 9. Alternately, the adventurers may plunder the resource, gaining 10d10 loads of a trade good; if the hex is plundered, do not increase its land value. To determine what the resource is, roll randomly on the Merchandise table in ACKS Core. If the result is a finished good, the adventurers find the raw materials appropriate to create that good. (At the Judge’s discretion, if the resource is Precious Merchandise, the land value may be increased by 2 or more points if the resource is left unplundered.) The Judge should determine the amount of time required to plunder the resource. By default, it requires one day per character per 60gp of goods to plunder resources. (If using the optional Campaign Activities rules, plundering 60gp of goods counts as a major strenuous activity.)")
    if roll == 7:
        print(f"Ruin: The adventurers find an abandoned, unoccupied {structure()}. The struc- ture is damaged, but could be repaired. To find the ruin’s value, roll 1d12 and add a modifier as indicated by terrain type. The ruin has an initial value of 39,000 gp plus another 2,000 gp times the result of the Judge’s roll. Of course, these ruins are not in pristine shape; they wouldn’t be ruins if they were! The more wild and unsettled the terrain, the more likely the ruin is to be horrifically decayed. Roll 2d10 and subtract twice the terrain modifier listed above to determine what percentage of the ruin’s value has survived, to a minimum of 1%. At the Judge’s discre- tion, this value may be rounded to the nearest 5%.")
        print("(Terrain modifiers: Clear/Grass/Scrub 0, Hills/Mountains/Woods/River +2, Jungle/Swamp/Ocean/Desert/Barren +4)")
    if roll == 8:
        print("Safe Haven: The adventurers find a hidden, guarded, or other- wise especially safe location. While resting here, the adventur- ers will not be discovered by any random encounters, though the adventurers may be followed into the redoubt if they at- tempt to escape into it.")
    if roll == 9:
        print("Shortcut: The adventurers find a shortcut. Draw a line from the face of the hex the adventurers entered the hex from, to the face of the hex the adventurers leave through, along the direction of their travel. When traveling between these faces, the adventur- ers may treat the hex as having no modifier to travel speed. If the hex’s terrain already gave no modifier, the adventurers may treat it as a road instead. (At the Judge’s discretion, to simplify, these effects may be applied when traveling through the hex in any direction instead of only along their original axis of travel.)")
    if roll == 10:
        # TODO: Roll for which useful herb it is.
        print("Useful Herbs: The adventurers find a place where useful herbs grow. A character with Naturalism proficiency throw (or another appropriate proficiency) can identify the find with a proficiency throw of 11+. If correctly identified, the herbs can be harvested."
              f"There will be {roll_dice(2, 100)} lbs of herbs. Harvesting the"
              " herbs takes 1 turn per 5 lbs. (If using the optional Campaign"
              " activities rules, harvesting 180 lbs of herbs counts as a major"
              " strenous activity; e.g. 180lbs in 6 hours.) Each pound counts as"
              " one item for encumbrance purposes.")
    if roll == 11:
        print("View: The adventurers find a place with a fantastic view of the surrounding terrain. In addition to being an exemplar of nat- ural beauty, it offers an excellent strategic command post. If an army enters mass combat while controlling the viewpoint, each commander in the army gains a bonus to their Strategic Ability. The Judge may choose a bonus or roll 1d3.")
    if roll == 12:
        # TODO: Add ability to roll on Unique Terrain instead if a double is rolled again.
        print("Double terrain!")
        valuable_terrain()
        valuable_terrain()

def structure():
    """Generates a structure as laid out in Axioms 8."""
    roll = roll_dice(1, 20)
    structures = {1: "Aqueduct", 2: "Barrow mound", 3: "Bridge", 4: "Castle",
                  5: "Colossus", 6: "Cottage", 7: "Keep", 8: "Manor", 9: "Mausoleum",
                  10: "Monastery", 11: "Monument", 12: "Mine", 13: "Observatory",
                  14: "Prison", 15: "Outpost", 16: "Shrine/temple", 17: "Tomb",
                  18: "Tower", 19: "Villa", 20: "Wizard's Dungeon"}
    return structures[roll]

if __name__ == "__main__":
    hex_input()
