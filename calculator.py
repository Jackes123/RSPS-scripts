#Small script to calculate the prices in a trade.
num_items = int(input("Enter the number of items to be traded: "))

price_per_item_upgrade_tokens = 5800000 #The price of the item

exchange_rate = 1000 #Currency rate



# Calculate the total cost in both currencies
total_cost_primary = num_items * price_per_item_upgrade_tokens
total_cost_secondary = total_cost_primary / exchange_rate


print("  ")

#Display the total cost in both currencies
print(f"The total cost for {num_items} items at {price_per_item_upgrade_tokens / 1000000} million per item is {int(total_cost_primary / 1000000)}m")
print(f"The equivalent cost in 1k tokens is {int(total_cost_secondary / 1000)}k")