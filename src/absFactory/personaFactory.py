from absFactory.concretePersonaProducts import Race, CharacterClass

# Importa as interfaces e classes concretas do padrão State
from state.personaState import CharacterHealthState
from state.concretePersonaState import HealthyState,WoundedState,BleedingState

class PlayerCharacter:
    # Criando Player/Persona , passando o nome, raça e classe.
    def __init__(self, name: str, raca: Race, classe: CharacterClass):
        # Setando o nome do persona
        self.name = name
        
        # Adicionando valores ao Dicinario conforme a Raça ( definido em concrete_persona_product).
        self.vida = raca.vida
        self.forca = raca.forca
        self.agilidade = raca.agilidade
        self.agilidade_original = raca.agilidade
        self.inteligencia = raca.inteligencia
        self.defesa = raca.defesa
        self.raca = raca.raca

        # Setando os atributos conforme a Classe ( definido em concrete_persona_product)
        # Classe é uma referencia ao Objeto classe, passado em main 
        classe.define_class(self)

        # --- Integração do Padrão State ---
    
        self._health_state: CharacterHealthState = HealthyState() # Estado de saúde inicial

    def set_health_state(self, new_state: CharacterHealthState):
        
        # Verifica se o status de saude foi alterado, para realizar a logica apenas uma vez
        if type(self._health_state) != type(new_state):
            # Restaura agilidade original antes de aplicar o novo efeito
            self.agilidade = self.agilidade_original

            if isinstance(new_state, WoundedState):
                self.agilidade -= 3
            elif isinstance(new_state, BleedingState):
                self.agilidade = self.agilidade_original / 2  # ou self.agilidade_original * 0.5
                
        #Define o novo estado de saúde do personagem.
        self._health_state = new_state

    def take_damage(self, amount):
        #Delega a lógica de tomar dano para o estado de saúde atual.
        self._health_state.take_damage(self, amount)
        # Garante que a vida não caia abaixo de zero
        if self.vida < 0:
            self.vida = 0

    def heal(self, amount: int):
        #Delega a lógica de cura para o estado de saúde atual.
        self._health_state.heal(self, amount)
        
        # Usando o valor de vida após a aplicação da classe como máximo
        max_vida_initial = getattr(self,'vida_inicial_calculada', self.vida) 
       
        if self.vida > max_vida_initial:
            self.vida = max_vida_initial

    def get_current_health_status(self) -> str:
        # Obtém a descrição do estado de saúde atual.
        return self._health_state.get_status_description(self)

    def display_character_info(self):
        #Exibe todas as informações do personagem.
        print(f"--- Informações de {self.name} ---")
        for key, value in self.__dict__.items():
            if key not in ['_health_state',"agilidade_original",'attack']:  # pula objetos , ou dados utilizados apenas para logica.
                print(f"{key.capitalize()}: {value}")
        print(f"Status de Saúde: {self.get_current_health_status()}")
        print("-" * 25)