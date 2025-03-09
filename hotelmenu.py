#Define the menu of restaurant

menu ={
    'Pizza':400,
    'Burger':350,
    'Salad':250,
    'Fries':200,
    'Shake':250,
    'Dessert':300,
    'Beverage':150,
    'Coffee':300,
}
# Greet

print("Welcome to our restaurant!")
print("Pizza : Rs400\nBurger : RS500\nSalad :Rs250\nFries :Rs500\nShake :Rs250\nDessert :Rs500\nBeverage :Rs150\nCoffee :Rs150\n")

order_total = 0


item_1 = input("Enter name of item you want to order = ")
if item_1 in menu:
     
     order_total += menu[item_1]
     print(f"Your item {item_1} has been added to the order")

else:  
        print (f"Ordered item {item_1} is not available")

another_order = input("Do you want to add another item? (Yes/No)")

if another_order=="Yes":
        item_2 = input("Enter the name of your second item =")

        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Your item {item_2} has been added to the order")
        else:
            print(f"Ordered item {item_2} is not available")

            print(f"The total amount of order is {order_total}")
                   