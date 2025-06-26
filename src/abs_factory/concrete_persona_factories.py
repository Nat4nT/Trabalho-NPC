from abs_persona_factory import CharacterFactory, Race, CharacterClass
from concrete_persona_products import *

# Criando um Factory generico para desaclopar a redundancia.
class GeneralCharacterFactory(CharacterFactory):
    def __init__(self, race_cls, class_cls):
        self.race_cls = race_cls
        self.class_cls = class_cls

    def create_character(self) -> Race:
        return self.race_cls()

    def create_character_class(self) -> CharacterClass:
        return self.class_cls()