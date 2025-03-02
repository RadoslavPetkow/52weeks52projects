from levels.level_base import Level

class Level2(Level):
    def __init__(self, player):
        super().__init__(player)
        self.load_background("level2_bg.png")
        self.create_platforms([
            (400, self.height - 150, 120, 20),
            (800, self.height - 180, 160, 20),
            (1200, self.height - 220, 180, 20),
            (1600, self.height - 250, 200, 20),
            (2100, self.height - 300, 250, 20),
        ])