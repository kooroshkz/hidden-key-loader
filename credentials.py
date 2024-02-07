class File():
    def __init__(self):
        self.dev_file = "dev_credentials.txt"
        self.file = "credentials.txt"
        self.final = None
        try :
            with open(self.dev_file, 'r') as file:
                self.final = self.dev_file
        
        except FileNotFoundError:
            with open(self.file, 'r') as file:
                self.final = self.file

    def fetch_data(self):
        with open(self.final, 'r') as file:
            for line in file:
                variable, value = line.strip().split(' = ')
                value = value.strip('"')
                exec(f'global {variable}; {variable} = "{value}"')
        
file_object = File()
file_object.fetch_data()
