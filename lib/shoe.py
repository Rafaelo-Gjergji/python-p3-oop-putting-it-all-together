class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    def repair(self):
        print("The shoe has been repaired.")
        self.condition = "New"

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    def set_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.size = size