import json
from builder.characterBuilder import CharacterBuilder
from absFactory.concretePersonaProducts import Human,Orc,Mage,Adventurer,Warrior
from decorator.buffs import StrengthBuff, HealingBuff, ShieldBuff

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
            character_data = data.get('Players', [])
        
        created_characters = [] # Lista para guardar os personagens criados
        character_player = [] # Lista para guardar os personagens criados

        # Rodando para todos os index em Personas no json criado.
        for persona_info in personas_data:
            nome = persona_info.get("nome")
            raca = persona_info.get("raca")
            classe = persona_info.get("classe")

            race_cls = RACE_MAP.get(raca)
            class_cls = CLASS_MAP.get(classe)

            if race_cls and class_cls:
                builder = CharacterBuilder(nome, race_cls, class_cls)
                final_character = builder.build()
            
                created_characters.append(final_character)
            else:
                print("erro na leitura do arquivo")

        #Teste para ver se as funçoes estao funcionais
        if created_characters:
            exit
            hero = created_characters[1] # Pegando a cobaia
            vilan = created_characters[0] # Pegando a cobaia
            
            StrengthBuff(hero)
            HealingBuff(hero)
            ShieldBuff(hero)

            hero.attack.special(hero,vilan)
            
            hero.display_character_info()
            vilan.display_character_info()
            
            hero.attack.attack(hero,vilan)
            vilan.display_character_info()
            
            # Buffando personagem para transitar entre os status 
            HealingBuff(vilan)
            ShieldBuff(vilan)
            vilan.display_character_info()
            
            hero.attack.attack(hero,vilan)
            vilan.display_character_info()
            
            hero.attack.special(hero,vilan)
            vilan.display_character_info()
            # Tentando curar personagem morto
            HealingBuff(vilan)
            
        # Criando personagens gerados no script
        for characters_info in character_data:
            nome = characters_info.get("nome")
            raca = characters_info.get("raca")
            classe = characters_info.get("classe")

            race_cls = RACE_MAP.get(raca)
            class_cls = CLASS_MAP.get(classe)

            if race_cls and class_cls:
                builder = CharacterBuilder(nome, race_cls, class_cls)
                final_character = builder.build()
            
                character_player.append(final_character)
        
        # Mostrando dados do player criado
        for player in character_player:
            player.display_character_info()

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
if __name__ == "__main__":
    main()