# Лабораторная работа №8.1. Прототип запроса к базе данных

## Практическое задание
1. В этом задании ваша цель — научить Анфису отвечать на вопрос «Кто все мои друзья?». Ответ Анфисы должен быть примерно таким:
2. Допишите в конец программы вызов функции process_anfisa() с аргументом 'Где все мои друзья?'. В теле функции process_anfisa() добавьте ещё одно условие elif, которое будет проверять, содержит ли переменная query строку 'Где все мои друзья?'. В теле нового блока elif пока что напишите return ‘Я поняла, это вопрос про города!’: списком городов вы займётесь в следующем задании, а пока Анфиса просто даст знать, что она поняла суть вопроса.
3. Удалите из кода строку return 'Я поняла, это вопрос про города!': на этом месте вам нужно написать код, который создаст перечень городов из словаря DATABASE (города в этом перечне не должны повторяться); вернёт фразу Твои друзья в городах: <город_1> <город_2> <город_3> … (города должны перечисляться через пробел).