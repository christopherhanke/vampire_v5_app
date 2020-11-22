from random import randint

class Vampire:
    clans = ["Brujah", "Gangrel", "Malkavian", "Nosferatu", "Toreador", "Tremere", "Ventrue"]
    
    attributes = {
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
    
    skills = {
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

    disciplines = {
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

