# 

class NumberManager:
    # Class to handle Number initialization, insertion, and searching
    def __init__(self):
        self.numbers = []

    def insert_number(self, num: int):
        # Inserts a number into the collection
        self.numbers.append(num)

    def search_number(self, x: int) -> int:
        # seraches for the enter number in collection
        # writens index if found, or -1 otherwise 
        
        try:
            return self.numbers.index(x) + 1
        except ValueError:
            return -1
        