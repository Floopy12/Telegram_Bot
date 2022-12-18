import random as r
import time as t
class Guess:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.max_cash = cash


class Menu:
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.max_cost = cost
        self.max_quantity = quantity

guests = []

guests.append(Guess('Mike', 150))
guests.append(Guess('Bob', 130))
guests.append(Guess('Nikc', 125))

        
dishes = []

dishes.append(Menu('Spagetti', 50, 2))
dishes.append(Menu('Sup', 30, 1))
dishes.append(Menu('Meat', 70, 5))
dishes.append(Menu('Fish', 55, 5))
dishes.append(Menu('Cola', 15, 8))
dishes.append(Menu('Vegetables', 25, 6))

def order(self, dish = None):
    while 1:
        for i in range(3):
            dish = r.choice(dishes)     
            while dish.quantity <= 0:
                dish = r.choice(dishes)
            print(f'{self.name} заказывает {dish.name} за {dish.cost}.')
            t.sleep(1)
            self.cash -= dish.cost
            dish.quantity -= 1
            
            print(f'У {self.name} осталось {self.cash} наличных')
            t.sleep(1)
            if self.cash < 0:
                print('-Официант: У вас не хватает наличных для этого заказа.')
                self.cash = self.max_cash
                t.sleep(1)
                print(f'-{self.name}: Хорошо, дайте подумать...')
                t.sleep(1.7)
                break
        else:
                print(f'-Официант: Ваш заказ будет готов через минуту. \n-{self.name}: Хорошо, спасибо.')
                
                break
        
   

while 1:
    guest = int(input('Выберите гостя: '))
    order(guests[guest]) 




        
