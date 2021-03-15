import eel

eel.init('web')													# Путь к папке с HTML


@eel.expose														# Надо
def NumberTranslator(num):										# Функция, переводящая цифры на английский
	if num == '':
		return None
	else:
		num = ''.join(str(num).split())
		try:
			# Числа с 0 по 9
			first = {
				0: 'zero', 
				1: 'one', 
				2: 'two', 
				3: 'three', 
				4: 'four', 
				5: 'five', 
				6: 'six', 
				7: 'seven', 
				8: 'eight', 
				9: 'nine'
			}
			# Числа с 10 по 19
			second = {
				10: 'ten', 
				11: 'eleven', 
				12: 'twelve', 
				13: 'thriteen', 
				14: 'fourteen', 
				15: 'fiteen', 
				16: 'sixteen', 
				17: 'seventeen', 
				18: 'eighteen', 
				19: 'nineteen'
			}
			# Числа с 20 по 90
			thrid = {
				20: 'twenty', 
				30: 'thirty', 
				40: 'forty', 
				50: 'fifty', 
				60: 'sixty', 
				70: 'seventy', 
				80: 'eighty', 
				90: 'ninety'
			}
			# Степени десятки
			infinity = {
				10**2: 'hundred', 
				10**3: 'thousand', 
				10**6: 'million', 
				10**9: 'billion',
				10**12: 'trillion', 
				10**15: 'quadrillion', 
				10**18: 'quintillion', 
				10**21: 'sextillion',
				10**24: 'septillion', 
				10**27: 'octillion', 
				10**30: 'nonillion', 
				10**33: 'decillion',
				10**36: 'undecillion', 
				10**39: 'duodecillion'
			}
			
			num = int(num)
			key = len(str(abs(num)))
			# Ограничитель
			if key > 30:
				return "The number is too large"
			# Проверка на отрицание
			elif num != abs(num):
				return ('negative ' + NumberTranslator(abs(num))).title()
			# Числа с 0 по 9
			elif num in set(first):
				return (first[num]).title()
			# Числа с 10 по 19
			elif num in set(second):
				return (second[num]).title()
			# Числа из thrid
			elif num in set(thrid):
				return (thrid[num]).title()
			# Числа с 20 по 99
			elif key == 2:
				return (thrid[num // 10 * 10] + ' ' + NumberTranslator(num % 10)).title()
			# Числа со 100 по 900
			elif key == 3:
				return (NumberTranslator(num // 100) + ' ' + infinity[100] + ((' and ' + NumberTranslator(num % 100)) if num // 100 * 100 != num else '')).title()
			# Все остальные числа
			else:
				k = (key - 1) // 3 * 3
				return (NumberTranslator(num // 10 ** k) + ' ' + infinity[10 ** k] + ((' ' + NumberTranslator(num % 10 ** k)) if num // 10 ** k * 10 **k != num else '')).title()
		except ValueError:
			return 'Enter the number'
		except KeyError:
			return 'The number is too large'


eel.start('index.html', size=(400, 705))		# Запуск окна