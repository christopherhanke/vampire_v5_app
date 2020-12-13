import json
from vampire import Vampire, Vampire_Encode


def new_vampire():
    vampire = Vampire.new_Vampire()
    
    # step one - choose a clan
    print("\n\n1. Choose a clan")
    for key in Vampire.clans.keys():
        print(key)
    while True:
        clan = input(">> ")
        if clan in Vampire.clans.keys():
            vampire.set_clan(clan)
            break
        else:
            print("Invalid clan name!")
    
    # step two - set attributes
    print("\n\n2. Set your attributes")
    print("You'll have nine attributes with a range from one (1) to a later maximum of five (5).")
    print("At the beginning you can choose one attribute at four (1x 4), three times three (3x 3), \nfour times two (4x 2) and one attribute at one (1x 1).")
    print("The attributes are:")
    print_attributes()
    print()
    i = 0
    attr = [4, 3, 3, 3, 2, 2, 2, 2, 1]
    while i in range(len(Vampire.keys_attributes)):
        item = Vampire.keys_attributes[i]
        try:
            value = int(input(f"{'{:<15}'.format(item)}: "))
        except ValueError:
            value = 0
        if value in attr:
            vampire.set_attribute(Vampire.keys_attributes[i], value)
            attr.remove(value)
            i += 1
        else:
            print(f"Invalid value. {attr}")
    
    # step three - set skills
    print("\n\n3. Set your skill")
    print("You can choose out of a list of 27 skills. Skills you learned \nare in range of one (1) to a later maximum of five (5)")
    print("At the beginning you can choose three skills at three (3x 3), five times two (5x 2) and seven times one (7x 1).")
    print("The skills are:")
    print_all_skills()
    print()
    i = 0
    skl = [3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]
    while len(skl) != 0:
        skill = input("Choose a skill: ")
        if skill == "help":
            print_all_skills()
            print(f"\n{skl}\n")
        elif not skill in Vampire.keys_skills:
            print("Skill not valid. Enter 'help' for list of skills.")
            continue
        elif skill in Vampire.keys_skills and vampire.get_skill(skill):
            print(f"You already chose {skill} with {vampire.get_skill(skill)} points.")
        else:
            try:
                value = int(input(f"Set level for {skill}: "))
            except ValueError:
                value = 0
            if value in skl:
                vampire.set_skill(skill, value)
                skl.remove(value)
            else:
                print(f"Invaldi value. {skl}")
    
    # set specials
    # TODO
    print("\nNow you it's time for specialties.")
    for item in ["Academics", "Craft", "Performance", "Science"]:
        if vampire.get_skill(item):
            spec = input(f"Choose a specialty for {item}: ")
            vampire.set_specialty(item, spec)
    while True:
        skill = input("Choose a skill to specialize: ")
        if skill == "help":
            print_vamp_skills(vampire)
            continue
        elif vampire.get_skill(skill) == 0:
            print(f"You don't have {skill} as a skill.")
            continue
        else:
            spez = input(f"Choose a specialty for {skill}: ")
            try:
                vampire.set_specialty(skill, spez)
            except Exception as err:
                print(err.args)
            break

    # step four - set disciplines
    print("\n\n4. Set your disciplines")
    print("You can choose two disciplines of the given list. One takes two points and the other one point.")
    print_disciplines(vampire)
    print()
    i = 0
    dsc = [2, 1]
    while len(dsc) != 0:
        discipline = input("Choose a discipline: ")
        if discipline == "help":
            print_disciplines(vampire)
            continue
        elif not discipline in Vampire.keys_disciplines:
            print("Discipline not valid. Enter 'help' for list of skills.")
            continue
        elif not discipline in Vampire.clans.get(vampire.get_clan()) and vampire.get_clan() != "Caitiff":
            print("Discipline not valid. Enter 'help' for list of skills.")
            continue
        elif discipline in Vampire.clans.get(vampire.get_clan()) and vampire.get_discipline(discipline) and vampire.get_clan() != "Caitiff":
            print(f"You already chose {discipline} with {vampire.get_discipline(discipline)} points.")
            continue
        else:
            try:
                value = int(input(f"Set level for {discipline}: "))
            except ValueError:
                value = 0
            if value in dsc:
                vampire.set_discipline(discipline, value)
                dsc.remove(value)
            else:
                print(f"Invalid value. {dsc}")
    
    # step five - choose hunting trait
    # TODO

    # step six - choose vantages
    # TODO

    return vampire


