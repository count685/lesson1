names = {
	'Anton': {'city': 'Moscow', 'temperature': 25, 'wind': 'nord'}, 
	'Kate': {'city': 'Barcelona', 'temperature': 30, 'wind': 'east'}, 
	'Mike': {'city': 'Moscow', 'temperature': 25, 'wind': 'nord'},
}
a = input('Введите имя:')
print(names.get(a)['city'], names.get(a)['temperature'])
