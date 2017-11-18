question = input()
answers = {'привет': 'и тебе привет!', 'как дела': 'лучше всех', 'пока': 'Увидимся'}

def get_answer(question):
	return answers.get(question.lower(), 'Не понимаю, о чем ты.')

	
print(get_answer(question))
