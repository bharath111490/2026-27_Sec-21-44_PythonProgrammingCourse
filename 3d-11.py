balance = 1000
def deposit(amount):
    global balance
    balance += amount
    print("Balance after deposit:", balance)
def show_local_balance():
    balance = 5000 
    print("Local balance inside function:", balance)
print("Initial balance:", balance)
deposit(500)
show_local_balance()
print("Final account balance:", balance)