# Stap 1: Definieer de Class
class Location:
    # De __init__ methode wordt uitgevoerd bij aanmaak
    def __init__(self, name, country):
        self.name = name
        self.country = country

    # Stap 2: Voeg een methode toe
    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

# Stap 3: Instanties maken (objecten creëren)
loc1 = Location("Tomas", "Portugal")
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
your_loc = Location("Glineur Quentin", "België")

# Stap 4: De methode aanroepen
loc1.myLocation()
loc2.myLocation()
loc3.myLocation()
your_loc.myLocation()