from abc import ABC,abstractmethod

# --- Abstract Products (Raças) ---
class Race(ABC):
    @abstractmethod
    def __init__(self):
        self.nivel = 1
        self.vida = 0
        self.nome = ""
        self.forca = 0
        self.agilidade = 0
        self.inteligencia = 0
        self.defesa = 0
        self.raca = ""

# --- Abstract Products (Classes) ---
class CharacterClass(ABC):
    @abstractmethod
    def define_class(self,character_attr):
        pass

    @abstractmethod
    def get_class_name(self) -> str:
        pass
    
    @abstractmethod
    def attack_strategy(self):
        pass

# --- Abstract Factory ---
class CharacterFactory(ABC):
    @abstractmethod
    def create_character(self) -> Race: # A fábrica cria uma instância de Race 
        pass

    @abstractmethod
    def create_character_class(self) -> CharacterClass: # E uma instância de CharacterClass 
        pass