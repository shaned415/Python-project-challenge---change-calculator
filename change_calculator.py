from sys import exit

   
def dollars_to_cents(purchase, given):
    """
    converts float dollar value to an
    integer value in cents
    """
    purchase, given = float(purchase), float(given)
    change_in_cents = (given - purchase) * 100
    change_in_cents = int(change_in_cents)
    return change_in_cents

def coins_returned(change):
    """
    Creates a list of tuples with coin name and
    amount of each coin returned
    """
    values = [5000, 2000, 1000, 500, 200, 100, 25, 10, 5, 1]
    coin_name = ['$50 bills:', '$20 bills:', '$10 bills:', 
                 '$5 bills:', 'Toonies:', 'Loonies:', 'Quarters:', 
                 'Dimes:', 'Nickels:', 'Pennies:']
    returned = []
    for value in values:
        coin_back = change / value
        returned.append(coin_back)
        change = change % value
    returned = zip(coin_name, returned)
    return returned
    
def start():
    price_of_purchase = raw_input("Enter price of purchase:\n>$")
    money_given = raw_input("Enter amount given:\n>$")

    cents = dollars_to_cents(price_of_purchase, money_given)
    returned = coins_returned(cents)
    for a, b in returned:
        if b > 0:
            print a, b
    again = raw_input("Enter another set of value? (Y or N)\n>")
    if again == "Y" or again == "y":
        start()
    else:
        quit(0)

    
start()
