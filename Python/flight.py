class Flight():
    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.passengers=[]
    def add_passenger(self,name):
        if  not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity-len(self.passengers)

flight= Flight(4)
people=["Avinash","Chunduri","Gitam","rajju"]
for i in people:
    if flight.add_passenger(i):
        print(f"Added {i} to the flight successfully")
    else:
        print(f"No available seats for {i}")