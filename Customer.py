import random


class Customer:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank  # rank of the customer

        # Determine hair_cut_time based on rank
        if rank == "Officer":
            self.hair_cut_time = random.randint(4, 6)
        elif rank == "Sargent":
            self.hair_cut_time = random.randint(2, 4)
        elif rank == "Private":
            self.hair_cut_time = random.randint(1, 3)

