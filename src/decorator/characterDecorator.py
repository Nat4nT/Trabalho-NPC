class CharacterDecorator:
    def __init__(self, character):
        self._character = character

    def __getattr__(self, attr):
        # Delegar acesso de atributos para o personagem "decorado"
        return getattr(self._character, attr)

    def display_character_info(self):
        self._character.display_character_info()