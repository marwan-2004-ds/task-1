hours_worked = float(input("hours worked: "))
hourly_rate = float(input("hourse rate: "))

gross_pay = hours_worked * hourly_rate
print(f"The employee's gross pay is: {gross_pay:.2f}")

rate = gross_pay * 0.20
final_pay = gross_pay - rate
print(f"The employee's final pay after tax is: {final_pay:.2f} $USD")