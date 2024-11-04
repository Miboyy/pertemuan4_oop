class Mobil:

    # attribute and method of the parent class
    name = "Porsche"
    harga = "15 Milliar"
    def sport(self):
        print("Aku Mobil Sport Tercepat")
    

# inherit from Animal
class Mobilsport(Mobil):

    # new method in subclass
    def Cetaknama(self):
        # access name attribute of superclass using self
        print("Namaku : ", self.name)
    def cetakharga(self):
        print("Hargaku :", self.harga)

# create an object of the subclass
labrador = Mobilsport()

# access superclass attribute and method 

labrador.sport()
labrador.cetakharga()
# call subclass method 
labrador.Cetaknama()