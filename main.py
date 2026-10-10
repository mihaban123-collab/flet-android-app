import flet as ft
import sys

#Всякие флаги и никнейм, уроки
back_info = False
username = None
answers = []
score = 0
# Функции
def main(page: ft.Page):
    global back_info, input_start_field
    page.title = "Codler Education"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
            ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=80,  # Расстояние по вертикали между текстом и полем ввода
            controls=[
                ft.Container(height=1),
                ft.Text("Прежде чем мы начнем, введите, пожалуйста, ваш никнейм", size=23, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                input_start_field,
                ft.Button("Продолжить",
                          on_click= next_main_menu,
                          style = ft.ButtonStyle(
                          shape=ft.RoundedRectangleBorder(),
                          padding = 30,
                          color = ft.Colors.PURPLE
                          )
                                )
            ],
        )
    )
# функция закрытия приложухи
def close_app(e):
    e.page.run_task(e.page.window.destroy)
#Итоговое тестирование: Первая задача
def first_final_task(e: ft.Event[ft.Button]):
    e.page.controls.clear()
    first_final_ans = ft.TextField(label="Ответ", width=300, max_length = 6)
    e.page.add(
         ft.Row(alignment=ft.Alignment.TOP_LEFT,
                  controls=[ft.Text("Задача 1 (5 баллов)", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                            ]
                ),
         ft.Column(ft.Container(height=60)),
         ft.Row(
             alignment = ft.MainAxisAlignment.START,
             controls=[
                 ft.Text("Выберите все правильные названия переменных. В ответе укажите ряд чисел без пробелов и\nзнаков препинания", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)
                         ]
             ),
         ft.Row(
             alignment = ft.MainAxisAlignment.START,
             controls=[
                 ft.Text("1. user_score\n2. 2nd_player\n3. total-amount\n4. _bonus_points\n5. shrek3\n6. my name", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
                         ]
             ),
         ft.Column(ft.Container(height=90)),
         ft.Column(
             alignment=ft.Alignment.CENTER,
             spacing = 150,
             controls=[
                 first_final_ans,
                 ft.Button(
                     "Дальше",
                on_click = lambda e: second_final_task(e, first_final_ans),
                style = ft.ButtonStyle(
                shape=ft.BeveledRectangleBorder(),
                padding = 40,
                color = ft.Colors.PURPLE)
                )
                 ]
             )
         )
def second_final_task(e: ft.Event[ft.Button], first_final_ans):
    global answers, score
    if first_final_ans.value != "145":
        answers.append(first_final_ans.value)
    else:
        score += 5
        answers.append(first_final_ans.value)
    e.page.controls.clear()
    second_final_ans = ft.TextField(label="Ответ", width=300, max_length = 1)
    e.page.add(
         ft.Row(alignment=ft.Alignment.TOP_LEFT,
                  controls=[ft.Text("Задача 2 (10 баллов)", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                            ]
                ),
         ft.Column(ft.Container(height=60)),
         ft.Row(
             alignment = ft.MainAxisAlignment.START,
             controls=[
                 ft.Text("Выберите правильное определение конкатенации. В ответ укажите цифру ответа", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)
                         ]
             ),
         ft.Row(
             alignment = ft.MainAxisAlignment.START,
             controls=[
                 ft.Text("1. Процесс последовательного соединения двух или более строк в одну новую строку. В Python эта операция\nобычно выполняется с помощью знака плюс (+), например: 'Пи' + 'тон' превратится в 'Питон'\n2. Конкатенация — это математическая операция, при которой значения\nчисловых переменных складываются и автоматически округляются до ближайшего целого числа.\n3.Конкатенация — это специальный режим работы функции print(), который\nавтоматически переводит все англоязычные слова в коде на русский язык при выводе на экран.", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
                         ]
             ),
         ft.Column(ft.Container(height=90)),
         ft.Column(
             alignment=ft.Alignment.CENTER,
             spacing = 150,
             controls=[
                 second_final_ans,
                 ft.Button(
                     "Дальше",
                on_click = lambda e: third_final_task(e, second_final_ans),
                style = ft.ButtonStyle(
                shape=ft.BeveledRectangleBorder(),
                padding = 40,
                color = ft.Colors.PURPLE)
                )
                 ]
             )
         )
def third_final_task(e: ft.Event[ft.Button], second_final_ans):
    global answers, score
    if second_final_ans.value != "1":
        answers.append(second_final_ans.value)
    else:
        score += 10
        answers.append(second_final_ans.value)
    e.page.controls.clear()
    third_final_ans = ft.TextField(label="Ответ", width=300, max_length = 75)
    e.page.add(
         ft.Row(alignment=ft.Alignment.TOP_LEFT,
                  controls=[ft.Text("Задача 3 (15 баллов)", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                            ]
                ),
         ft.Column(ft.Container(height=60)),
         ft.Row(
             alignment = ft.MainAxisAlignment.START,
             controls=[
                 ft.Text("Дан код. В текстовое поле запишите результат работы программы.\nЕсли программа выдаст ошибку, то в ответ запишите 0.", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)
                         ]
             ),
         ft.Row(
             alignment = ft.MainAxisAlignment.START,
             controls=[
                 ft.Text("first_part = 'Вот она '\nsecond_part = 'и последняя'\nthird_part = ' задача курса :( |'\nnum_1 = 2 * 2 + 1\nnum_2 = 3 % 2\nprint(first_part + second_part + third_part, num_1 + num_2, 'задач было решено вами.')", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
                         ]
             ),
         ft.Column(ft.Container(height=90)),
         ft.Column(
             alignment=ft.Alignment.CENTER,
             spacing = 150,
             controls=[
                 third_final_ans,
                 ft.Button(
                     "Завершить тест",
                     on_click = lambda e: final_menu(e, third_final_ans),
                style = ft.ButtonStyle(
                shape=ft.BeveledRectangleBorder(),
                padding = 40,
                color = ft.Colors.PURPLE)
                )
                 ]
             )
         )
def final_menu(e: ft.Event[ft.Button], third_final_ans):
    global answers, score, username
    if third_final_ans.value != "Вот она и последняя задача курса :( | 6 задач было решено вами.":
        answers.append(third_final_ans.value)
        final_test_btn.visible = False
    else:
        score += 15
        answers.append(third_final_ans.value)
    if 0 <= score <= 5:
        final_speech = ft.Text(f"{username}, к сожалению вы не очень хорошо поняли программу курса. Советуем повторить теорию и попробывать разобраться самим", size=21, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)
    elif 5 < score <= 15:
        final_speech = ft.Text(f"{username}, неплохой результат, но есть пробелы. Их нужно срочно закрывать! Советуем повторить теорию.", size=21, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)
    else:
        final_speech = ft.Text(f"{username}, невероятная работа! Вы великолепно поняли программу курса. Вам стоит незамедлительно продолжить изучение Python.", size=21, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)
    e.page.controls.clear()
    e.page.add(
        ft.Column(alignment = ft.Alignment.TOP_CENTER,
            controls = [
                ft.Text("Результаты итогового тестирования", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)
                ]
            ),
        ft.Row(alignment = ft.MainAxisAlignment.START,
               controls = [
                ft.Text(f"1-ая задача правильный ответ: 145; ваш ответ - {answers[0]}\n2-ая задача правильный ответ: 1; ваш ответ - {answers[1]}\n3-ая задача правильный ответ: 'Вот она и последняя задача курса :( | 6 задач было решено вами.'; ваш ответ -\n'{answers[2]}'", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
                ]
               ),
        ft.Column(alignment = ft.Alignment.TOP_CENTER,
            controls = [
                ft.Container(height = 60)
                ]
            ),
        ft.Row(alignment = ft.MainAxisAlignment.START,
               controls = [
                ft.Text(f"Итого баллов: {score}/30", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
                ]
               ),
        ft.Column(alignment = ft.Alignment.TOP_CENTER,
            controls = [
                ft.Container(height = 60)
                ]
            ),
        ft.Row(alignment = ft.MainAxisAlignment.START,
               controls = [
                final_speech
                ]
               ),
        ft.Column(alignment = ft.Alignment.TOP_CENTER,
            controls = [
                ft.Container(height = 60)
                ]
            ),
        ft.Column(
                    alignment = ft.Alignment.TOP_CENTER,
                     controls=[
                         ft.Button(
                            "Обратно\nв меню",
                            on_click=next_main_menu,
                            style = ft.ButtonStyle(
                            shape=ft.BeveledRectangleBorder(),
                            padding = 40,
                            color = ft.Colors.PURPLE)
                     )
                 ]
             )
        )
# Итоговое тестирование: Начальное окно
def final_test_start(e: ft.Event[ft.Button]):
    global username
    e.page.controls.clear()
    e.page.add(
            ft.Column(alignment=ft.Alignment.TOP_CENTER,
                  controls=[ft.Text("Итоговое тестирование", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                  ),
            ft.Row(alignment=ft.MainAxisAlignment.START,
                   controls=[
                       ft.Text(f'{username}, вы начинаете итоговое тестирование.\nПри нажатии кнопки снизу оно начнется.\nТест состоит из трех задач.\nБудьте внимательны при сдаче ответа! Он принимается только один раз!\nПравильные ответы и количество баллов вы сможете увидеть при окончании тестирования.\nТестирование можно пройти только один раз.\nЕсли вы хотите еще повторить теорию, перейдите в главное меню и откройте нужный вам урок.', size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                   ),
            ft.Column(ft.Container(height=170)),
            ft.Column(
            alignment = ft.Alignment.TOP_CENTER,
            spacing = 50,
            controls=[
                      ft.Button(
                          "Начать",
                          on_click = first_final_task,
                          style = ft.ButtonStyle(
                              color = ft.Colors.PURPLE,
                              shape = ft.RoundedRectangleBorder(),
                              padding = 40)
                          )
                      ]
            ),
            ft.Column(ft.Container(height=90)),
            ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                     controls=[
                         ft.Button(
                            "Обратно\nв меню",
                            on_click=next_main_menu,
                            style = ft.ButtonStyle(
                            shape=ft.BeveledRectangleBorder(),
                            padding = 20,
                            color = ft.Colors.PURPLE)
                     )
                 ]
             )
            )
# функция для открытия окна с информацией о разработчиках
def information(e: ft.Event[ft.Button]):
    global username
    e.page.controls.clear()
    e.page.add(
        ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing = 40,
            controls=[
                ft.Text(f"Это наша команда разработчиков, {username}", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                ft.Text("Разработчик: Сидоренко Михаил", size=17, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                ft.Text("Дизайнер №1: Кривенко Егор", size=17, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                ft.Text("Дизайнер №2: Сидоренко Михаил", size=17, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                ft.Text("Презентатор: Кривенко Егор ", size=17, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                ft.Text("Методист: Сидоренко Михаил ", size=17, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                ft.Text("Тестировщик: Сидоренко Михаил", size=17, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                ft.Container(height=130)
                ]
            ),
        ft.Row(
            alignment=ft.Alignment.BOTTOM_LEFT,
            controls=[ft.Button(
                "Вернуться",
                on_click= next_main_menu,
                style = ft.ButtonStyle(
                shape=ft.BeveledRectangleBorder(),
                padding = 20,
                color = ft.Colors.PURPLE)
                )
                        ]
            )
        )
#Задача первого урока
def task_first(e: ft.Event[ft.Button]):
    e.page.controls.clear()
    first_ans = ft.TextField(label="Ответ", width=300)
    e.page.add(
         ft.Row(alignment=ft.Alignment.TOP_LEFT,
                  controls=[ft.Text("Дан код. В текстовое поле запишите результат работы программы", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                            ]
                ),
         ft.Column(ft.Container(height=60)),
         ft.Row(
             alignment = ft.MainAxisAlignment.START,
             controls=[
                 ft.Text("greeting = 'Привет любителям Python!'\ngreeting_2 = 'Добро пожаловать на наш курс!'\nprint(greeting, greeting_2)", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
                         ]
             ),
         ft.Column(ft.Container(height=90)),
         ft.Column(
             alignment=ft.Alignment.CENTER,
             spacing = 150,
             controls=[
                 first_ans,
                 ft.Button(
                     "Проверить",
                on_click= lambda e: check_ans_first(e, first_ans),
                style = ft.ButtonStyle(
                shape=ft.BeveledRectangleBorder(),
                padding = 40,
                color = ft.Colors.PURPLE)
                )
                 ]
             ),
         ft.Row(
             alignment=ft.MainAxisAlignment.START,
             controls=[
                 ft.Button(
                    "Обратно\nв меню",
                    on_click=next_main_menu,
                    style = ft.ButtonStyle(
                    shape=ft.BeveledRectangleBorder(),
                    padding = 20,
                    color = ft.Colors.PURPLE)
                     )
                 ]
             )
         )
# Проверка первой задачи
def check_ans_first(e: ft.Event[ft.Button], first_ans):
    global second_lesson
    check = first_ans.value
    if check == "Привет любителям Python! Добро пожаловать на наш курс!":
        e.page.show_dialog(ft.SnackBar(ft.Text("Бинго! Открыт следующий урок.", size = 22)))
        e.page.update()
        second_lesson.disabled = False
    else:
        e.page.show_dialog(ft.SnackBar(ft.Text("Пока-что неправильно. Попробуй еще раз.", size = 22)))
# Теория первого урока
def first_lesson_theory(e: ft.Event[ft.Button]):
    e.page.controls.clear()
    e.page.add(
        ft.Column(alignment=ft.Alignment.TOP_CENTER,
                  controls=[ft.Text("Теория", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                  ),
         ft.Row(alignment=ft.Alignment.TOP_LEFT,
                  controls=[ft.Text("Переменная - это хранилище с именем, в которую можно положить информацию (данные) чтобы использовать её позже.\nВ Python, чтобы создать переменную, нужно написать её имя, поставить знак = (оператор присваивания) и указать значение.\nЖелательно, имена переменных должны быть понятны, чтобы позже не забывать их предназначение (Например, name, а не n)", size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)
                            ]
                  ),
        ft.Column(alignment=ft.Alignment.TOP_CENTER,
                  controls=[ft.Text("Правила присваивания имен переменным", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                  ),
        ft.Row(alignment=ft.Alignment.TOP_LEFT,
                  controls=[ft.Text("1. Переменная не должна начинаться с цифры.\n2.Пробелы и спец. символы (@, !, - т.д., но не знак подчеркивания _) запрещены!\n3. Называть переменные русскими буквами не стоит, так как некоторые компиляторы не смогут прочесть имя переменной\n(программки, в которых работаешь с Python, не поймут написанного).\n4. Python различает регистр, поэтому две переменные age и Age - разные.\n5. Зарезервированные слова под функции(вроде print, if, else и т.д.) нельзя использовать как имя переменной", size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)
                            ]
                ),
        ft.Column(alignment=ft.Alignment.TOP_CENTER,
                  controls=[ft.Text("Функция print()", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                  ),
         ft.Row(alignment=ft.Alignment.TOP_LEFT,
                  controls=[ft.Text("print() - встроенная функция в Python. При помощи нее можно выводить текст или какие-либо данные на экран.\nЧтобы вывести на экран число, будет достаточным написания напрямую. Например, print(2) - выведет 2.\nПритом, чтобы вывести текст, его нужно заключить (ограничить) кавычками. Например, print('Hello World'), выведет Hello world.\nПодойдут как двойные, так и одиночные кавычки. Чтобы вывести значение переменной достаточно написать ее название между скобками.\nЕсли в переменной текст, не нужно заключать имя переменной в кавычки. Таким образов выведется: Имя переменной.\nЕсли необходимо ввести несколько значений, между названиями переменных или текстами, ограниченными кавычками, или числами, ставим запятую.\nТак, программа выведет нужное через пробел", size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)
                            ]
                ),
        ft.Column(alignment=ft.Alignment.TOP_CENTER,
                  controls=[ft.Text("Пример", size=23, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                  ),
        ft.Row(alignment=ft.Alignment.TOP_LEFT,
                  controls=[ft.Text("age = 3\nname = 'Егор'\nprint(age)\nprint(name)\nВывод:\n3\nЕгор", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
                            ]
                ),
        ft.Column(
            alignment=ft.Alignment.CENTER,
            controls=[
                ft.Button(
                    "Дальше",
                    on_click=task_first,
                    style=ft.ButtonStyle(
                    color=ft.Colors.PURPLE,
                    shape=ft.RoundedRectangleBorder(),
                    padding=30
                    )
                )
            ]
        )
    )
def check_ans_second(e: ft.Event[ft.Button], second_ans):
    global third_lesson
    check = second_ans.value
    if check == "9 девять":
        e.page.show_dialog(ft.SnackBar(ft.Text("Абсолютно верно! Можете приступать к следующему уроку.", size = 22)))
        e.page.update()
        third_lesson.disabled = False
    else:
        e.page.show_dialog(ft.SnackBar(ft.Text("Пока-что неправильно. Помните - на ошибках учатся!", size = 22)))
def task_second(e: ft.Event[ft.Button]):
    second_ans = ft.TextField(label = "Ответ", width=300)
    e.page.controls.clear()
    e.page.add(
        ft.Row(
            alignment = ft.MainAxisAlignment.START,
            controls=[
                ft.Text("Дан код. В текстовое поле запишите результат работы программы.", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
            ),
        ft.Column(
            alignment = ft.Alignment.TOP_CENTER,
            controls=[ft.Container(height=90)]
            ),
        ft.Row(
            alignment = ft.MainAxisAlignment.START,
            controls=[ft.Text("ans = 3\nans2 = ans\nans //= 2\nans += 8\nans_w = 'девять'\nprint(ans, ans_w)", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)]
            ),
        ft.Column(
            alignment = ft.Alignment.TOP_CENTER,
            spacing = 50,
            controls=[second_ans,
                      ft.Button(
                          "Проверить",
                          on_click = lambda e: check_ans_second(e, second_ans),
                          style = ft.ButtonStyle(
                              color = ft.Colors.PURPLE,
                              shape = ft.RoundedRectangleBorder(),
                              padding = 40)
                          )
                      ]
        ),
        ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                     controls=[
                         ft.Button(
                            "Обратно\nв меню",
                            on_click=next_main_menu,
                            style = ft.ButtonStyle(
                            shape=ft.BeveledRectangleBorder(),
                            padding = 20,
                            color = ft.Colors.PURPLE)
                     )
                 ]
             )
        )
# Теория второго урока
def second_lesson_theory(e: ft.Event[ft.Button]):
    e.page.controls.clear()
    e.page.add(
            ft.Column(alignment=ft.Alignment.TOP_CENTER,
                  controls=[ft.Text("Теория", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                  ),
            ft.Row(alignment=ft.MainAxisAlignment.START,
                   controls=[
                       ft.Text("Из прошлого урока мы узнали, как создавать переменную. Однако она может и менять свое значение.\nНапример, сначала задав значение переменной x = 5, его можно поменять, и сделать значение переменной, например, x = 10.\nПрисваивание нового значения аналогичен созданию переменной. Пишем название переменной, оператор присваивания (=) и новое значение.\nВ Python переменная может сначала хранить число, а после строку. Например, сначала age = 15, а после age = 'пятнадцать'.", size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                   ),
            ft.Column(alignment=ft.Alignment.TOP_CENTER,
                  controls=[ft.Text("Операции сложения, вычитания, умножения и деления", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                  ),
            ft.Row(alignment=ft.MainAxisAlignment.START,
                   controls=[
                       ft.Text("Для того, чтобы прибавлять, вычитать, умножать и делить значения, а также изменять числовые значения внутри переменной используются арифметические\nоператоры. Чтобы сложить, используем оператор '+' (без ковычек); чтобы вычесть, используем '-' (без ковычек); чтобы умножить, используем '*' (без ковычек);\nчтобы делить, используем '/' (без ковычек)\nТакже, часто используется оператор нахождения остатка от деления '%' (без ковычек); и целочисленное деление (только целая часть) '//'. (без ковычек)\nНапример, чтобы вывести 2 + 2, пишем print(2 + 2), что выведет 4. Аналогично можно вывести 2 - 2, пишем print(2 - 2), что выведет 0. Чтобы вывести\nпроизведение 3 на 2, пишем print(3 * 2), что выводит 6. Аналогично деление 6 на 2 записывается как print(6 / 2), что выводит 3.0, притом всегда выводится\nдробная часть, даже если равна нулю. Чтобы выводить без нее, используется оператор '//', т.е. print(6 // 2), выведет 3. Иногда в задачах может пригодиться\nостаток от деления, поэтому, например, чтобывывести остаток от деления 3 на 2, пишем print(3 % 2), что выводит 1",size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                   ),
            ft.Row(alignment=ft.MainAxisAlignment.START,
                   controls=[ft.Text("Однако переменные тоже можно изменять. Например, переменную x = 13 можно увеличить на 2, таким образом x становиться равным: x = x + 2.\n Теперь переменная x равна 15. Аналогично работает с остальными арифметическими операторами. Однако, запись x = x + 2; x = x - 4; и т.д. операторами\nприсваивания. Например x = x + 2 заменяется x += 2. Аналогично x -= 1 и x = x - 1 одинаковы.\nТо есть любой оператор присваивания принимает такой вид: имя переменной арифметический_оператор= число, на которое мы прибавляем, умножаем, ищем\nостаток от деления и т.д.", size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)
                       ]
                   ),
            ft.Column(alignment=ft.Alignment.TOP_CENTER,
                      spacing = 20,
                      controls=[
                          ft.Text("Пример", size = 28, weight = ft.FontWeight.BOLD, color = ft.Colors.PURPLE),
                          ]
                      ),
            ft.Row(alignment = ft.MainAxisAlignment.START,
                   controls = [
                       ft.Text("x = 4        |Вывод:\nprint(x)    | 4\nx += 3      | 7\nprint(x)    | 1\nx -= 6       | 3\nprint(x)    | 1\nx *= 3       | один\nprint(x)     |\nx %= 2      |\nprint(x)     |\nx = 'один'|\nprint(x)     |", size = 18, weight = ft.FontWeight.BOLD, color = ft.Colors.BLUE)]
                   ),
            ft.Column(alignment = ft.Alignment.TOP_CENTER,
                      controls=[ft.Button(
                          "Дальше",
                          on_click = task_second,
                          style=ft.ButtonStyle(
                              color=ft.Colors.PURPLE,
                              shape=ft.RoundedRectangleBorder(),
                              padding=30)
                          )
                                ]
                      )
        )
def check_ans_third(e: ft.Event[ft.Button], third_ans):
    global final_test_btn
    check = third_ans.value
    if check == "Даша и Саша: 60 очков":
        e.page.show_dialog(ft.SnackBar(ft.Text("Невероятная работа! Вам доступно итоговое тестирование!", size = 22)))
        e.page.update()
        final_test_btn.disabled = False
    else:
        e.page.show_dialog(ft.SnackBar(ft.Text("Неправильно. Попробуйте еще раз.", size = 22)))
def third_task(e: ft.Event[ft.Button]):
    third_ans = ft.TextField(label = "Ответ", width=300)
    e.page.controls.clear()
    e.page.add(
        ft.Row(
            alignment = ft.MainAxisAlignment.START,
            controls=[
                ft.Text("Дан код. В текстовое поле запишите результат работы программы.", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
            ),
        ft.Column(
            alignment = ft.Alignment.TOP_CENTER,
            controls=[ft.Container(height=90)]
            ),
        ft.Row(
            alignment = ft.MainAxisAlignment.START,
            controls=[ft.Text("num_1 = 5\nnum_2 = 25\nnum_3 = 2\nfirst_name = 'Даша'\nunited = ' и '\nsecond_name = 'Саша'\nprint(first_name + united + second_name + ':', (num_1 + num_2) * 2, 'очков')", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)]
            ),
        ft.Column(
            alignment = ft.Alignment.TOP_CENTER,
            spacing = 65,
            controls=[third_ans,
                      ft.Button(
                          "Проверить",
                          on_click = lambda e: check_ans_third(e, third_ans),
                          style = ft.ButtonStyle(
                              color = ft.Colors.PURPLE,
                              shape = ft.RoundedRectangleBorder(),
                              padding = 40)
                          )
                      ]
        ),
        ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                     controls=[
                         ft.Button(
                            "Обратно\nв меню",
                            on_click=next_main_menu,
                            style = ft.ButtonStyle(
                            shape=ft.BeveledRectangleBorder(),
                            padding = 20,
                            color = ft.Colors.PURPLE)
                     )
                 ]
             )
        )
def third_lesson_theory(e: ft.Event[ft.Button]):
    e.page.controls.clear()
    e.page.add(
        ft.Column(alignment=ft.Alignment.TOP_CENTER,
                  controls=[ft.Text("Математические выражения с переменными", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                  ),
        ft.Row(alignment=ft.MainAxisAlignment.START,
                   controls=[
                       ft.Text("Из прошлого урока мы научились арифметическим действиям с числами, однако переменные при работе с математическими операциями работают аналогично.\nВозьмем переменную x = 5, и y = 3. Если мы хотим записать в переменную total сумму этих двух чисел, то запись будет выглядить как: total = x + y.\nВ итоге total будет равняться 8. Ровно таким же образом можно вывести их сумму. То есть можно написать print(x + y), что выведет 8.", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                   ),
        ft.Column(alignment=ft.Alignment.TOP_CENTER,
                  controls=[ft.Text("Приоритет операций с переменными и числами", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                  ),
        ft.Row(alignment=ft.MainAxisAlignment.START,
                   controls=[
                       ft.Text("Приоритет действий с числами и переменными аналогичны математическим. Напомним:\n1. Действия в скобочках ()\n2. Операции умножения и деления.\n3. Операции сложения и вычитания.\nПритом важно знать, что математический пример читается слева-направо, то есть высшим приоритетом обладают левые действия. Например, в примере x * y / z,\nнаивысшим приоритетом обладает операция x * y, а после идет результат произведения x на y, деленное на z. Рассмотрим пример: result = (a + b) * c + d.\nВ данном случае наивысший приоритет у суммы a + b, так как она находиться в скобочках. После пойдет умножение на c, а в конце к результату будет\nприбавлено d.", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                   ),
        ft.Column(alignment=ft.Alignment.TOP_CENTER,
                  controls=[ft.Text("Конкатенация", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                  ),
        ft.Row(alignment=ft.MainAxisAlignment.START,
                   controls=[
                       ft.Text("Иногда в задачах необходимо соединить строки воедино, чтобы получить искомый ответ. Для этого можно складывать строки арифметическим знаком \n'+'. Такое преобразование называется конкатенация. Например, если name = 'Михаил', то print('Привет ' + name) выведет: Привет Михаил.\nПритом при складывании строк пробела между ними нету!\nАналогичным образом складываются и переменные. То есть если score = ' пять', а leader = 'Кощей:', то print(score + leader) выведется - Кощей: пять", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)]
                   ),
        ft.Column(alignment=ft.Alignment.TOP_CENTER,
                  controls=[ft.Button(
                      "Дальше",
                          on_click = third_task,
                          style=ft.ButtonStyle(
                              color=ft.Colors.PURPLE,
                              shape=ft.RoundedRectangleBorder(),
                              padding=30)
                      )
                            ]
                  ),
        )
    
# Возможные уровни приложухи
def levels_list(e: ft.Event[ft.Button]):
    global username
    e.page.controls.clear()
    e.page.add(
        ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=50,
            controls=[
                ft.Text(f"Выберите урок, {username}", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                ft.Button(
                    "Создание\nпеременной",
                    on_click=first_lesson_theory,
                    style = ft.ButtonStyle(
                        color = ft.Colors.PURPLE,
                        shape = ft.CircleBorder(),
                        padding = 55
                        )
                    ),
                second_lesson,
                third_lesson,
                ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                     controls=[
                         ft.Button(
                            "Обратно\nв меню",
                            on_click=next_main_menu,
                            style = ft.ButtonStyle(
                            shape=ft.BeveledRectangleBorder(),
                            padding = 20,
                            color = ft.Colors.PURPLE)
                     )
                 ]
             )
                ]
            )
        )
    
# функция запуска главного меню и проверка ника
def next_main_menu(e: ft.Event[ft.Button]):
    global back_info, username
    if back_info is False:
        username = input_start_field.value
        if len(username) < 3:
            e.page.show_dialog(ft.SnackBar(ft.Text("Никнейм должен содержать хотя-бы 3 символа!", size = 22)))
            return
        elif len(username) >= 3:
            back_info = True
            pass
    else:
        pass
    e.page.controls.clear()
    e.page.add(
        ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing = 60,
            controls=[
            ft.Text(f"Здравствуй, {username}", size=25, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
            ft.Button("Начать обучение",
            on_click= levels_list,
            style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(),
            padding = 30,
            color = ft.Colors.PURPLE
            )),
            final_test_btn,
            ft.Button("Информация о разработчиках",
            on_click=information,
            style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(),
            padding = 30,
            color = ft.Colors.PURPLE
            )),
            ft.Button("Выход из приложения",
            on_click= close_app,
            style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(),
            padding = 30,
            color = ft.Colors.PURPLE
            ))
            ]
            )
            )
#Уроки и стартовое поле ввода
second_lesson = ft.Button("Изменение\nзначения\nпеременной", on_click=second_lesson_theory, disabled = True, style=ft.ButtonStyle(color = ft.Colors.PURPLE, shape = ft.CircleBorder(), padding = 50))
third_lesson = ft.Button("Переменные\nв выражениях", on_click = third_lesson_theory, disabled = True, style=ft.ButtonStyle(color = ft.Colors.PURPLE, shape = ft.CircleBorder(), padding = 55))
final_test_btn = ft.Button("Итоговое тестирование", on_click=final_test_start, visible = True, disabled = True, style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(), padding = 30, color = ft.Colors.PURPLE))
input_start_field = ft.TextField(label="Никнейм", max_length=16, width=300)
ft.run(main)
