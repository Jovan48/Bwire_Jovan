# create an atm withdrawal program, use if-else statements to check account balance before allowing withdrawal

balance = 0 
    
deposit_amount = float(input("Enter the amount to deposit: $"))
new_balance = balance + deposit_amount
print(f"Deposit successful! Your new balance is: ${new_balance}")
withdrawal_amount = float(input("Enter the amount to withdraw: $"))
final_balance = new_balance - withdrawal_amount    
    
if withdrawal_amount <= 0:
        print("Withdrawal amount must be greater than zero.")
elif withdrawal_amount > new_balance:
        print("Insufficient funds. Your current balance is: $", balance)
else:
        new_balance -= withdrawal_amount
        print(f"Withdrawal successful! Your new balance is: ${final_balance}")