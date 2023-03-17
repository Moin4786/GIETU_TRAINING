'''class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, cost):
        self.__vehicle_id = vehicle_id
        self.__vehicle_type = vehicle_type
        self.__cost = cost
        self.__premium_amount = self.__calculate_premium_amount()

    def __calculate_premium_amount(self):
        if self.__vehicle_type == "Two Wheeler":
            return self.__cost * 0.02
        elif self.__vehicle_type == "Four Wheeler":
            return self.__cost * 0.06
        else:
            raise ValueError("Invalid vehicle type")

    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type
        self.__premium_amount = self.__calculate_premium_amount()

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost
        self.__premium_amount = self.__calculate_premium_amount()

    def get_premium_amount(self):
        return self.__premium_amount

    def __str__(self):
        return f"Vehicle ID: {self.__vehicle_id}, Vehicle Type: {self.__vehicle_type}, Cost: {self.__cost}, Premium Amount: {self.__premium_amount}"



vehicle1 = Vehicle("V001", "Two Wheeler", 50000)
print(vehicle1.get_premium_amount())  # Output: 1000.0
vehicle2 = Vehicle("V002", "Four Wheeler", 100000)
print(vehicle2.get_premium_amount())  #

class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
    
    def validate_marks(self):
        return self.__marks >= 0 and self._marks <= 100
    
    def validate_age(self):
        return self.__age > 20
    
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks >= 65:
                return True
        return False
    
    def set_student_id(self, id):
        self.__student_id = id
    
    def set_marks(self, marks):
        self.__marks = marks
    
    def set_age(self, age):
        self.__age = age
    
    def get_student_id(self):
        return self.__student_id
    
    def get_marks(self):
        return self.__marks
    
    def get_age(self):
        return self.__age
    
    def get_discount(self):
        if self.__marks > 85:
            return 0.25
        else:
            return 0
    
    def get_fee(self, course_fee):
        return course_fee - (course_fee * self.get_discount())

s = Student()

# Set the student details
s.setb _student_id(101)
s.set_marks(75)
s.set_age(23)

# Check if the student qualifies for admission
if s.check_qualification():
    print("Qualified for admission")
    course_fee = 10000
    fee_after_discount = s.get_fee(course_fee)
    print("Course fee after discount:", fee_after_discount)
else:
    print("Not qualified for admission")'''





class Customer:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.quantity = 0

    def validate_quantity(self, quantity):
        if quantity > 0 and quantity <= 2:
            self.quantity = quantity
            return True
        else:
            return False

class PizzaService:
    counter = 100

    def __init__(self, pizza_type, additional_topping):
        self.pizza_type = pizza_type
        self.additional_topping = additional_topping
        self.pizza_cost = 0
        self.service_id = chr(ord(pizza_type[0].upper())) + str(PizzaService.counter)
        PizzaService.counter += 1
                                                                                            
    def validate_pizza_type(self):
        if self.pizza_type.lower() == 'small' or self.pizza_type.lower() == 'medium':
            return True
        else:
            return False
            
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and customer.validate_quantity(customer.quantity):
            if self.pizza_type.lower() == 'small':
                self.pizza_cost = 150
            elif self.pizza_type.lower() == 'medium':
                self.pizza_cost = 200
            if self.additional_topping:
                self.pizza_cost += 50
        else:
            self.pizza_cost = -1

class DoorDelivery(PizzaService):
    def __init__(self, pizza_type, additional_topping, distance_in_kms):
        super().__init__(pizza_type, additional_topping)
        self.distance_in_kms = distance_in_kms
        self.delivery_charge = 0

    def validate_distance_in_kms(self):
        if self.distance_in_kms >= 1 and self.distance_in_kms <= 10:
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms() and super().validate_pizza_type() and customer.validate_quantity(customer.quantity):
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                if self.distance_in_kms <= 5:
                    self.delivery_charge = 5
                else:
                    self.delivery_charge = 5 + (self.distance_in_kms - 5) * 7
        else:
            self.pizza_cost = -1

customer = Customer("John Doe", "123 Main Street", "555-1234")

pizza_service = PizzaService("small", True)
pizza_service.calculate_pizza_cost()
print("PizzaService Details:")
print("Service ID:", pizza_service.service_id)
print("Pizza Type:", pizza_service.pizza_type)
print("Additional Topping:", pizza_service.additional_topping)
print("Pizza Cost:", pizza_service.pizza_cost)

door_delivery = DoorDelivery("medium", False, 7)
door_delivery.calculate_pizza_cost()
print("DoorDelivery Details:")
print("Service ID:", door_delivery.service_id)
print("Pizza Type:", door_delivery.pizza_type)
print("Additional Topping:", door_delivery.additional_topping)
print("Distance in KMs:", door_delivery.distance_in_kms)
print("Pizza Cost:", door_delivery.pizza_cost)
print("Delivery Charge:", door_delivery.delivery_charge)





