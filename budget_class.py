class BudgetCategory:
    categories = []

    def __init__(self, name, budget): #Define budget category, with name and budget amounts
        self.__name = name
        self.__budget = budget
        self.expenses = [] #This list will eventuallty contain a dictionary of expenses
        BudgetCategory.categories.append(self) #Adds the object to the Categories List

    def get_name(self): #Define Name Getter
        return self.__name
    
    def get_budget(self): #Define Budget Getter
        return self.__budget
    
    def set_name(self, new_name): #Define Name Setter
        old = self.__name
        self.__name = new_name
        print(f"Category name {old} changed to {new_name}!")

    def set_budget(self, new_budget): #Set Budget Setter
        try:
            if new_budget < 1:
                old = self.__budget
                self.__budget = new_budget
                print(f"Budget amount {old} changed to {new_budget}")
            else:
                print(f"Error: Cannot have a budget less than 0")
        except ValueError:
            print(f"Error: Please enter a number.")

    def add_expense(self, exp_amount): #Reduces the value of "Budget" by the spent expense
        try:
            if exp_amount > self.__budget: #Error Checking
                print(f"This amount exceeds your budget.")
            else:
                self.__budget -= exp_amount
                self.expenses.append({'Amount': exp_amount})
                print(f"{exp_amount} added to {self.__name} budget")
        except ValueError:
            print(f"Error: Please enter a number.")


    def display_category_summary(cls):
        print(f"Categories:\n")
        for category in cls.categories:
            print(f"Category: {category.get_name()}\nBudget: {category.get_budget()}")