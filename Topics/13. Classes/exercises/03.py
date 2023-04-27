class BankAccount:
    def __init__(self, balance): #Comentarios igual que ne el 01.py
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount 
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount #Creo una variable balanace en este método, que no tiene nada que ver con la variable balance del init (para mí sí que tienen relación, pero para el ordenador no)
        else:
            print("There are not sufficient funds to substract this amount")

saldo = 35000
print (saldo)

cuenta = BankAccount(saldo)
cuenta.deposit(1000)
saldo = cuenta.balance #Esta línea podríamos ahorrarla poniendo en el print directamente print(cuenta.balance)
print (saldo)

cuenta.withdraw(200)
saldo = cuenta.balance
print (saldo)