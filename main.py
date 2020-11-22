import vampire

alex = vampire.Vampire()
chris = vampire.Vampire.new_Vampire()

for key in alex.get_keys_of_attributes():
    print(key)

my_dice = vampire.Dices()
print(my_dice.d10(10))
