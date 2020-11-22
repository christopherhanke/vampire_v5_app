import json
from random import randint

class Vampire(json.JSONEncoder):
    clans = ["Brujah", "Gangrel", "Malkavian", "Nosferatu", "Toreador", "Tremere", "Ventrue"]
    
    # setting up standard dictionaries for attributes etc
    __attributes = {
        "Strength": None,
        "Dexterity": None,
        "Stamina": None,
        "Charisma": None,
        "Manipulation": None,
        "Composure": None,
        "Intelligence": None,
        "Wits": None,
        "Resolve": None
    }
    
    __skills = {
        "Athletics": None,
        "Brawl": None,
        "Craft": None,
        "Drive": None,
        "Firearms": None,
        "Larceny": None,
        "Melee": None,
        "Stealth": None,
        "Survival": None,

        "Animal Ken": None,
        "Etiquette": None,
        "Insight": None,
        "Intimidation": None,
        "Leadership": None,
        "Performance": None,
        "Persuasion": None,
        "Streetwise": None,
        "Subterfuge": None,

        "Academics": None,
        "Awareness": None,
        "Finance": None,
        "Investigation": None,
        "Medicine": None,
        "Occult": None,
        "Politics": None,
        "Science": None,
        "Technology": None
    }

    __disciplines = {
        "Animalism": None,
        "Auspex": None,
        "Blood Sorcery": None,
        "Celerity": None,
        "Dominate": None,
        "Fortitude": None,
        "Obfuscate": None,
        "Potence": None,
        "Presence": None
    }

    __health = {"total": None, "superficial": None, "aggravated": None}
    __willpower = {"total": None, "superficial": None, "aggravated": None}
    __hunger = None
    __humanity = None
    

    def get_keys_of_attributes(self):
        keys_of_attributes = self.__attributes.keys()
        return keys_of_attributes

    def get_keys_of_skills(self):
        keys_of_skills = self.__skills.keys()
        return keys_of_skills

    def get_keys_of_disciplines(self):
        keys_of_disciplines = self.__disciplines.keys()
        return keys_of_disciplines

    def __init__(self):
        pass
    

    # constructor method
    @classmethod
    def new_Vampire(cls):
        return cls()


class Dices:
    
    def __d10(self):
        return randint(1,10)
    

    def d10(self, x=1):
        """
        roll d10 x times, without arg it rolls once
        returns list of results
        """
        result = []
        for _ in range (x):
            result.append(self.__d10())
        
        return result

