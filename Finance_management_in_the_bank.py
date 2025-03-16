import abc

class Payable(abc.ABC):

    @abc.abstractmethod
    def pay(self,amount): pass


class CreditCard:
    def __init__(self,balance=0,limit=0):
        if not self.validate_card(balance,limit):
            raise TypeError('Balance and limit should be integer and positive number!!')
        self.__balance = balance
        self.__limit = limit
        self.owner = None


    @staticmethod
    def validate_card(*numbers):
        return all(isinstance(num,(int,float)) and num >= 0  for num in numbers )


    @property
    def balance(self):
        return self.__balance


    @balance.setter
    def balance(self,new_balance):
        if not self.validate_card(new_balance):
            raise TypeError('Balance should be positive number!!')
        self.__balance = new_balance


    @property
    def limit(self):
        return self.__limit


    @limit.setter
    def limit(self, new_limit):
        if not self.validate_card(new_limit):
            raise TypeError('limit should be positive number!!')
        self.__limit = new_limit


    def validate_pay(self,amount):
        if not (self.validate_card(amount) and self.__balance >= amount):
            raise ValueError("Недостаточно средств для списания баланса!")
        return amount



class Person:
    def __init__(self,name,age,credit_card):
        if not self.validate_person(age,name):
            raise TypeError('Некорректный ввод информации.')
        self.__name = name
        self.__age  = age
        self.credit_card = credit_card
        self.credit_card.owner = self


    @staticmethod
    def validate_person(age,name):
        return isinstance(age,int) and isinstance(name,str) and 18 <= int(age) <= 120


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self,new_age):
        if self.validate_person(new_age,self.__name):
            self.__age = new_age


    def introduce(self):
        return f"Меня зовут {self.__name}, мне {self.__age} лет."




class Student(Person,Payable):
    def __init__(self, name, age,university, credit_card):
        super().__init__(name, age, credit_card)
        self.university = university


    def pay(self,amount):
        amount = self.credit_card.validate_pay(amount)
        discount = amount * 0.1
        final_amount = amount - discount
        self.credit_card.balance -= final_amount
        print(f"Оплачено {final_amount} со скидкой 10%.  Новый баланс: {self.credit_card.balance}")



class Employee(Person,Payable):
    def __init__(self,name,age,salary,credit_card):
        super().__init__(name,age,credit_card)
        self.salary = salary


    def pay(self,amount):
        amount = self.credit_card.validate_pay(amount)
        self.credit_card.balance -= amount
        print(f"Оплачено {amount}. Новый баланс: {self.credit_card.balance}")






student = Student("Bob", 20, "MIT", CreditCard(1000, 3000))
employee = Employee("John", 35, 50000, CreditCard(2000, 10000))
print(student.credit_card.owner)
print(employee.credit_card.owner)
print(student.credit_card.balance)
print(employee.credit_card.balance)
student.pay(200) # "Оплачено 180 (скидка 10%). Новый баланс: 820"
employee.pay(200) # "Оплачено 200. Новый баланс: 1800"
