class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I am a musician"

    def __repr__(self):
        return f"{type(self).__name__}('{self.name}')"

    def get_instrument(self):
        pass

    def play_solo(self):
        pass


class Guitarist(Musician):
    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):
    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


class Band:
    all_bands = []
    print('this is my bands', all_bands)

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.all_bands.append(self)

    def __str__(self):
        return f"{self.name} band"

    def __repr__(self):
        return f"Band('{self.name}')"

    def add_musician(self, musician):
        if isinstance(musician, Musician):
            self.members.append(musician)

    def play_solos(self):
        solos = [musician.play_solo() for musician in self.members]
        return solos

    @classmethod
    def to_list(cls):
        return cls.all_bands



