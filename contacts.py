'''
Inputs:
-Name, phone number, and email for each contact


Processing:
AddressBook class:
- can add a contact
- can search by name
- can display all contacts
- count total number of contacts

Outputs:
Each contact with their info, total number of contacts


'''

class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
    

    def __str__(self):
        return f"{self.name} | {self.number} | {self.email}"
    
class AddressBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_for_contact(self, search):
        result = ""
        for contact in self.contacts:
            if search in contact.name:
                result = result + str(contact) + "\n"
        return result

    def __str__(self):
        result = ""
        for contact in self.contacts:
            result = result + str(contact) + "\n"
        return result
    
    def count_contacts(self):
        return len(self.contacts)

#creating addressbook and contact info
my_book = AddressBook()
jimbo = Contact("Jimbo Lakeswild", "278-555-4356", "jimbo_loves_shrimp@yahoo.com")
petunia = Contact("Petunia Biffard", "756-981-0954", "thanos_lover_69@gmail.com")
chris = Contact("Christopher Cheeseball", "987-345-1234", "thanksgiving_lover_5@msn.com")
#adding contacts to the address book
my_book.add_contact(jimbo)
my_book.add_contact(petunia)
my_book.add_contact(chris)

#calling the search function
name = input("Search contact by name: ")
print(my_book.search_for_contact(name))

#printing all contacts
print(my_book)

#showing how many contacts there are
print(f"Total contacts: {my_book.count_contacts()}")

