
#1. Vehicle
#2. Driver
#3. Rider


class Zone:

    def __init__(self):

        self.drivers = []
        self.cars = []
        self.users = []

    def addDrivers(self, drivers_list):

        self.drivers.append(drivers_list)
        print('Drivers are added to the Zone')

    def addCars(self, cars_list):

        self.cars.append(cars_list)
        print('Drivers are added to the Zone')


    def addUsers(self, users_list):
            self.users.append(users_list)
            print('Drivers are added to the Zone')


    def getDrivers(self):

        return self.drivers


    # def getinfo(self):
    #     print([i.plate for i in self.cars])
    #     print('--------------------------')
    #     print([i.name for i in self.drivers])
    #     print('--------------------------')
    #     print([i.name for i in self.users])

class Car:

    def __init__(self, plate, make, model):

        self.plate = plate
        self.make = make
        self.model = model
        self.fuel_percent = 0.7
        self.capacity = 4


class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.history = []
        self.location = None

    def requestRide(self, dist, zone):

        #List down all the drives in the zone
        drivers_list = zone.getDrivers()[0]

        act_drivers_status = [div.getDriverName() for div in drivers_list]

        for div in act_drivers_status:
            if div[2] == "Available":
                print(div[1])
                break
            else:
                continue


class Driver:
    def __init__(self, id, name, vehicle=None, status="Available"):
        self.id = id
        self.name = name
        self.history = []
        self.location = None
        self.status = status

    def getInfo(self):
        print(f'Name: {self.name}, Driver ID: {self.id} , Location: {self.location} , Status: {self.status}')

    def getDriverName(self):
        return self.id, self.name, self.status
    
    def setStatus(self, status):
        old_status = self.status
        self.status = status
        print(f'The Status of the Driver is changed from {old_status} --> {self.status}')

    def acceptRide(self, user, dist=20):
        if self.status != "Available":
            print("Cannot accept ride, diver is not available")
        else:
            print(f"Ride has been started with  {user.name}")
            self.setStatus('Busy')
            self.history.append([self.name, f'Rider: {user.name}', f'Distance: {dist}'])

    def getHistory(self):
        print(self.history)


    def completeRide(self):
        self.setStatus('Avaiable')
