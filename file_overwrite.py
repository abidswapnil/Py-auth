a_list = ['10']
i = input('i: ')
a_list.append(i)
with open('rough.py', 'r') as f:
    read_file = f.read()
item_1 = read_file.split('\n')[0]
item_2 = f'a_list = {a_list}'
new_file = read_file.replace(str(item_1), str(item_2))
with open('rough.py', 'w') as f:
    f.write(new_file)
