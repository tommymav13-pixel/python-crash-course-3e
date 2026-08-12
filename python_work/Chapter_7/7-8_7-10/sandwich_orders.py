sandwich_orders = ['tuna', 'chicken', 'salmon', 'beef', 'teriyaki', 'pastrami', 
                   'pastrami', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

# loop through te list
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

# Polling is complete. Show the results.
print("\n--- Order List ---")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich.")
