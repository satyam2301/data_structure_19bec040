class Creditcard:
    def __init__(self,customer,bank,creditcard,balance,charge): 
        self._customer=customer
        self._bank=bank
        self._creditcard=creditcard
        self._balance=balance
        self._charge=charge
    def get_customer(self): 
        return self._customer 
    def get_bank(self): 
        return self._bank 
    def get_creditcard(self):
        return self._creditcard 
    def get_balance(self):
        return self._balance 
    def get_charge(self):
        price=int(input())             #you have to give input here to get the output of charge 
        self._balance=self._balance+price
        return self._balance

if __name__ == '__main__':
    wallet = []
    wallet.append(Creditcard('Raj','swaraj bank','5371 0345 1245 2764',45000,1))
    wallet.append(Creditcard( 'John Bowman' , 'California Federal' ,' 3485 0399 3395 1954' , 35000,2)) 
    wallet.append(Creditcard( 'John Bowman' , 'California Finance' , '5391 0375 9387 5309' , 50000,3))

    
    for c in range(3):
        print( 'Customer=' , wallet[c].get_customer())
        print( 'Bank =' , wallet[c].get_bank())
        print('creditcard=',wallet[c].get_creditcard()) 
        print('balance=',wallet[c].get_balance())
        print('charge=',wallet[c].get_charge())

    

