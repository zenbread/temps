
class Temperature():

    def __init__(self, C=None, F=None, K=None, D=None):
        self.C = C
        self.F = F
        self.K = K
        self.D = D
        if C is not None or F is not None or K is not None or D is not None:
            self._GetTemps()
            self._RoundTemps()

    def __add__(self, other):
        return Temperature(self.C + other.C)

    def _GetTemps(self):
        if self.C is not None:
            self.C = float(self.C)
            self.D = (100 - self.C) * float(3) / float(2)
            self.F = 212 - self.D * float(6) / float(5)
            self.K = 373.15 - self.D * float(2) / float(3)
        elif self.F is not None:
            self.F = float(self.F)
            self.D = (212 - self.F) * float(5) / float(6)
            self.K = 373.15 - self.D * float(2) / float(3)
            self.C = 100 - self.D * float(2) / float(3)
        elif self.K is not None:
            self.K = float(self.K)
            self.D = (373.15 - self.K) * float(3) / float(2)
            self.C = 100 - self.D * float(2) / float(3)
            self.F = 212 - self.D * float(6) / float(5)
        elif self.D is not None:
            self.D = float(self.D)
            self.C = 100 - self.D * float(2) / float(3)
            self.F = 212 - self.D * float(6) / float(5)
            self.K = 373.15 - self.D * float(2) / float(3)

    def _RoundTemps(self):
        for x in self.__dict__.keys():
            self.__dict__[x] = round(self.__dict__[x], 2)
