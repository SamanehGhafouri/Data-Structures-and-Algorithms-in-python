class Table:

    def __init__(self, height:int, legs:int, material:str):
        self.height = height
        self.legs = legs
        self.material = material

    def __eq__(self, other: 'Table'):
        b_h = self.height == other.height
        b_l = self.legs == other.legs
        b_m = self.material == other.material
        return b_h and b_l and b_m

    def __repr__(self):
        desc = f"<<height : {self.height}, legs: {self.legs}, material: {self.material}>>"

        return desc

    def __gt__(self, other: 'Table'):
        return self.height > other.height

    def __lt__(self, other: 'Table'):
        return self.height < other.height




if __name__ == '__main__':
    tabel_1 = Table(18, 4, 'steel')
    tabel_2 = Table(20, 6, 'wood')
    tabel_3 = Table(18, 4, 'glass')
    # compare1 = tabel_1.compare(tabel_2)
    # # print(compare1)
    # compare2 = tabel_1.compare(tabel_3)
    # print(compare2)
    print(tabel_1 == tabel_2, tabel_1, tabel_2)
    print(tabel_1 == tabel_3, tabel_1, tabel_3)
    print(tabel_1 == tabel_1, tabel_1, tabel_1)
    print(tabel_1 > tabel_2, tabel_1.height, tabel_2.height)
    print(tabel_2 > tabel_1, tabel_1.height, tabel_2.height)
    print(tabel_1 < tabel_2, tabel_1.height, tabel_2.height)

