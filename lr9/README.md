# Лабораторная работа №9. Библиотека Requests, исследование HTTP методов.

## Практическое задание
1. Используя библиотеку requests, реализуйте 2 функции выполняющий GET запрос, одна функция должна возвращать список студентов, вторая функция должна принимать параметр “номер студента” и возвращать информацию о конкретном студенте.
2. Используя библиотеку requests, реализуйте функцию принимающую в качестве параметра информацию о новом студенте и добавлющую ее на серве, функция должна возвращать ответ от сервера.
3. Реализуйте функцию которая будет принимать 2 параметра, первый = id студента, второй обновляемая инфомация. Функция должна возвращать строку ответа от сервера указанную в ожидаемом ответе.
4. Реализуйте функцию которая будет удалить информацию о студенте по id студента переданному в качестве параметра функции. Функция должна возвращать ответ от сервера.
5. Запустите Wireshark для looback интерфейса и захватите трафик который генерирует написанный вами клиент, для данного сервера. Расскрывая информацию о каждом http сообщение опишите что просиходит в данном дампе, какие есть заголовки и параметры у протокола http в запросе, какие в ответе. В каком формате передаються данные между сервером и клиентом? Почему кирилица отображаеться не коректно в дампе?

## Ответы на контрольные вопросы
**1. Расскрывая информацию о каждом http сообщение опишите что просиходит в данном дампе, какие есть заголовки и параметры у протокола http в запросе, какие в ответе.**
***Ответ:*** В запросе могут быть заголовки Host, User-Agent, Accept-Encoding, Accept, Connection, Content-Length, Content-Type. В ответе могут быть заголовки Server, Date, Content-Type, Content-Length, Connection.
**2. В каком формате передаються данные между сервером и клиентом?**
***Ответ:*** Содержимое сообщения передается текстом (массивы - тоже текстом, в формате JSON), указывается размер текста в байтах. Заголовки (параметры) передаются отдельно от "содержимого".
**3. Почему кирилица отображаеться не коректно в дампе?**
***Ответ:*** Кириллица отображается "некорректно" т.к. она не является стандартным символом ASCII и передается в формате управляющей последовательности - т.е. \uXXXX, где X - цифра из кода буквы.