from status.persona_state import CharacterHealthState
import random

class HealthyState(CharacterHealthState):
    def take_damage(self, persona, amount: int):
        persona.vida -= amount
        print(f"{persona.name} tomou {amount} de dano. Vida: {persona.vida}")
        # Possibilidade de sangramento ao ser atacado
        if random.randint(1,10) == random.randint(1,10):
            persona.set_health_state(BleedingState())
        else:
            self.check_transition(persona)

    def heal(self, persona, amount: int):
        persona.vida += amount
        print(f"{persona.name} curou {amount} de vida. Vida: {persona.vida}")
        self.check_transition(persona)

    def get_status_description(self, persona) -> str:
        return f"{persona.name} está **Saudável**."

    def check_transition(self, persona):
        if persona.vida <= 0:
            persona.set_health_state(DeadState())
        elif persona.vida <= 20:
            persona.set_health_state(BleedingState())
        elif persona.vida <= 50:
            persona.set_health_state(WoundedState())


class WoundedState(CharacterHealthState):
    def take_damage(self, persona, amount: int):
        persona.vida -= amount
        print(f"{persona.name} tomou {amount} de dano. Vida: {persona.vida}")
        
        if random.randint(1,5) == random.randint(1,5):
            persona.set_health_state(BleedingState())
        else:
            self.check_transition(persona)

    def heal(self, persona, amount: int):
        persona.vida += amount
        print(f"{persona.name} curou {amount} de vida. Vida: {persona.vida}")
        self.check_transition(persona)

    def get_status_description(self, persona) -> str:
        return f"{persona.name} está **Ferido**."

    def check_transition(self, persona):
        if persona.vida <= 0:
            persona.set_health_state(DeadState())
        elif persona.vida <= 20:
            persona.set_health_state(BleedingState())
        elif persona.vida > 50:
            persona.set_health_state(HealthyState())


class BleedingState(CharacterHealthState):
    def take_damage(self, persona, amount: int):
        persona.vida -= amount
        print(f"{persona.name}  tomou {amount} de dano. Vida: {persona.vida}")
        self.check_transition(persona)

    def heal(self, persona, amount: int):
        reduced_heal = amount // 2
        persona.vida += reduced_heal
        print(f"{persona.name} está sangrando e a cura é reduzida para {reduced_heal}.")
        self.check_transition(persona)

    def get_status_description(self, persona) -> str:

        return f"{persona.name} está **Sangrando**."

    def check_transition(self, persona):
        if persona.vida <= 0:
            persona.set_health_state(DeadState())
        elif persona.vida > 50:
            persona.set_health_state(HealthyState())
        elif persona.vida > 20: # Se a vida está entre 21 e 50
            persona.set_health_state(WoundedState())


class DeadState(CharacterHealthState):
    def take_damage(self, persona, amount: int):
        print(f"{persona.name} (Morto) não pode tomar mais dano.")

    def heal(self, persona, amount: int):
        print(f"{persona.name} (Morto) não pode ser curado.")

    def get_status_description(self, persona) -> str:
        return f"{persona.name} está **Morto**."

    def check_transition(self, persona):
        print(f"{persona.name} (Morto) não pode mudar de estado automaticamente.")

