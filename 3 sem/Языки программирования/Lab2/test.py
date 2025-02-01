import subprocess


def print_separator():
	print("---- ---- ---- ---- ---- ----")


def run_programm(input):
	result = subprocess.run("./main", capture_output=True, text=True, input=input)
	return result.stdout, result.stderr


def run_test(input, expected_stdout, expected_stderr):
	out, err = run_programm(input)
	print("Тестируемый ключ:", input)
	if (out == expected_stdout and err == expected_stderr):
		print("Тест успешно пройден")
	else:
		print("Ошибка")
		print("Ожидаемый вывод:", expected_stdout)
		print("Вывод программы:", out)
		print("Ожидаемый вывод ошибок:", expected_stderr)
		print("Вывод ошибок программы:", err)


def test_1():
	print("Запуска теста 1\n")
	input = "third 3\n"
	expected_stdout = "third word explanation???\n"
	expected_stderr = ""
	run_test(input, expected_stdout, expected_stderr)


def test_2():
	print("Запуска теста 2\n")
	input = "unfinded_key\n"
	expected_stdout = ""
	expected_stderr = "Не удалось найти ключ\n"
	run_test(input, expected_stdout, expected_stderr)


def test_3():
	print("Запуска теста 3\n")
	input = (
			"very_big_text_very_big_text_very_big_text_very_big_text_very_big_text_" 
			"very_big_text_very_big_text_very_big_text_very_big_text_very_big_text_"
			"very_big_text_very_big_text_very_big_text_very_big_text_very_big_text_"
			"very_big_text_very_big_text_very_big_text_very_big_text_very_big_text_"
			"very_big_text_very_big_text_very_big_text_very_big_text_very_big_text\n"
			)
	expected_stdout = ""
	expected_stderr = "Не удалось прочитать в буффер\n"
	run_test(input, expected_stdout, expected_stderr)


def test_4():
	print("Запуска теста 4\n")
	input = "\n"
	expected_stdout = ""
	expected_stderr = "Не удалось найти ключ\n"
	run_test(input, expected_stdout, expected_stderr)


def test_5():
	print("Запуска теста 5\n")
	input = (
		"test buffer size test buffer size test buffer size test buffer size "
		"test buffer size test buffer size test buffer size test buffer size "
		"test buffer size test buffer size test buffer size test buffer size "
		"test buffer size test buffer size test buffer size\n"
		)
	expected_stdout = "good buffer\n"
	expected_stderr = ""
	run_test(input, expected_stdout, expected_stderr)


def test_6():
	print("Запуска теста 6\n")
	input = (
		"test buffer size test buffer size test buffer size test buffer size "
		"test buffer size test buffer size test buffer size test buffer size "
		"test buffer size test buffer size test buffer size test buffer size "
		"test buffer size test buffer size test buffer size!\n"
		)
	expected_stdout = ""
	expected_stderr = "Не удалось прочитать в буффер\n"
	run_test(input, expected_stdout, expected_stderr)


subprocess.run(["make", "clean"])
subprocess.run("make")
print()

print("Starting tests")
print_separator()

tests = [test_1, test_2, test_3, test_4, test_5, test_6]
for test in tests:
	test()
	print_separator()
