# Initialize an empty portfolio dictionary
portfolio = {}

# Create a loop to manage the portfolio
while True:
    print("Portfolio Management Menu:")
    print("1. Add Asset")
    print("2. Update Asset")
    print("3. Retrieve Asset Information")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Add an asset to the portfolio
        asset_name = input("Enter asset name: ")
        asset_details = {}  # Create a dictionary to store asset details
        # Prompt for and store details such as quantity, purchase price, etc.
        asset_details["quantity"] = float(input("Enter quantity: "))
        asset_details["purchase_price"] = float(input("Enter purchase price: "))
        portfolio[asset_name] = asset_details

    if choice == "2":
        # Update asset details
        asset_name = input("Enter asset name to update: ")
        if asset_name in portfolio:
            # Prompt for and update details such as quantity, purchase price, etc.
            portfolio[asset_name]["quantity"] = float(input("Enter new quantity: "))
            portfolio[asset_name]["purchase_price"] = float(input("Enter new purchase price: "))
        else:
            print("Asset not found in the portfolio.")

    if choice == "3":
        # Retrieve and display asset information
        asset_name = input("Enter asset name to retrieve: ")
        if asset_name in portfolio:
            # Display asset details
            print("Asset Name:", asset_name)
            print("Quantity:", portfolio[asset_name]["quantity"])
            print("Purchase Price:", portfolio[asset_name]["purchase_price"])
        else:
            print("Asset not found in the portfolio.")

    if choice == "4":
        break  # Exit the program
