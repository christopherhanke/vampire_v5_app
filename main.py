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
    for item in Vampire.keys_attributes:
        if item in Vampire.keys_attributes[:2] or item in Vampire.keys_attributes[3:5] or item in Vampire.keys_attributes[6:8]:
            print(item, end=", ")
        else:
            print(item)
    
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
