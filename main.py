from vampire import Vampire

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
    print_skills()
    print()
    i = 0
    skl = [3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]
    while len(skl) != 0:
        skill = input("Choose a skill: ")
        if skill == "help":
            print_skills()
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

    # step four - set disciplines
    print("\n\n4. Set your disciplines")
    print("You can choose two disciplines of the given list. One takes two points and the other one point.")

    # step five - choose hunting trait
    # TODO

    # step six - choose vantages
    # TODO
    

def print_attributes():
    for x in range(3):
        print(f"{'{:<15}'.format(Vampire.keys_attributes[x])} | {'{:<15}'.format(Vampire.keys_attributes[x+3])} | {'{:<15}'.format(Vampire.keys_attributes[x+6])}")


def print_skills():
    for x in range(9):
        print(f"{'{:<15}'.format(Vampire.keys_skills[x])} | {'{:<15}'.format(Vampire.keys_skills[x+9])} | {'{:<15}'.format(Vampire.keys_skills[x+18])}")    
    

if __name__ == "__main__":
    print("Welcome to the World of Darkness")
    
    while True:
        print("What do you want to do?")
        print(" [C]reate a new Vampire")
        print(" [L]oad an old Vampire")
        selection = input(": ")
        selection = selection.lower()

        if selection == "c":
            new_vampire()
            break
        elif selection == "l":
            print("\n\n\nNot yet implemented")
            break
        else:
            print("Please enter a valid option. \n\n")
