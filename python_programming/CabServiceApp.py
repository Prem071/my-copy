from configApp import Zone, Car, Driver, User


z1 =  Zone()

c1 = Car("HB 5967","Hyundai", "Aura")
c2 = Car("BV 8963", "Toyota", "Etios")

d1 = Driver(1, "John", vehicle=c1, status="Busy")
d2 = Driver(2, "Stephen", vehicle=c2, status="Lunch")
d3 = Driver(3, "Rechen", status="Lunch")
d4 = Driver(4, "Smith", status="Available")

u1 = User(3, "Jennifer")
u2 = User(4, "Kryz")

z1.addCars([c1, c2])
z1.addDrivers([d1, d2, d3, d4])
z1.addUsers([u1, u2])
# z1.getinfo()

u1.requestRide(100, z1)


