# Создать программу, которая запрашивает у пользователя произвольную строку символов. Далее программа ее шифрует и
# выводит на экран в зашифрованном виде. Шифрование происходит путем замены каждого символа символом, который находится
# на 5 позиций правее в предопределенной таблице шифрования. Таблица шифрования задается программистом в виде
# одномерного списка символов латинского алфавита от a до z и цифр от 0 до 9. Если при выборе символа для шифровки
# таблица шифрования заканчивается, то циклически переходить к ее началу. Отсутствующие в таблице шифрования символы,
# записываются в результирующую строку без изменений. Регистр игнорируется.
#    	Таблица шифрования (a, b, c, d, ..., x, y, z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# 	    Например: Исходная строка, которую ввел пользователь: 'secret', 'office 365'
# 	    Зашифрованная строка, которую выдала программа: 'xjhwjy', 'tkknhj 8ba'
# 	    Примечание: т.н. таблица шифрования может быть представлена как строка или список.
