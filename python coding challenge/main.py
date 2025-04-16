import sys
from dao.petdaoimpl import PetDAOImpl
from dao.donationdaoimpl import DonationDAOImpl
from dao.adoptioneventdaoimpl import AdoptionEventDAOImpl
from entity.pet import Pet
from entity.dog import Dog
from entity.cat import Cat
from entity.cashdonation import CashDonation
from entity.itemdonation import ItemDonation
from exceptions.invalidpetageexception import InvalidPetAgeException
from exceptions.insufficientfundsexception import InsufficientFundsException
from exceptions.adoptionexception import AdoptionException

def display_menu():
    print("\n=== PetPals - The Pet Adoption Platform ===")
    print("1. View Available Pets")
    print("2. Add a New Pet")
    print("3. Remove a Pet")
    print("4. Record a Donation")
    print("5. View Adoption Events")
    print("6. Register for an Adoption Event")
    print("7. View the Donation")
    print("8. Exit")

def view_available_pets():
    pet_dao = PetDAOImpl()
    pets = pet_dao.get_all_pets()
    if not pets:
        print("No pets available.")
    else:
        print("Available Pets:")
        for pet in pets:
            print(pet)  


def add_new_pet():
    pet_dao = PetDAOImpl()
    try:
        name = input("Enter pet's name: ")
        age = int(input("Enter pet's age: "))
        if age <= 0:
            raise InvalidPetAgeException(f"Invalid age {age}. Age must be a positive number.")
        breed = input("Enter pet's breed: ")
        pet_type = input("Enter pet type (Dog/Cat/Other): ").strip().lower()

        if pet_type == "dog":
            dog_breed = input("Enter specific dog breed: ")
            pet = Dog(name, age, breed, dog_breed)
        elif pet_type == "cat":
            cat_color = input("Enter cat color: ")
            pet = Cat(name, age, breed, cat_color)
        else:
            pet = Pet(name, age, breed)

        pet_dao.add_pet(pet)
        print("Pet added successfully!")

    except InvalidPetAgeException as e:
        print("Error:", e)
    except ValueError:
        print("Invalid input. Please ensure age is a number.")

def remove_pet():
    pet_dao = PetDAOImpl()
    pet_id = input("Enter the pet ID to remove: ")
    try:
        pet_id = int(pet_id)
        pet_dao.remove_pet(pet_id)
        print("Pet removed successfully!")
    except ValueError:
        print("Invalid pet ID.")

def record_donation():
    donation_dao = DonationDAOImpl()
    donor_name = input("Enter donor's name: ")
    donation_type = input("Enter donation type (Cash/Item): ").strip().lower()
    try:
        if donation_type == "cash":
            amount = float(input("Enter donation amount: "))
            if amount < 10:
                raise InsufficientFundsException("Donation must be at least $10.")
            donation_date = input("Enter donation date (YYYY-MM-DD): ")
            donation = CashDonation(donor_name, amount, donation_date)
            donation_dao.record_cash_donation(donation)
        elif donation_type == "item":
            item_type = input("Enter the item donated: ")
            donation = ItemDonation(donor_name, 0, item_type)
            donation_dao.record_item_donation(donation)
        else:
            print("Invalid donation type.")
            return

        print("Donation recorded successfully!")
    except InsufficientFundsException as e:
        print("Error:", e)
    except ValueError:
        print("Invalid input. Please check your entries.")
        
def view_donations():
    donation_dao = DonationDAOImpl()
    donations = donation_dao.get_all_donations()
    if not donations:
        print("No donations recorded yet.")
    else:
        print("Donations Received:")
        for idx, d in enumerate(donations, start=1):
            print(f"{idx}. {d}")

def view_adoption_events():
    adoption_event_dao = AdoptionEventDAOImpl()
    events = adoption_event_dao.get_all_events()
    if not events:
        print("No adoption events found.")
    else:
        print("Adoption Events:")
        for event in events:
            print(f"ID: {event['event_id']} | Name: {event['event_name']} | Date: {event['event_date']}")

def register_for_event():
    adoption_event_dao = AdoptionEventDAOImpl()
    try:
        name = input("Enter your name: ")
        event_id = int(input("Enter event ID to register: "))
        role = input("Enter your role (e.g., Adopter/Shelter): ")
        adoption_event_dao.register_participant(name, event_id, role)
        print("Registration successful!")
    except ValueError:
        print("Invalid event ID.")
    except Exception as e:
        print("Error during registration:", e)

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == '1':
            view_available_pets()
        elif choice == '2':
            add_new_pet()
        elif choice == '3':
            remove_pet()
        elif choice == '4':
            record_donation()
        elif choice == '5':
            view_adoption_events()
        elif choice == '6':
            register_for_event()
        elif choice == '7':
            view_donations()
        elif choice == '8':
            print("Exiting the application. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
