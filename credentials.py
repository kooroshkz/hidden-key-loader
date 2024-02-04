try:
    with open('dev_credentials.txt', 'r') as file:

        for line in file:
            variable, value = line.strip().split(' = ')
            value = value.strip('"')
            exec(f'{variable} = "{value}"')

except FileNotFoundError:

    with open('credentials.txt', 'r') as file:

        for line in file:
            variable, value = line.strip().split(' = ')
            value = value.strip('"')
            exec(f'{variable} = "{value}"')