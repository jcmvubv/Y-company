from beautifultable import BeautifulTable


class Contact_Book:
    def __init__(self):
        self.__data = {}
    
    def addContact(self, name = None, address = None, phone_number = None, email = None):
        if name != None and address != None and phone_number != None and email != None:
            if phone_number not in self.__data:
                self.__data[phone_number] = [name, address, phone_number, email]
                print("Added successfully")
            else:
                print("Number already exists")
        else:
            print("Please enter all the values")


    def deleteContact(self, phone_number = None):
        if phone_number != None:
            if phone_number in self.__data:
                del self.__data[phone_number]
                print("Deleted successfully")
            else:
                print("Phone number does not exists in the database")
        else:
            print("Please enter phone number")

    def editContact(self, name = None, address = None, phone_number = None, email = None):
        if phone_number != None and phone_number in self.__data:
            lst_info = self.__data[phone_number]
            if name != None:
                lst_info[0] = name
            if address != None:
                lst_info[1] = address
            if email != None:
                lst_info[3] = email
            self.__data[phone_number] = lst_info
            print("Data updated successfully")
        else:
            print("Phone number does not exists in the database")


    def searchContact(self, query = None, sort_field = None):
        if query != None:
            search_arr = []
            for key, val in self.__data.items():
                search_arr.append(val + [" ".join(val)])
                        
            result = set()
            for word in query.lower().split():
                for i in range(len(search_arr)):
                    if word in search_arr[i][-1].lower():
                        result.add(i)
            
            ans = []
            for i in result:
                ans.append(search_arr[i][:-1])
            
            indx = 0
            if sort_field == "name":
                indx = 0
            if sort_field == "address":
                indx = 1
            if sort_field == "phone_number":
                indx = 2
            if sort_field == "email":
                indx = 3
            ans.sort(key= lambda x : x[indx])

            self.viewContact(ans)
        else:
            return []

    
    def viewContact(self, data):
        table = BeautifulTable()
        for child_data in data:
            table.rows.append(child_data)

        table.rows.header = [str(i) for i in range(1, len(data) + 1)]
        table.columns.header = ["name", "address", "phone_number", "email"]
        print(table)

    def console(self):
        while True:
            try:
                print("\n1. Add Contact\n2. Delete Contact\n3. Edit Contact\n4. Search Contact\n5. View Contacts\n6. Stop")
                n = int(input("Enter your options: "))
                if n == 1:
                    name = input("Name: ")
                    address = input("Address: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    if len(name) == 0:
                        name = None
                    if len(address) == 0:
                        address = None
                    if len(phone_number) == 0:
                        phone_number = None
                    if len(email) == 0:
                        email = None
                    self.addContact(name, address, phone_number, email)

                if n == 2:
                    phone_number = input("Phone Number: ")
                    if len(phone_number) == 0:
                        phone_number = None
                    self.deleteContact(phone_number)
                
                if n == 3:
                    name = input("Name: ")
                    address = input("Address: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    if len(name) == 0:
                        name = None
                    if len(address) == 0:
                        address = None
                    if len(phone_number) == 0:
                        phone_number = None
                    if len(email) == 0:
                        email = None
                    self.editContact(name, address, phone_number, email)
                
                if n == 4:
                    query = input("Search: ")
                    sort_by = input("Sort by: ")
                    if len(query) == 0:
                        query = None
                    if len(sort_by) == 0:
                        sort_by = None
                    self.searchContact(query, sort_by)

                if n == 5:
                    new_data = []
                    for key, val in self.__data.items():
                        new_data.append(val)
                    self.viewContact(new_data)
                
                if n == 6:
                    break

            except Exception as e:
                pass



contact_book = Contact_Book()
contact_book.console()