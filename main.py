import vampire

alex = vampire.Vampire()
chris = vampire.Vampire.new_Vampire()

for key in alex.keys_attributes:
    print(key)

print(chris.get_skill("Firearms"))

my_dice = vampire.Vampire_Dices()
print(my_dice.d10(10))
