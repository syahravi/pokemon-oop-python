#buat class (objek) Pokemon
class Pokemon:
    def __init__(self, nama, tipe, hp):
        self.nama = nama
        self.tipe = tipe
        self.hp = hp
        self.max_hp = hp

    #tugas print(objek)
    def __str__(self):
        return f"{self.nama} ({self.tipe})\n\t{self.hp}/{self.max_hp} HP."

    #tugas nambah hp
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 5
            print(f"{self.nama} has now {self.hp} HP.")
        else:
            print(f"{self.nama} HP is fully.")

    #alur pertarungan dan hasil kemenangan
    def battle(self, vs):
        print("---#_<")
        print(self, "\n---\n", vs)
        print()
        print("---#_<")
        print("Battle: ", self.nama,"vs", vs.nama)
        result = self.typewheel(self.tipe, vs.tipe)
        print(f"\t{self.nama} fought {vs.nama},\n\t\tand the result is a {result}")

        if result == 'lose':
            self.hp -= 20
            print(f"{self.nama} lost and now has {self.hp} HP.")
        elif result == 'win':
            vs.hp -= 20
            print(f"{vs.nama} lost and now has {vs.hp} HP.")

        print()
        print("---#_<")
        print(self, "\n---\n", vs)

    #menentukan kemenangan
    @staticmethod
    def typewheel(v1, v2):
        result = {0: "lose", 1: "win", -1: "te"}

        #kondisi kemenangan
        game_type = {"water": 0, "fire": 1, "grass": 2}

        #matrix menang-kalah
        wl_matrix = [
                [-1, 1, 0], #water
                [0, -1, 1], #fire
                [1, 0, -1] #grass
            ]

        #deklarasi kemenangan
        wl_result = wl_matrix[game_type[v1]][game_type[v2]]

        return result[wl_result]

if __name__ == "__main__":
    ravi = Pokemon("Ravi", "grass", 100)
    vira = Pokemon("Vira", "water", 200)
"""
CONCEPTS
========
- Object-Oriented Programming in Python
- game logic
- instance methods
- `@staticmethod`
- self, other
- __init__, __str__
- if __name__ == '__main__'
"""
