class Mobil:

    # attributes and method of the parent class
    name = ""

    def start(self):
        print("Mobil mogok")
# inherit from Mobil
class MobilSport(Mobil):

    # override start() method
    def start(self):
        print("Mobil sport sudah bisa melaju dengan cepat")

# create an object of the subclass
porsche = MobilSport()

# call the start() method on the porsche object

porsche.start()
