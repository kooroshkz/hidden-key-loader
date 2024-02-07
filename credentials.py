# NO NEED TO CHANGE ANYTHING IN THIS FILE


class File:
    def __init__(self):
        self.file_names = ["dev_credentials.txt", "credentials.txt"]
        self.selected_file = None
        
        try:
            with open(self.file_names[0], 'r') as file:
                self.selected_file = self.file_names[0]
        except FileNotFoundError:
            with open(self.file_names[1], 'r') as file:
                self.selected_file = self.file_names[1]

    def fetch_data(self):
        with open(self.selected_file, 'r') as file:
            for line in file:
                variable, value = line.strip().split(' = ')
                value = value.strip('"')
                exec(f'global {variable}; {variable} = "{value}"')
        
file_object = File()
file_object.fetch_data()
