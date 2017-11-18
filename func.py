def get_summ(one, two, delimeter=' '):
    return str.upper(one) + str(delimeter) + str.upper(two)

print(get_summ('hello', 'world'))

def get_summ2(one, two, delimeter=' '):
	return one.upper() + delimeter + two.upper()

print(get_summ2('hello', 'world'))