def peek(vampire):
    while True:
        print("\nPeek - Menu")
        print(" [A]ttributes")
        print(" [C]lan")
        print(" [D]isciplines")
        print(" [S]kills")
        print(" [Q]uit menu")
        selection = input(": ")
        selection = selection.lower()

        if selection == "a":
            for i in range(len(vampire.keys_attributes)):
                key = vampire.keys_attributes[i]
                value = ""
                for _ in range(vampire.get_attribute(key)):
                    value += "*"
                print(f"{'{:<15}'.format(key)} {'{:<5}'.format(value)}", end="")
                if (i+1) % 3 == 0:
                    print()
                else:
                    print(" | ", end="")
            pass
        elif selection == "c":
            print(f"Clan: {vampire.get_clan()}")
        elif selection == "s":
            pass
        elif selection == "d":
            pass
        elif selection == "q":
            break
        else:
            print("Please enter a valid option.")


def print_attributes():
    for x in range(3):
        print(f"{'{:<15}'.format(Vampire.keys_attributes[x])} | {'{:<15}'.format(Vampire.keys_attributes[x+3])} | {'{:<15}'.format(Vampire.keys_attributes[x+6])}")


def print_all_skills():
    for x in range(9):
        print(f"{'{:<15}'.format(Vampire.keys_skills[x])} | {'{:<15}'.format(Vampire.keys_skills[x+9])} | {'{:<15}'.format(Vampire.keys_skills[x+18])}")


def print_vamp_skills(vampire):
    skills = []
    for key in Vampire.keys_skills:
        if vampire.get_skill(key) != 0:
            skills.append(key)
    for i in range(len(skills)):
        if i % 2 != 0:
            print(f"{'{:<15}'.format(Vampire.keys_skills[x])} | ", end="")
        else:
            print(f"{'{:<15}'.format(Vampire.keys_skills[x])}")
    

def print_disciplines(vampire):
    if vampire.get_clan() != "Caitiff":
        disciplines = Vampire.clans.get(vampire.get_clan())
        print(f"{'{:<15}'.format(disciplines[0])} | {'{:<15}'.format(disciplines[1])} | {'{:<15}'.format(disciplines[2])}")
    else:
        for x in range(5):
            print(f"{'{:<15}'.format(Vampire.keys_disciplines[x])} | {'{:<15}'.format(Vampire.keys_disciplines[x+5])}")
    

if __name__ == "__main__":
    print("Welcome to the World of Darkness")
    
    while True:
        print("What do you want to do?")
        print(" [C]reate a new Vampire")
        print(" [R]andomize a new Vampire")
        print(" [L]oad an old Vampire")
        print(" [Q]uit")
        selection = input(": ")
        selection = selection.lower()

        if selection == "c":
            vampire = new_vampire()
            break
        elif selection == "l":
            vampire = Vampire.new_Vampire_from_file("save.json")
            break
        elif selection == "r":
            print("\nNot yet implemented [RANDOMIZE]\n")
            break
        elif selection == "q":
            exit()
        else:
            print("Please enter a valid option. \n\n")
    
    while True:
        print("\n\nGame - Main Menu.")
        print(" [M]ake check")
        print(" [P]eek stats")
        print(" [S]ave character stats")
        print(" [Q]uit")
        selection = input(": ")
        selection = selection.lower()

        if selection == "q":
            exit()
        elif selection == "m":
            print("Not yet implemented")
            continue
        elif selection == "p":
            peek(vampire)
            continue
        elif selection == "s":
            try:
                with open("save.json", "w") as save_file:
                    save_file.write(Vampire_Encode().encode(vampire))
            except FileNotFoundError:
                print(Vampire_Encode().encode(vampire))
            else:
                print("Data saved.")
            continue
        else:
            print("Please enter a valid option.\n\n")
