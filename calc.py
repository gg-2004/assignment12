operand_1=int(input("Enter the first operand"))
operand_2=int(input("Enter the second operand"))
operator=input("Enter any operator(+,-,*,/)")
if operator=="+":
    print(operand_1+operand_2)
elif operator=="-":
    print(operand_1-operand_2)
elif operator=="*":
    print(operand_1*operand_2)
elif operator=="/":
    print(operand_1/operand_2)
else:
    print("none")