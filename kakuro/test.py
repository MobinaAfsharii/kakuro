class Mobina:
    def __init__(self) -> None:
        self.name = "mobina"
        self.age = 20

    def set_age(self, value: int):
        self.age = value

    def __str__(self) -> str:
        return str(self.age)


class Mohammadreza:
    def __init__(self) -> None:
        self.age = 20
        self.mobinas = []

    def set_age(self, value: int):
        self.age = value

    def change_mobina(self, n: int):
        self.mobinas[n].age = 5

    def __repr__(self) -> str:
        return ", ".join([str(i) for i in self.mobinas])


Moh1 = Mohammadreza()

mob1 = Mobina()
mob2 = Mobina()
mob3 = Mobina()

Moh1.mobinas = [mob1, mob2, mob3]
mob2.age = 3
Moh1.change_mobina(0)
print(mob1, mob2, mob3)
