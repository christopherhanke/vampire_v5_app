import json
from vampire import Vampire, Vampire_Encode


def create_vampire():
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
    print_attributes(vampire)
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
    print("You'll choose your skills out of a list of 27 skills, which will later \nrange up to a maximum level of five. Therefore you have to choose one \nof three templates.")
    print("You can choose between three templates. Jack of all trades / Balanced / Specialist.")
    print("[J]ack - (1x 3), (8x 2), (10x 1)")
    print("[B]alanced - (3x 3), (5x 2), (7x 1).")
    print("[S]pecialist - (1x 4), (3x 3), (3x 2), (3x 1)")
    while True:
        temp = input(">> ").lower()
        if temp == "j":
            skl = [3,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
            break
        elif temp == "b":
            skl = [3,3,3,2,2,2,2,2,1,1,1,1,1,1,1]
            break
        elif temp == "s":
            skl = [4,3,3,3,2,2,2,1,1,1]
            break
        else:
            print("Input was invalid. Please choose a template [B/J/S].")
    
    print("The skills are:")
    print_all_skills(vampire)
    
    while len(skl) != 0:
        skill = input("Choose a skill: ")
        if skill == "help":
            print_all_skills(vampire)
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
    print("\nNow you it's time for specialties.")
    for item in ["Academics", "Craft", "Performance", "Science"]:
        if vampire.get_skill(item):
            spec = input(f"Choose a specialty for {item}: ")
            vampire.set_specialty(item, spec)
    while True:
        skill = input("Choose a skill to specialize: ")
        if skill == "help":
            print_skills_learned(vampire)
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
                print(discipline, value, vampire.get_discipline(discipline), sep=" | ")
            else:
                print(f"Invalid value. {dsc}")
    
    # step five - choose hunting trait
    # TODO - for now not implementing. creation only for new vampires

    # step six - choose vantages
    # TODO

    return vampire


def peek_charactersheet(vampire):
    """
    shows a charactersheet template in the prompt
    """
    # print character infos
    print('{:*^66}'.format(" Character "))
    print(f"Name: {vampire.get_name()}")
    print(f"Clan: {vampire.get_clan()}")
    print()
    
    # print attributes
    print('{:*^66}'.format(" Attributes "))
    print_attributes(vampire)

    # print skills
    print('{:*^66}'.format(" Skills "))
    print_all_skills(vampire)

    # print specialties
    print('{:*^22}'.format(" Specialties "))
    list_spec = {}
    for i in range(len(vampire.get_specialties_keys())):
        key = vampire.get_specialties_keys()[i]
        print('{:<13}'.format(key), ": ", end="")
        for j in range(len(vampire.get_specialty(key))):
            if j+1 < len(vampire.get_specialty(key)):
                print(vampire.get_specialty(key)[j], end=", ")
            else:
                print(vampire.get_specialty(key)[j])
    print()

    # print disciplines
    print('{:*^66}'.format(" Disciplines "))
    list_dsc = {}
    for i in range(len(vampire.get_discipline_keys())):
        key = vampire.get_discipline_keys()[i]
        value = ""
        for _ in range(vampire.get_discipline(key)):
            value += "*"
        s = '{:<15}'.format(key) + '{:<5}'.format(value)
        list_dsc[key]=s
    
    for dsc in list_dsc.keys():
        print(list_dsc.get(dsc), " |")
        for i in range(vampire.get_discipline(dsc)):
            print(f"Trait {i+1}")
    print()

    # TODO - print vantages


# print function for prompt printing attributes
# printing attributes with/without value
def print_attributes(vampire):
    attr = []
    for i in range(len(vampire.keys_attributes)):
        key = vampire.keys_attributes[i]
        value = ""
        for _ in range(vampire.get_attribute(key)):
            value += "*"
        s = '{:<15}'.format(key) + '{:<5}'.format(value)
        if i < 6:
            s = s + " | "
        attr.append(s)

    for i in range(3):
        s_out = attr[i] + attr[i+3] + attr[i+6]
        print(s_out)
    print()


# print function for prompt printing skills
# printing skills with/without value
def print_all_skills(vampire):
    skl = []
    for i in range(len(vampire.keys_skills)):
        key = vampire.keys_skills[i]
        value = ""
        for _ in range(vampire.get_skill(key)):
            value += "*"
        s = '{:<15}'.format(key) + '{:<5}'.format(value)
        if i < 18:
            s = s + " | "
        skl.append(s)
    
    for i in range(9):
        s_out = skl[i] + skl[i+9] + skl[i+18]
        print(s_out)
    print()


# prints only learned skills
def print_skills_learned(vampire):
    skills = []
    for key in Vampire.keys_skills:
        if vampire.get_skill(key) != 0:
            skills.append(key)
    for i in range(len(skills)):
        if i % 2 != 0:
            print(f"{'{:<15}'.format(Vampire.keys_skills[x])} | ", end="")
        else:
            print(f"{'{:<15}'.format(Vampire.keys_skills[x])}")
    

# prints all avaible disciplines to learn
def print_disciplines(vampire):
    if vampire.get_clan() != "Caitiff":
        disciplines = Vampire.clans.get(vampire.get_clan())
        print(f"{'{:<15}'.format(disciplines[0])} | {'{:<15}'.format(disciplines[1])} | {'{:<15}'.format(disciplines[2])}")
    else:
        for x in range(5):
            print(f"{'{:<15}'.format(Vampire.keys_disciplines[x])} | {'{:<15}'.format(Vampire.keys_disciplines[x+5])}")
    

# MAIN - Start and Play
if __name__ == "__main__":
    print("Welcome to the World of Darkness")
    
    # first Menu - Create or Load a Vampire
    while True:
        print("What do you want to do?")
        print(" [C]reate a new Vampire")
        print(" [R]andomize a new Vampire")
        print(" [L]oad an old Vampire")
        print(" [Q]uit")
        selection = input(": ")
        selection = selection.lower()

        if selection == "c":
            vampire = create_vampire()
            break
        elif selection == "l":
            vampire = Vampire.new_Vampire_from_file("save.json")
            break
        elif selection == "r":
            print("\nNot yet implemented [RANDOMIZE]\n")
            continue
        elif selection == "q":
            exit()
        else:
            print("Please enter a valid option. \n\n")
    
    # Main Menu in game
    while True:
        print("\n\nGame - Main Menu.")
        print(" [M]ake check")
        print(" [P]eek Character sheet")
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
            peek_charactersheet(vampire)
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
