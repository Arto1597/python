""" cocas = ['Coca cola', 'Fresca', 'Manzanita', 'Sprite', 'Yoli']
pepsis = ['Pepsi', 'Manzanita', 'Miranda', '7up', 'Toronjada']
new_list = []
for refresco in cocas:
    new_list.append(refresco)
for refresco in pepsis:
    if refresco in new_list:
        print(f'Refreso repetido {refresco}')
    else:
        new_list.append(refresco)
print(new_list)
 """
cocas = ['Coca cola', 'Fresca', 'Manzanita', 'Sprite', 'Yoli']
pepsis = ['Pepsi', 'Manzanita', 'Miranda', '7up', 'Toronjada']


""" new_list = []
for refresco in cocas:
    new_list.append(refresco)
for refresco in pepsis:
    if not refresco in new_list:
        new_list.append(refresco)
print(new_list) """
""" 
new_list= cocas + pepsis """
""" 
new_list= set(new_list)
new_list= list(new_list) """


new_list= list(set(cocas+ pepsis))

new_list.sort()

print(new_list)


