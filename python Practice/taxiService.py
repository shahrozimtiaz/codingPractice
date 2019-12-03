class TaxiCompany:
    def __init__(self,companyName,taxis=set()):
        self.name = companyName
        self.taxis = taxis
    def addTaxi(self,taxi):
        self.taxis.add(taxi)
    def removeTaxi(self,taxi):
        self.taxis.remove(taxi)
    def __str__(self):
        return 'Company name: {}, # of Taxis: {}'.format(self.name,len(self.taxis))

    class Taxi:
        def __init__(self,company,taxiNumber,drivers=set()):
            self.company = company
            self.number = taxiNumber
            self.drivers = drivers
        def addDriver(self,driver):
            self.drivers.add(driver)
        def removeDriver(self,driver):
            self.drivers.remove(driver)

        class Driver:
            def __init__(self,taxi,driverName,trips=[]):
                self.taxi = taxi
                self.name = driverName
                self.trips = trips
                self.income = 0
                self.taxi.addDriver(self)
            def addTrip(self,trip):
                self.trips.append(trip)
            def getPayment(self):
                if len(self.trips)>0 and not self.trips[-1].paid:
                    trip = self.trips[-1]
                    moneyPaid = trip.passenger.givePayment(self.calculteFare(trip))
                    if moneyPaid > 0:
                        trip.paid=True
                else:
                    print('no trips')
            def getPaymentAll(self):
                for trip in self.trips:
                    if not trip.paid:
                        moneyPaid = trip.passenger.givePayment(self.calculteFare(trip))
                        if moneyPaid > 0:
                            trip.paid = True

            def calculteFare(self,trip):
                return 3 + (trip.miles * 1.73)


        class Passenger:
            def __init__(self, passengerName,balance=50):
                self.name = passengerName
                self.balance = balance

            def givePayment(self,money):
                if self.balance >= money:
                    self.balance -= money
                    print('fare of ${} has been paid'.format(money))
                    return money
                else:
                    print('fare can\'t be paid')
                    return 0
            def addBalance(self,money):
                self.balance += money

        class Trip:
            def __init__(self,miles,driver,passenger):
                self.miles = miles
                self.driver = driver
                self.passenger = passenger
                self.paid = False
                self.driver.addTrip(self)
def test():
    Trip = TaxiCompany.Taxi.Trip
    Driver = TaxiCompany.Taxi.Driver
    Passenger = TaxiCompany.Taxi.Passenger

    company = TaxiCompany('Rosey&Corbae\'s9MonthTaxiService')
    taxi_001 = company.Taxi(company,'001')
    gadget = Driver(taxi_001,'Gadget')
    jax = Driver(taxi_001,'Jax')
    leah = Passenger('leah',69)
    trip_1 = Trip(4.20,gadget,leah)
    print('before fare:',leah.balance)
    gadget.getPayment()
    print('after fare:',leah.balance)
    if(leah.balance == 58.734):
        print('test passed')
    else:
        print('test failed')

def interactive():
    companies = set()
    drivers = set()
    passengers = set()
    trips = []

    Trip = TaxiCompany.Taxi.Trip
    Driver = TaxiCompany.Taxi.Driver
    Passenger = TaxiCompany.Taxi.Passenger

    while True:
        command = input('Enter a command\n').lower()

        if command == 'help':
            print('1-create company {company name}')
            print('2-create taxi {company name},{taxi number}')
            print('3-create driver {taxi name},{driver name}')
            print('4-create passenger {passenger name},{balance}')
            print('5-create trip {miles driven},{driver name},{passenger name}')
            print('-----------------------------------------------------------------')
            print('1-get company {company name}')
            print('2-get taxi {company name},{taxi number}')
            print('3-get driver {taxi name},{driver name}')
            print('-----------------------------------------------------------------')
            print('1-records')
        elif 'create company' in command:
            inputs = command[14:]
            companies.add(TaxiCompany(companyName=inputs))
        elif 'records' in command:
            print('companies: ')
            for company in companies:
                print(' ', company)
            print('drivers: ', drivers)
            print('passengers: ', passengers)
            print('trips: ', trips)
        else:
            print('no such command')



if __name__ == '__main__':
    interactive()