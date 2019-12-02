class Leah:
    def __init__(self,tiredness=0,hungerLevel=0,hateFlight=0,luggageWeight=0,missShahroz=0):
        self.tiredness = tiredness
        self.hungerLevel = hungerLevel
        self.hateFlight = hateFlight
        self.luggageWeight = luggageWeight
        self.missShahroz = missShahroz

    def willSheCry(self):
        cryPts = self.tiredness + self.hungerLevel + self.hateFlight + self.luggageWeight + self.missShahroz
        cryThreshold = 75 + 50 + 85 + 70 + 60
        if cryPts > cryThreshold:
            return 'she will cry :"('
        return 'she will not cry'

if __name__ == '__main__':
    leah = Leah(74,40,90,60,100)
    print(leah.willSheCry())
