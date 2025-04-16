import pyodbc
from dao.petdao import PetDAO
from util.dbconnutil import DBConnUtil
from entity.pet import Pet
from entity.dog import Dog
from entity.cat import Cat

class PetDAOImpl(PetDAO):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def get_all_pets(self):
        pets = []
        cursor = self.conn.cursor()
        cursor.execute("select * from pets")
        rows = cursor.fetchall()
        for row in rows:
            if row.type == 'Dog':
                pet = Dog(row.name, row.age, row.breed, row.dog_breed)
            elif row.type == 'Cat':
                pet = Cat(row.name, row.age, row.breed, row.cat_color)
            else:
                pet = Pet(row.name, row.age, row.breed)
            pet.pet_id = row.pet_id 
            pets.append(pet)
        return pets

    def add_pet(self, pet):
        cursor = self.conn.cursor()
        if isinstance(pet, Dog):
            cursor.execute("insert into pets (name, age, breed, type, dog_breed) values (?, ?, ?, ?, ?)",
                           (pet.name, pet.age, pet.breed, 'Dog', pet.dog_breed))
        elif isinstance(pet, Cat):
            cursor.execute("insert into pets (name, age, breed, type, cat_color) values (?, ?, ?, ?, ?)",
                           (pet.name, pet.age, pet.breed, 'Cat', pet.cat_color))
        else:
            cursor.execute("insert into pets (name, age, breed, type) values (?, ?, ?, ?)",
                           (pet.name, pet.age, pet.breed, 'Pet'))
        self.conn.commit()

    def remove_pet(self, pet_id):
        cursor = self.conn.cursor()
        cursor.execute("delete from pets where pet_id = ?", (pet_id,))
        self.conn.commit()
