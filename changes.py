class Client:
    def __init__(self, name, phone_number, bank_account):
        self.name = name
        self.phone_number = phone_number
        self.bank_account = bank_account

    def bill_customer(self, cost):
        
        print(f"Facturation de {self.name} d'un montant de {cost}.")

    def refund_customer(self, amount):
        
        print(f"Remboursement de {self.name} d'un montant de {amount}.")

client1 = Client("Alice Dupont", "123-456-7890", "FR76 1234 5678 9012 3456 7890 123")


client1.bill_customer(100)


client1.refund_customer(50)
