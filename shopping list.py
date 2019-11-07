"""Shopping list that asks what you want, how much you want, what your priorities are"""


shopping_list = {}


running = True

while running:
    
    print("type q if you want to quit ")
    amount = int(input("How many things are you going to buy?: "))
    
    shop = input("What shop are you going to?: ")
    
    for i in range(amount):
        
        item = input("Enter the item name: ")
        
        priority = input("Enter the priority of this item: ")
        
        
        
        pay = input("Enter the amount you are willing to pay: ")

        quantity = input("Enter the amount of this item you want: ")
        
        shopping_list[item] = priority, pay, quantity
        
        print(shopping_list)
        
    if str(amount) == "q":
        
        running = False


