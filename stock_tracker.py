# Stock Portfolio Tracker

stocks = {
    "WIPRO": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMAZON": 130
}

print("📈 Stock Portfolio Tracker")

stock_name = input("Enter stock name (WIPRO/TSLA/GOOGLE/AMAZON): ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    total = stocks[stock_name] * quantity
    print("Stock:", stock_name)
    print("Price:", stocks[stock_name])
    print("Quantity:", quantity)
    print("Total Investment: $", total)
else:
    print("❌ Stock not found!")