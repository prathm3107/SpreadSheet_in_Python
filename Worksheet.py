class Worksheet:
    def __init__(self, worksheet_name, column_names, data):
        self.worksheet_name = worksheet_name
        self.column_names = column_names
        self.data = data
        
    def print_worksheet(self):
        print(f"== {self.worksheet_name} ==")
        print("\n")

        column_widths = [len(data) for row in self.data for data in row]
        print(" ".join(columns.ljust(max(column_widths)+2)
                      for columns in self.column_names))
        print("\n")

        for i in range(len(self.data[0])):
            for j in range(len(self.data)):
                print(self.data[j][i].ljust(max(column_widths) + 2), end = " ")
            print("\n")

    def sort_data(self, column_numbers = [], way_to_sort = []):
        if len(column_numbers) == 0 or len(way_to_sort) == 0:
            print("No changes made to the worksheet\n")
        else:
            for i in range(len(column_numbers)):
                self.data[column_numbers[i]].sort(reverse = way_to_sort[i])
