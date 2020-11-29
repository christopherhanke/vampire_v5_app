import json
from random import randint

class Vampire(json.JSONEncoder):
    # static dictionary for the clans and their clan-disciplines
    clans = {
        "Brujah": ["Celerity", "Potence", "Presence"],
        "Gangrel": ["Animalism", "Fortitude", "Protean"],
        "Malkavian": ["Auspex", "Dominate", "Obfuscate"],
        "Nosferatu": ["Animalism", "Obfuscate", "Potence"],
        "Toreador": ["Auspex", "Celerity", "Presence"],
        "Tremere": ["Auspex", "Blood Sorcery", "Dominate"],
        "Ventrue": ["Dominate", "Fortitude", "Presence"],
        "Caitiff": []
    }
    
    # static key lists
    keys_attributes = ["Strength", "Dexterity", "Stamina", "Charisma", "Manipulation", "Composure", "Intelligence", "Wits", "Resolve"]
    keys_disciplines = ["Animalism", "Auspex", "Blood Sorcery", "Celerity", "Dominate", "Fortitude", "Obfuscate", "Potence", "Presence", "Protean"]
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
    def get_clan(self):
        return self.__clan
    
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
    
    def get_health(self):
        total = self.__health.get("total", 0)
        superficial = self.__health.get("superficial", 0)
        aggravated = self.__helath.get("aggravated", 0)
        if total > (superficial + aggravated):
            current = total - (superficial + aggravated)
        else:
            current = 0
        return current
    

    # setter methods for instance variables
    def set_attribute(self, attribute, value):
        """
        attribute = key for attribute
        value = value of attribute
        """
        if attribute in self.keys_attributes:
            self.__attributes[attribute] = value
        else:
            print(f"{attribute} is not valid")
    
    def set_skill(self, skill, value):
        """
        skill = key for skill
        value = value of the skill
        """
        if skill in self.keys_skills:
            self.__skills[skill] = value
        else:
            print(f"{skill} is not valid")
    
    def set_discipline(self, discipline, value):
        """
        discipline = key for discipline
        value = value of the discipline
        """
        if discipline in self.keys_disciplines:
            self.__disciplines[discipline] = value
        else:
            print(f"{discipline} is not valid")
    
    def set_clan(self, clan):
        """
        clan = clan name
        """
        if clan in self.clans.keys():
            self.__clan = clan
        else:
            print(f"{clan} is not valid")


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

    def rouse_check(self):
        check = self.__d10()
        if check < 6 and self.get_hunger() < 5:
            self.__hunger += 1
        elif check < 6 and self.get_hunger >= 5:
            raise Exception()


    # setting __init__ for constructors
    def __init__(self, **kwargs):
        if "file" in kwargs:
            #TODO
            print(f"File to get... {kwargs['file']}")
        else:
            print("Embrace begins... ")
    

    # classmethods for constructors
    @classmethod
    def new_Vampire(cls):
        """
        Constructor: initialize a new Vampire
        """
        return cls()

    @classmethod
    def new_Vampire_from_file(cls, file):
        """
        Constructor: initialize a Vampire from file
        file contains path to file
        """
        return cls(file=file)
    