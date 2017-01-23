all_dicts = {'a':{'name': 'A', 'city':'foo'},
             'b':{'name':'B', 'city':'bar'},
             'c':{'name':'C', 'city':'bar'},
             'd':{'name':'D', 'city':'foo'},
             'e':{'name':'E', 'city':'bar'}

            }
citys = {}

for key, value in all_dicts.items():
    citys[key] = value['city']

for key, value in citys.items():
    if value == 'bar':
        print(all_dicts[key])

""" lamda function """

specific_values=list(filter(lambda x: x['city'] == 'bar', all_dicts.values()))
print(specific_values)
