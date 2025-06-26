from abc import ABC, abstractmethod

class CharacterHealthState(ABC):
    # Interface abstrata para os estados de saúde do personagem.
    @abstractmethod
    def take_damage(self, persona, amount: int):
        # Lógica para tomar dano .
        pass

    @abstractmethod
    def heal(self, persona, amount: int):
        # Lógica para cura .
        pass

    @abstractmethod
    def get_status_description(self, persona) -> str:
        # Retorna uma descrição do estado atual 
        pass

    @abstractmethod
    def check_transition(self, persona):
        # Verifica se há necessidade de transitar para outro estado.
        pass