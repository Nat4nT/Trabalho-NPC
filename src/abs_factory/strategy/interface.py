from abc import ABC, abstractmethod

class ActionStrategy(ABC):
    @abstractmethod
    def attack(self, attacker, target):
        pass
    
    @abstractmethod
    def special(self,attacker,targuet):
        pass
