from levels.level_base import Level

class Level1(Level):
    def __init__(self, player):
        super().__init__(player)
        self.load_background("level1_bg.png")
        self.create_platforms([
            (300, self.height - 100, 100, 20),
            (600, self.height - 150, 150, 20),
            (1000, self.height - 100, 100, 20),
            (1300, self.height - 200, 150, 20),
            (1800, self.height - 250, 200, 20),
        ])