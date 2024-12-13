from budget_class import BudgetCategory


food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()

food_category = BudgetCategory("Rent", 1000)
food_category.add_expense(300)
food_category.display_category_summary()