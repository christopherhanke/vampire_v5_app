import json
from random import randint

class Vampire(json.JSONEncoder):
    # static lists
    clans = ["Brujah", "Gangrel", "Malkavian", "Nosferatu", "Toreador", "Tremere", "Ventrue"]
    
    # static key lists
    keys_attributes = ["Strength", "Dexterity", "Stamina", "Charisma", "Manipulation", "Composure", "Intelligence", "Wits", "Resolve"]
    keys_disciplines = ["Animalism", "Auspex", "Blood Sorcery", "Celerity", "Dominate", "Fortitude", "Obfuscate", "Potence", "Presence"]
    keys_skills = [
        "Athletics", "Brawl", "Craft", "Drive", "Firearms", "Larceny", "Melee", "Stealth", "Survival", 
        "Animal Ken", "Etiquette", "Insight", "Intimidation", "Leadership", "Performance", "Persuasion", "Streetwise", "Subterfuge", 
        "Academics", "Awareness", "Finance", "Investigation", "Medicine", "Occult", "Politics", "Science", "Technology"
    ]
    

    # instance variables
    __clan = ""
    __attributes = {}
    __skills = {}
    __disciplines = {}
    __health = {"total": None, "superficial": None, "aggravated": None}
    __willpower = {"total": None, "superficial": None, "aggravated": None}
    __hunger = None
    __humanity = None

    
    # getter methods for instance variables
    def get_attribute(self, attribute):
        if attribute in self.keys_attributes:
            return self.__attributes.get(attribute)
        else:
            print(f"There is no such attribute: {attribute}")
            return 0
    
    def get_skill(self, skill):
        if skill in self.keys_skills:
            return self.__skills.get(skill, 0)
        else:
            print(f"There is no such skill: {skill}")
            return 0

    def get_discipline(self, discipline):
        if discipline in self.keys_disciplines:
            return self.__disciplines.get(discipline, 0)
        else:
            print(f"There is no such discipline: {discipline}")
            return 0
    
    def get_hunger(self):
        return self.__hunger
    
    def get_humanity(self):
        return self.__humanity
    
    def get_willpower(self):
        total = self.__willpower.get("total", 0)
        superficial = self.__willpower("superficial", 0)
        aggravated = self.__willpower("aggravated", 0)
        if total > (superficial + aggravated):
            current = total - (superficial + aggravated)
        else:
            current = 0
        return current
        

    def __init__(self):
        pass
    

    # constructor method
    @classmethod
    def new_Vampire(cls):
        return cls()


class Vampire_Dices:
    
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
