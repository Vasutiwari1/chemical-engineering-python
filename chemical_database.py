# =============================================
# Chemical Properties Database
# Author: Vasu Tiwari
# College: PDPU — Chemical Engineering
# Year: 2025
# =============================================

database = {
    "Water": {
        "boiling_point"   : 100,
        "molecular_weight": 18,
        "state"           : "Liquid"
    },
    "Ethanol": {
        "boiling_point"   : 78,
        "molecular_weight": 46,
        "state"           : "Liquid"
    },
    "Benzene": {
        "boiling_point"   : 80,
        "molecular_weight": 78,
        "state"           : "Liquid"
    },
    "Methane": {
        "boiling_point"   : -161,
        "molecular_weight": 16,
        "state"           : "Gas"
    },
    "Ammonia": {
        "boiling_point"   : -33,
        "molecular_weight": 17,
        "state"           : "Gas"
    }
}

def search(name):
    if name in database:
        result = database[name]
        print(f"=== {name} ===")
        print(f"Boiling Point    : {result['boiling_point']}°C")
        print(f"Molecular Weight : {result['molecular_weight']} g/mol")
        print(f"State            : {result['state']}")
    else:
        print("Chemical not found!")
def show_all():
 count=0
 for name in database:
    count+=1
    print(count,name)
def add_chemical():
    name=input("enter chemical name u want to add: ")
    boiling_point=float(input("enter the boiling point of chemical: "))
    molecular_weight=float(input("enter the molecular weight of chemical: "))
    state=input("enter the state of chemical: ")
    database[name]={"boiling_point":boiling_point,
                    "molecular_weight":molecular_weight,
                    "state":state
    }
    print(f" {name} added successfully!")
def delete_chemical():
 name_to_be_deleted=input("enter the chemical you want to delete from database: ")
 if name_to_be_deleted in database:
  del database[name_to_be_deleted]
  print(f"{name_to_be_deleted}deleted successfully")
 else:
    print("no chemical found ")
def menu():
    while True:                    
        print("1. Search")
        print("2. Add")
        print("3. Delete")
        print("4.show all")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
         name = input("Enter chemical name: ")
         search(name)             
        elif choice == "2":
           add_chemical()                   
        elif choice == "3":
            delete_chemical()                 
        elif choice == "4":
              show_all()                
        elif choice == "5":
            print("Goodbye!")
            break                 
        else:
            print("Invalid choice!")
        

menu()                            
