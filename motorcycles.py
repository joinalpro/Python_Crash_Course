motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles[0] = 'ducati'
# print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)
new_moto_list = []
new_moto_list.append('Yamaha')
new_moto_list.append('Honda')
new_moto_list.append('Suzuki')
new_moto_list.insert(0, 'ducati')
print(new_moto_list)
# del new_moto_list[0]
# pop() removing last items from the list
new_moto_list.pop()
print(new_moto_list)
