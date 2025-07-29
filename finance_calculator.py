
def calculate_finances(monthly_income: float, tax_rate: float, currency: str, gym: float, room_rent: float, food: float)-> None:

    yearly_salary : float = monthly_income * 12
    monthly_tax : float = monthly_income*(tax_rate/100)
    yearly_tax: float = monthly_tax*12
    monthly_net_income : float = monthly_income -  monthly_tax
    yearly_net_income : float = monthly_net_income*12
    total_monthly_expense : float = gym + room_rent + food

    print("----------------------------------------------------------")
    print(f"Monthly Income: {currency}{monthly_income:,.2f}")
    print(f"Tax Rate: {tax_rate:,.0f}%")
    print(f"Monthly Tax: {currency} {monthly_tax:,.2f}")
    print(f"Monthly Net Income : {currency}{monthly_net_income:,.2f}")
    print(f"yearly Salary: {currency}{yearly_salary:,.2f}")
    print(f"Yearly Tax paid: {currency}{yearly_tax:,.2f}")
    print(f"Yearly Net Income: {currency}{yearly_net_income:,.2f}")
    print(f"Total Monthly Expense: {currency}{total_monthly_expense:,.2f}")
    print(f"Monthly Saving: {currency}{(monthly_income-total_monthly_expense):,.2f}")
    print("-----------------------------------------------------------") 

def main()->None:
    print("-----------------------------------------------------------")
    while(True):
            try:
                 monthly_income1=float(input("Enter Your Monthly salary or 0 to Quit: "))
                 if(monthly_income1 is not float):
                     break
                 tax_rate: float = float(input("Enter Your Tax Rate (%): "))
                 currency: str = input("Enter Your Currency : ")
                 gym: float = float(input("Enter your GYM Fees: "))
                 room_rent: float = float(input("Enter your Room Rent: "))
                 food: float = float(input("Enter your Food Expense: "))
                 print("--------------------------------------------------")
                 if (monthly_income1 > 0 and tax_rate >= 0 and gym >= 0 and room_rent > 0 and food > 0):
                  calculate_finances(monthly_income1, tax_rate, currency, gym, room_rent, food)
                  break
                 else:
                  print("Please enter valid positive values for all fields.")
            except ValueError:
                print("Invalid input! Please enter numeric values for salary, tax rate, and expenses.")
if __name__ == "__main__":
    main()