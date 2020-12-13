import json
from json import JSONEncoder, JSONDecoder
from random import randint

class Vampire():
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
    __specialties = {}
    __disciplines = {}
    __health = {"total": 0, "superficial": 0, "aggravated": 0}
    __willpower = {"total": 0, "superficial": 0, "aggravated": 0}
    __hunger = None
    __humanity = None
    __flaws = None
    __name = ""


    # serialize method to encode instance date to JSON
    def serialize(self):
        vampire = dict()
        vampire["name"] = self.__name
        vampire["clan"] = self.__clan
        vampire["attributes"] = self.__attributes
        vampire["skills"] = self.__skills
        vampire["specialties"] = self.__specialties
        vampire["disciplines"] = self.__disciplines
        vampire["health"] = self.__health
        vampire["willpower"] = self.__willpower
        vampire["hunger"] = self.__hunger
        vampire["humanity"] = self.__humanity
        vampire["flaws"] = self.__flaws
        return vampire
    

    # deserialize method to set data from JSON to class instance
    def deserialize(self, data):
        """
        data = JSON string with serialized data of a vampire instance
        """
        #TODO - implement deserialize of all keys

        data = dict(data)
        for key in data.keys():
            if key == "name":
                self.set_name(data.get(key))

            elif key == "clan":
                self.set_clan(data.get(key))

            elif key == "attributes":
                self.__attributes = data.get(key)

            elif key == "skills":
                skls = list(data.get(key).keys())
                for skl in skls:
                    self.set_skill(skl, data.get(key).get(skl))

            elif key == "specialties":
                specs = list(data.get(key).keys())
                for spec in specs:
                    for s in data.get(key).get(spec):
                        self.set_specialty(spec, s)

            elif key == "disciplines":
                dscs = list(data.get(key).keys())
                for dsc in dscs:
                    self.set_discipline(dsc, data.get(key).get(dsc))
                    
            elif key == "health":
                keys = list(data.get(key).keys())
                for k in keys:
                    if k in self.__willpower.keys():
                        self.__willpower[key] = data.get(key).get(k)

            elif key == "willpower":
                keys = list(data.get(key).keys())
                for k in keys:
                    if k in self.__willpower.keys():
                        self.__willpower[key] = data.get(key).get(k)
                
            elif key == "hunger":
                if not self.__hunger:
                    self.set_hunger(data.get(key))
                
            elif key == "humanity":
                if not self.__humanity:
                    self.set_humanity(data.get(key))

            elif key == "flaws":
                pass
    

    # getter methods for instance variables
    def get_clan(self):
        return self.__clan
    

    def get_attribute(self, attribute):
        """
        return value of attribute
        if attribute is not initialized return 0
        if value of attribute is invalid return None
        """
        if attribute in self.__attributes.keys():
            return self.__attributes.get(attribute)
        elif attribute in self.keys_attributes:
            return 0
        else:
            print(f"There is no such attribute: {attribute}")
            return None
    

    def get_skill(self, skill):
        if skill in self.keys_skills:
            return self.__skills.get(skill, 0)
        else:
            print(f"There is no such skill: {skill}")
            return 0
    
    def get_specialty(self, skill):
        """
        test if skill has specialty
        returns list if there is specialty
        """
        return self.__specialties.get(skill)


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
        total = self.__willpower.get("total")
        superficial = self.__willpower.get("superficial")
        aggravated = self.__willpower.get("aggravated")
        if total > (superficial + aggravated):
            return total - (superficial + aggravated)
        else:
            return 0
    # TODO - make up mind if total health is reasonable or if list of all three is of more use
    

    def get_health(self):
        total = self.__health.get("total")
        superficial = self.__health.get("superficial")
        aggravated = self.__health.get("aggravated")
        if total > (superficial + aggravated):
            return total - (superficial + aggravated)
        else:
            return 0
    # TODO - make up mind if total health is reasonable or if list of all three is of more use
    

    def get_name(self):
        return self.__name
    

    def get_specialties_keys(self):
        return list(self.__specialties.keys())

    
    def get_discipline_keys(self):
        return list(self.__disciplines.keys())
    

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
    

    def set_specialty(self, skill, specialty):
        """
        skill = key for skill
        specialty = specialty in skill
        """
        if not skill in self.__skills:
            raise Exception(f"{skill} is not skilled yet.")
        else:
            if not self.__specialties.get(skill, None):
                self.__specialties[skill] = []
            
            self.__specialties[skill].append(specialty)
    

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
    

    def set_name(self, name):
        """
        name = Name of the Vampire
        """
        self.__name = name
    

    def set_hunger(self, value):
        """
        value = hunger value
        use this function only for initialization
        """
        self.__hunger = value
    

    def set_humanity(self, value):
        """
        value = humanity value
        use this function only for initialization
        """
        self.__humanity = value
    

    def set_health(self):
        self.__health["total"] = self.__attributes.get("Stamina") + 3


    def set_willpower(self):
        self.__willpower["total"] = self.__attributes.get("Composure") + self.__attributes.get("Resolve")

    # dice functions
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
        """
        make rouse check.
        Increases hunger if check fails and returns True.
        Throws Exception if rouse check isn't possible (e.g. Hunger is at five).
        Returns False if nothing happend.
        """
        check = self.__d10()
        if hunger >= 5:
            raise Exception()
        elif check < 6 and self.get_hunger() < 5:
            self.__hunger += 1
            return True
        else:
            return False
        

    
    # CONSTRUCTORS
    # setting __init__ for constructors
    def __init__(self, **kwargs):
        if "file" in kwargs:
            try:
                with open(kwargs.get("file"), "r") as file:
                    data = json.loads(file.read())
                    self.deserialize(data)
            except FileNotFoundError:
                print("File not found.")
        
        else:
            pass
    

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


class Vampire_Encode(JSONEncoder):
    
    def default(self, o):
        return o.serialize()
