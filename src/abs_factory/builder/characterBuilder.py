from concrete_persona_factories import GeneralCharacterFactory
from persona_factory import PlayerCharacter  # sua classe de personagem

class CharacterBuilder:
    def __init__(self, nome, race_cls, class_cls):
        self.nome = nome
        self.race_cls = race_cls
        self.class_cls = class_cls

    #Builder para criar PlayerCharacter via fábrica genérica.
    def build(self):
        # Cria e retorna o personagem com raça e classe definidas.
        factory = GeneralCharacterFactory(self.race_cls, self.class_cls)
        race_instance = factory.create_character()
        class_instance = factory.create_character_class()
        # class_instance.define_class(race_instance)  # ajusta atributos na raça

        # Cria o player
        # Utiliza o padrao builder
        player = PlayerCharacter(self.nome, race_instance, class_instance)


        return player
