from Worksheet import Worksheet

worksheet_name = input("Enter the worksheet name: ")
column_names = input("Enter the Column names: ").split(" ")
print("Enter the data for the following columns\n**Enter q to finish**")
for i in column_names:
    print(i, end = "\t")

worksheet_data = [[] for _ in range(len(column_names))]
temp = input("\n").split(" ")
while(temp[0].lower() != 'q'):
    for i in range(len(temp)):
        worksheet_data[i].append(temp[i])
    temp = input().split(" ")
    
w1 = Worksheet(worksheet_name, column_names, worksheet_data)

op = input("Enter the operation you want to perform \n1. Print Worksheet \n**Enter q to finish**\n")
while (op != 'q'):
    if op == '1':
        print("\n")
        w1.print_worksheet()
        print("\n")
    op = input("Enter the operation you want to perform: \n1. Print Worksheet \n**Enter q to finish**\n")
