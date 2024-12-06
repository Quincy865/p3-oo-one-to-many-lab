class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Returns a list of pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Associates a pet with this owner."""
        if not isinstance(pet, Pet):
            raise Exception("The provided pet is not an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        """Returns a sorted list of the owner's pets by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = [] 

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.pet_type = pet_type
        if owner and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self.owner = owner
        Pet.all.append(self)
