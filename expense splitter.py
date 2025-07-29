#-------------------------------------Expense Spiltter--------------------------------------
def calculate_split(total_amount,number_of_people,currency):
    if(number_of_people<=1):
        raise ValueError("Number of People must be greater than one")
    
    print("---------------------------------------------")
    print(f"Total Expenses:{currency}{total_amount}")
    print(f"Total People:{number_of_people}")

def main():
    while(True):    
        try:
            print("----------------------------------------------------------")
            total_amount1=int(input("Enter the total amount of expense or 0 to Quit: "))
            if((total_amount1)==0):
                break
            number_of_people1=int(input("Enter the total number of people or 0 to Quit: "))
            if(number_of_people1==0):
                break
            Lsit_currency=["Rs." , "$" ,"Uro"]
            currency=input("Currency:")
            if(currency not in Lsit_currency):
                raise ValueError("The Currency must be in : ", Lsit_currency)
            
            total_amount=float(total_amount1)
            number_of_people=int(number_of_people1)
            print("----------------------------------------------------------")
            user_input=[]
            i=0
            while(i<int(number_of_people1)):
                user=input("Enter your Share % (Q to quit): ")
                if(user.upper()=="Q"):
                    break
                try:
                    user_share=float(user)
                    if(0<=user_share<=100):
                        user_input.append(user_share)
                    else:
                        print("Invalid shares Please enter the value between 0 to 100")
                except ValueError:
                    print("Invalid Input. Please Enter the Number and q to Quit.")
                i=i+1
            if(sum(user_input)!=100):
                print("Warning:Total Number of Shares Should be 100%. Please Enter again.")
                continue
            if(len(user_input)!=number_of_people):
                print(f"Warning: Number of shares must be equal to{number_of_people}. Please Enter again")
                continue
            calculate_split(total_amount,number_of_people,currency)

            print("-------------------------------------------")
            for i in range(len(user_input)):
                print(f"Person {i+1} Share:{currency}{(user_input[i]/100)*total_amount:,.2f}.")
            break
        except ValueError as e:
            print(f"Error:{e}")

if (__name__=="__main__"):
    main()