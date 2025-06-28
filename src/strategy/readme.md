trategy permite definir uma família de algoritmos, encapsular cada um e torná-los intercambiáveis. Permite que o algoritmo varie independentemente dos clientes que o utilizam.

Como está no código:
Cada classe de personagem tem uma estratégia de ataque diferente (MageStrategy, WarriorStrategy, AdventurerStrategy), definindo como os ataques e especiais são realizados, encapsulando essa lógica fora das classes principais.

Arquivos principais:

    strategy/interface.py (interface)

    strategy/strategy.py (implementações)