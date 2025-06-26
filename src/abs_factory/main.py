import json
from persona_factory import PlayerCharacter
from builder.characterBuilder import CharacterBuilder
from concrete_persona_factories import GeneralCharacterFactory
from concrete_persona_products import Human,Orc,Mage,Adventurer,Warrior


RACE_MAP = {
    "Humano": Human,
    "Ogro": Orc,
}
CLASS_MAP = {
    "Aventureiro": Adventurer,
    "Soldado": Warrior,
    "Mago": Mage,
}
# --- Lógica Principal: Ler JSON e Orquestrar a Criação ---
def main():
    try:
        with open('script.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            personas_data = data.get('Personas', [])
        
        created_characters = [] # Lista para guardar os personagens criados

        # Rodando para todos os index em Personas no json criado.
        for persona_info in personas_data:
            nome = persona_info.get("nome")
            raca = persona_info.get("raca")
            classe = persona_info.get("classe")

            race_cls = RACE_MAP.get(raca)
            class_cls = CLASS_MAP.get(classe)

            if race_cls and class_cls:
                factory = GeneralCharacterFactory(race_cls, class_cls)
                race_instance = factory.create_character()
                class_instance = factory.create_character_class()

                final_character = PlayerCharacter(nome, race_instance, class_instance)
                # final_character.display_character_info()
                created_characters.append(final_character)
            else:
                print("erro na leitura do arquivo")

        #Teste para ver se as funçoes estao funcionais
        if created_characters:
            hero = created_characters[0] # Pegando a cobaia
            vilan = created_characters[1] # Pegando a cobaia
            # print(f"\nStatus inicial de {hero.name}: {hero.get_current_health_status()}")

            hero.attack.special(hero,vilan)
            hero.display_character_info()
            vilan.display_character_info()
            
            """hero.take_damage(30)
            hero.display_character_info()
            print(f"Status atual de {hero.name}: {hero.get_current_health_status()}")

            hero.take_damage(30)
            hero.display_character_info()
            print(f"Status atual de {hero.name}: {hero.get_current_health_status()}")

            hero.take_damage(20)
            hero.display_character_info()
            print(f"Status atual de {hero.name}: {hero.get_current_health_status()}")

            hero.take_damage(15)
            hero.display_character_info()
            print(f"Status atual de {hero.name}: {hero.get_current_health_status()}")

            hero.take_damage(10)
            hero.display_character_info()
            print(f"Status atual de {hero.name}: {hero.get_current_health_status()}")
            hero.take_damage(25)
            hero.display_character_info()
            print(f"Status atual de {hero.name}: {hero.get_current_health_status()}")

            print("\n--- Tentando curar personagem morto ---")
            hero.heal(50)
            hero.display_character_info()
            print(f"Status atual de {hero.name}: {hero.get_current_health_status()}")"""
        #rodando apenas uma vez
        exit
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        
    builder = CharacterBuilder("Gandalf", Human, Mage)
    gandalf = builder.build()
    gandalf.display_character_info()

if __name__ == "__main__":
    main()