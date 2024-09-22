print('30 Days Down - What do you think?/n')

for i in range(1,31):
    askUser = input(f'\nDay {i}:\n')
    sysText = f'You Thought Day {i} was'
    print(f'{sysText:^50}', end="")
    print(f'\n{askUser: ^50}')