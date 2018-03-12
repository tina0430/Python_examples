class Robot :
    name = '건담'
    energy = 50
    def attack(self):
        self.energy -= 10
        return '발차기, 남은 에너지 ' + str(self.energy)