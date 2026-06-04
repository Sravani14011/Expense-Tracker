expenses = []
while true:
  print("\n====Expense Tracker====")
  print("1. Add Expenses")
  print("2. view Expenses")
  print("3. Show Total Expense")
  print("4. Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    item = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append([item, amount])
    print("Expense added succesfully!")
  elif choice == "2":
    print("\nExpense list")
    for expense in expenses:
      print(expense[0], "-₹", expense[1])
  elif choice == "3":
    total = 0
    for expense in expenses:
      total += expense[1]
    print("Total Expense = ₹", total)
  elif choice == "4":
    print("Thank you")
    break
  else:
    print("Invalid choice")
