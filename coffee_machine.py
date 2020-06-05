# Write your code here
print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")


# Write your code here
class CoffeeMachine():
    water_ = 250
    milk_ = 75
    coffee_beans_ = 12
    disposable_cups_ = 1

    def __init__(self):
        self.water = 400
        self.money = 550
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
    def buy(self, type_coffee):
        if type_coffee == "1":
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
            self.disposable_cups -= 1

        elif type_coffee == "2":
            self.water -= 350
            self.coffee_beans -= 20
            self.money += 7
            self.disposable_cups -= 1
            self.milk -= 75
        elif type_coffee == "3":
            self.water -= 200
            self.coffee_beans -= 12
            self.money += 6
            self.disposable_cups -= 1
            self.milk -= 100

    def fill(self, water_, milk_, coffee_beans_, disposable_cups_):

        self.water += water_
        self.milk += milk_
        self.coffee_beans += coffee_beans_
        self.disposable_cups += disposable_cups_

    def take(self):

        print("I gave you", self.money)
        self.money -= self.money

    def show_remaining(self):
        print(f"""The coffee machine has:
    {self.water} ml of water
    {self.milk} ml of milk
    {self.coffee_beans} g of coffee beans
    {self.disposable_cups} of disposable cups
    {self.money} of money""")

    def user_input(self, action):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "buy":
                type_ = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                if self.water < CoffeeMachine.water_:
                    print("Sorry, not enough water!")
                    continue

                elif self.milk < CoffeeMachine.milk_:
                    print("Sorry, not enough milk!")
                    continue

                elif self.coffee_beans < CoffeeMachine.coffee_beans_:
                    print("Sorry, not enough coffee beans!")
                    continue

                elif self.disposable_cups < CoffeeMachine.disposable_cups_:
                    print("Sorry, not enough cups!")
                    continue

                elif type_ == "back":
                    continue

                else:
                    CoffeeMachine.buy(self, type_)
                    print("I have enough resources, making you a coffee!")

            elif action == "fill":
                add_water = int(input("Write how many ml of water do you want to add:"))
                add_milk = int(input("Write how many ml of milk do you want to add:"))
                add_coffee_beans = int(input("Write how many grams of coffee beans do you want to add:"))
                add_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
                CoffeeMachine.fill(self, add_water, add_milk, add_coffee_beans, add_disposable_cups)

            elif action == "take":
                CoffeeMachine.take(self)
            elif action == "remaining":
                CoffeeMachine.show_remaining(self)
            elif action == "exit":
                break


cm = CoffeeMachine()
cm.user_input("")



