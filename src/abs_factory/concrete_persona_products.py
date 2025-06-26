from abs_persona_factory import Race, CharacterClass
from strategy.strategy import *
# ---  Raças ---
class Human(Race):
    def __init__(self):
        self.vida = 100
        self.forca = 10
        self.agilidade = 5
        self.agilidade_original = 5
        self.inteligencia = 8
        self.defesa = 8
        self.raca = 'Humano'

class Orc(Race):
    def __init__(self):
        self.vida = 150
        self.forca = 30
        self.agilidade = 3
        self.agilidade_original = 3
        self.inteligencia = 2
        self.defesa = 15
        self.raca = 'Orc'

# ---  Classes ---
# Definindo os novos atributos apartir da classe
class Mage(CharacterClass):
    def define_class(self, persona: dict) -> dict:
        persona.vida -= 10
        persona.forca += 3
        persona.agilidade_original += 0
        persona.inteligencia += 5
        persona.defesa -= 3
        persona.classe = self.get_class_name()
        persona.attack = self.attack_strategy()
        
        return persona
    
    def get_class_name(self) -> str:
        return 'Mago'
    
    def attack_strategy(self):
        return MageStrategy()

class Warrior(CharacterClass): 
    def define_class(self, persona: dict) -> dict:
        persona.vida += 50
        persona.forca += 10
        persona.agilidade -= 1
        persona.agilidade_original -= 1
        persona.inteligencia += 1
        persona.defesa += 4
        persona.classe = self.get_class_name()
        persona.attack = self.attack_strategy()
        return persona

    def get_class_name(self) -> str:
        return 'Soldado'
    
    def attack_strategy(self):
        return WarriorStrategy()

class Adventurer(CharacterClass):
    def define_class(self, persona: dict) -> dict:
        persona.vida += 20
        persona.forca += 10
        persona.agilidade += 8
        persona.agilidade_original += 8
        persona.inteligencia += 3
        persona.defesa += 2
        persona.classe = self.get_class_name()
        persona.attack = self.attack_strategy()
        
        return persona

    def get_class_name(self) -> str:
        return 'Aventureiro'
    
    def attack_strategy(self):
        return AdventurerStrategy()
