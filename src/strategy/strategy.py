from strategy.interface import ActionStrategy

class MageStrategy(ActionStrategy):
    def attack(self, attacker, target):
        damage = int(attacker.inteligencia * 1.8) - target.defesa
        # declarando um minimo de dano possivel(para nao ser possivel atacar com valor negativo)
        damage = max(damage, 0)
        print(f"{attacker.name} (Mago) lança magia causando {damage} de dano.")
        target.take_damage(damage)
        
    def special(self,attacker,target):
        damage = int(attacker.inteligencia * 2.25) - target.defesa
        damage = max(damage, 0)
        
        # 25% do dano o mago tambem sofre
        burn_life = damage * 0.25
        
        print(f"{attacker.name} sacrificiou {burn_life}  para lançar uma super magia causando {damage} de dano.")
        
        target.take_damage(damage)
        attacker.take_damage(burn_life)


        

class WarriorStrategy(ActionStrategy):
    def attack(self, attacker, target):
        damage = attacker.forca - target.defesa
        damage = max(damage, 0)
        print(f"{attacker.name} (Soldado) golpeia com espada causando {damage} de dano.")
        target.take_damage(damage)
        
    def special(self,attacker,target):
        damage = (attacker.forca * 1.5) - target.defesa
        damage = max(damage, 0)
        print(f"{attacker.name} (Soldado) golpeia forte com espada causando {damage} de dano.")
        target.take_damage(damage)

        
    

class AdventurerStrategy(ActionStrategy):
    def attack(self, attacker, target):
        damage = (attacker.forca ) - target.defesa
        damage = max(damage, 0)
        print(f"{attacker.name} (Aventureiro) golpeia com a adaga causando {damage} de dano.")
        target.take_damage(damage)
    
    def special(self,attacker,target):
        qtd_ataques =  attacker.agilidade / 2
        damage_total = 0
        qtd_ataques = int(qtd_ataques)
        for ataque in range(qtd_ataques):
            damage = (attacker.forca * 0.75) 
            damage = max(damage, 0)
            damage_total +=damage
            target.take_damage(damage)
            
        print(f"{attacker.name} (Aventureiro) golpeia multiplas vezes com a adaga causando {damage_total} de dano.")
        
    
