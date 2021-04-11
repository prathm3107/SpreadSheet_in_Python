from Worksheet import Worksheet

worksheet_name = input("Enter the worksheet name: ")
column_names = input("Enter the Column names: ").split(" ")
print("Enter the data for the following columns\n**enter q to finish**")
for i in column_names:
    print(i, end = "\t")

worksheet_data = []
temp = input("\n").split(" ")
while(temp[0].lower() != 'q'):
    worksheet_data.append(temp)
    temp = input().split(" ")
    
w1 = Worksheet(worksheet_name, column_names, worksheet_data)
print("\n====================================\n")
w1.print_worksheet()
