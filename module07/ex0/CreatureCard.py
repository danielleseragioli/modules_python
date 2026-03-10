def CreatureCard(Card):
    def __init__(self, attack: str, health: str):
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        