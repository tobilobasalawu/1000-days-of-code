s = '12:45:54PM'

if s[8:10] == 'PM' and s[0:2] == '12':
    print(f'{s[0:8]}')
elif s[8:10] == 'PM':
    intial = int(s[0:2]) + 12
    print(f"{intial}:{s[3:5]}:{s[6:8]}")
elif s[8:10] == 'AM' and s[0:2] == '12':
    print(f"00:{s[3:5]}:{s[6:8]}")
else:
    print(f'{s[0:8]}')