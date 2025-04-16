from abc import ABC, abstractmethod

class PetDAO(ABC):
    @abstractmethod
    def get_all_pets(self):
        pass

    @abstractmethod
    def add_pet(self, pet):
        pass

    @abstractmethod
    def remove_pet(self, pet_id):
        pass
