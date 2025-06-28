from decorator.characterDecorator import CharacterDecorator

class StrengthBuff(CharacterDecorator):
    def __init__(self, character):
        super().__init__(character)
        self._character.forca += 5
        print(f"{self._character.name} recebeu um BUFF de força +5!")

class HealingBuff(CharacterDecorator):
    def __init__(self, character):
        super().__init__(character)
        if self._character.vida==0:
            print(f"{self._character.name} está morto")
        else:
            self._character.vida += 30
            print(f"{self._character.name} recebeu um BUFF de cura +30 de vida!")

class ShieldBuff(CharacterDecorator):
    def __init__(self, character):
        super().__init__(character)
        self._character.defesa += 10
        print(f"{self._character.name} recebeu um BUFF de defesa +10!")
