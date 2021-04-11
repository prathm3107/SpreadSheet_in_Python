class Worksheet:
    def __init__(self, worksheet_name, column_names, data):
        self.worksheet_name = worksheet_name
        self.column_names = column_names
        self.data = data
        
    def print_worksheet(self):
        column_widths = [len(data) for row in self.data for data in row]
        print(" ".join(columns.ljust(max(column_widths)+2)
                      for columns in self.column_names))
        for i in self.data:
            print(" ".join(data.ljust(max(column_widths)+2) 
                          for data in i))
