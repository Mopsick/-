import telebot
import types
from telebot import types

# Создание бота с указанием токена доступа
bot = telebot.TeleBot("7050489508:AAF48uBY22l_0c4A2is5eWEzi77h2Q4Q050")

workouts = {}



spravki = {
    "1": {
        "name": "Делители числа"
    },
    "2": {
        "name": "Кратные числа"
    },
    "3": {
        "name": "Признаки делимости на 10,5,2"
    },
    "4": {
        "name": "Признаки делимости на 9,3"
    },
    "5": {
        "name": "Простые и составные числа"
    },
    "6": {
        "name": "Разложение составных чисел на простые множители"
    },
    "7": {
        "name": "Наибольший общий делитель НОД"
    },
    "8": {
        "name": "Наименьшее общее кратное НОК"
    },
    "9": {
        "name": "Основное свойство дроби"
    },
    "10": {
        "name": "Сокращение дробей"
    },
    "11": {
        "name": "Приведение обыкновенных дробей к наименьшему общему знаменателю НОЗ"
    },
    "12": {
        "name": "Сравнение обыкновенных дробей"
    },
    "13": {
        "name": "Запись смешанного числа в виде неправильной дроби"
    },
    "14": {
        "name": "Запись натурального числа в виде неправильной дроби"
    },
    "15": {
        "name": "Сложение и вычитание смешанных чисел"
    },
    "16": {
        "name": "Умножение обыкновенных дробей"
    },
    "17": {
        "name": "Взаимно обратные числа"
    },
    "18": {
        "name": "Деление обыкновенных дробей"
    },
    "19": {
        "name": "Проценты (%)"
    },
    "20": {
        "name": "Задачи на нахождение части и целого"
    },
    "21": {
        "name": "Отрицательные и положительные числа"
    },
    "22": {
        "name": "Координаты на прямой"
    },
    "23": {
        "name": "Сравнение чисел с помощью числовой оси"
    },
    "24": {
        "name": "Противоположные числа"
    },
    "25": {
        "name": "Модуль числа"
    },
    "26": {
        "name": "Рациональные числа"
    },
    "27": {
        "name": "Коэффициент"
    },
    "28": {
        "name": "Правило раскрытия скобок"
    },
    "29": {
        "name": "Подобные слагаемые"
    },
    "30": {
        "name": "Решение линейных уравнений"
    },
    "31": {
        "name": "Координатная плоскость. Координата точки"
    }
}

spravki1 = {
    "1": {
        "name": "Угол"
    },
    "2": {
        "name": "Уголовой градус, измерение углов"
    },
    "3": {
        "name": "Окружность, круг"
    },
    "4": {
        "name": "Взаимное расположение двух прямых на плоскости"
    }
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "\U0001F590"

    bot.reply_to(message,
                 f"Привет!{text} Добро пожаловать в чат-бот. Меня зовут Георгий, я твой помощник при изучении математики в 6 классе!")
    text2 = "\U0001f468\u200D\U0001f3eb"
    bot.send_message(message.chat.id, text=text2)
    msq = bot.send_message(message.chat.id, 'Давай познакомимся, как тебя зовут?')

    bot.register_next_step_handler(msq, hi)


def hi(message):
    text1 = "\U0001F609"
    bot.send_message(message.chat.id, f'Вот мы и познакомились!{text1} Рад знакомству!')
    keyboard = generate_keyboard()

    bot.send_message(message.chat.id, text="Выбери раздел ", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    text1 = "\U0000270F"
    bot.send_message(call.message.chat.id, f"Вы выбрали {call.data} ")
    # add_workout(call.message)
    if call.data == f"Математика{text1}":
        guide(call.message)


    else:
        guide1(call.message)


def generate_keyboard():
    text = "\U0001F4CC"
    text1 = "\U0000270F"
    keyboard = types.InlineKeyboardMarkup()

    mood = [f"Математика{text1}", f"Начальные сведения из геометрии{text}"]
    for button_text in mood:
        button = types.InlineKeyboardButton(text=button_text, callback_data=button_text)

        keyboard.add(button)
    return keyboard




@bot.message_handler(commands=['guide'])
def guide(message):
    text = "\U0001F447"
    text1 = "\U0001F393"
    chat_id = message.chat.id
    bot.send_message(message.chat.id, f"Напиши номер пункта, который хочешь изучить{text}  А для следующей темы, ты можешь использовать моё Меню) Также, изучив все разделы, ты можешь подготовиться к ВПР!")
    for key, workout in spravki.items():
        bot.send_message(chat_id,
                         f"{text1}{key}.{workout['name']}")
    bot.register_next_step_handler(message,progress_guide)

@bot.message_handler(commands=['guide1'])
def guide1(message):
    text = "\U0001F447"
    text1 = "\U0001F537"
    chat_id = message.chat.id
    bot.send_message(message.chat.id, f"Напиши номер пункта, который хочешь изучить{text}  А для следующей темы, ты можешь использовать моё Меню)")
    for key, workout in spravki1.items():
        bot.send_message(chat_id,
                         f"{text1}{key}.{workout['name']}")
    bot.register_next_step_handler(message,progress_guide1)

def progress_guide(message):
    text = "\U0001F447"
    chat_id = message.chat.id
    selected_workout = message.text
    if selected_workout == "1":
        bot.send_document(chat_id=chat_id, document=open('Делители числа.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/govakugero')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "2":
        bot.send_document(chat_id=chat_id, document=open('Кратные числа.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/mubagahahu')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "3":
        bot.send_document(chat_id=chat_id, document=open('Признаки делимости на 10,5,2.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/zalohabuhu')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "4":
        bot.send_document(chat_id=chat_id, document=open('Признаки делимости на 9,3.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/fumavifeki')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "5":
        bot.send_document(chat_id=chat_id, document=open('Простые и составные числа.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/figigenoxo')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "6":
        bot.send_document(chat_id=chat_id, document=open('Разложение составных чисел на простые множители.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/pogabarexo')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "7":
        bot.send_document(chat_id=chat_id, document=open('Наибольший общий делитель НОД.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/hapofelisu')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "8":
        bot.send_document(chat_id=chat_id, document=open('Наименьшее общее кратное НОК.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/gixonofeni')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "9":
        bot.send_document(chat_id=chat_id, document=open('Основное свойство дроби.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/noferufodi')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "10":
        bot.send_document(chat_id=chat_id, document=open('Сокращение дробей.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/digilibuno')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "11":
        bot.send_document(chat_id=chat_id, document=open('Приведение обыкновнных дробей к наименьшему общему знаменателю НОЗ.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/dilibubume')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "12":
        bot.send_document(chat_id=chat_id,
                          document=open('Сравнение обыкновенных дробей.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/vudemorizu')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "13":
        bot.send_document(chat_id=chat_id,
                          document=open('Запись смешанного числа в виде неправильной дроби.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/gimefasuka')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "14":
        bot.send_document(chat_id=chat_id,
                          document=open('Запись натурального числа в виде неправильной дроби', 'rb'))
        # markup = types.InlineKeyboardMarkup()
        # button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
        #                                      url='https://edu.skysmart.ru/student/gimefasuka')
        # markup.add(button1)
        # bot.send_message(message.chat.id,
        #                  "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
        #                      message.from_user), reply_markup=markup)

    elif selected_workout == "15":
        bot.send_document(chat_id=chat_id,
                          document=open('Сложение и вычитание смешанных чисел.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/zadakibuge')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "16":
        bot.send_document(chat_id=chat_id,
                          document=open('Умножение обыкновенных дробей.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/duvalubima')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "17":
        bot.send_document(chat_id=chat_id,
                          document=open('Взаимно обратные числа.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/zavupumohi')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "18":
        bot.send_document(chat_id=chat_id,
                          document=open('Деление обыкновенных дробей.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/mupekapidu')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "19":
        bot.send_document(chat_id=chat_id,
                          document=open('Проценты (%).png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/finibigire')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "20":
        bot.send_document(chat_id=chat_id,
                          document=open('Задачи на нахождение части и целого.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/gikezopota')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    # elif selected_workout == "21":
    #     bot.send_document(chat_id=chat_id,
    #                       document=open('Угол.png', 'rb'))
    #     # markup = types.InlineKeyboardMarkup()
    #     # button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
    #     #                                      url='https://edu.skysmart.ru/student/gikezopota')
    #     # markup.add(button1)
    #     # bot.send_message(message.chat.id,
    #     #                  "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
    #     #                      message.from_user), reply_markup=markup)
    #
    # elif selected_workout == "22":
    #     bot.send_document(chat_id=chat_id,
    #                       document=open('Угловой градус, измерение углов.png', 'rb'))
    #     markup = types.InlineKeyboardMarkup()
    #     button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
    #                                          url='https://edu.skysmart.ru/student/tituhakuza')
    #     markup.add(button1)
    #     bot.send_message(message.chat.id,
    #                      "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
    #                          message.from_user), reply_markup=markup)
    #
    # elif selected_workout == "23":
    #     bot.send_document(chat_id=chat_id,
    #                       document=open('Окружность, круг.png', 'rb'))
    #     markup = types.InlineKeyboardMarkup()
    #     button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
    #                                          url='https://edu.skysmart.ru/student/fivorurana')
    #     markup.add(button1)
    #     bot.send_message(message.chat.id,
    #                      "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
    #                          message.from_user), reply_markup=markup)

    elif selected_workout == "21":
        bot.send_document(chat_id=chat_id,
                          document=open('Отрицательные и положительные числа.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/mifobebapu')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "22":
        bot.send_document(chat_id=chat_id,
                          document=open('Координаты на прямой.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/hisopoleka')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)


    elif selected_workout == "23":
        bot.send_document(chat_id=chat_id,
                          document=open('Сравнение чисел с помощью числовой оси.png', 'rb'))
        # markup = types.InlineKeyboardMarkup()
        # button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
        #                                      url='https://edu.skysmart.ru/student/hisopoleka')
        # markup.add(button1)
        # bot.send_message(message.chat.id,
        #                  "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
        #                      message.from_user), reply_markup=markup)

    elif selected_workout == "24":
        bot.send_document(chat_id=chat_id,
                          document=open('Противоположные числа.png', 'rb'))
        # markup = types.InlineKeyboardMarkup()
        # button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
        #                                      url='https://edu.skysmart.ru/student/hisopoleka')
        # markup.add(button1)
        # bot.send_message(message.chat.id,
        #                  "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
        #                      message.from_user), reply_markup=markup)

    elif selected_workout == "25":
        bot.send_document(chat_id=chat_id,
                          document=open('Модуль числа.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/tadakepoge')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "26":
        bot.send_document(chat_id=chat_id,
                          document=open('Рациональные числа.jpg', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/dakuheximu')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    # elif selected_workout == "30":
    #     bot.send_document(chat_id=chat_id,
    #                       document=open('Взаимное расположение двух прямых на плоскости.jpg', 'rb'))
    #     markup = types.InlineKeyboardMarkup()
    #     button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
    #                                          url='https://edu.skysmart.ru/student/beponosoxa')
    #     markup.add(button1)
    #     bot.send_message(message.chat.id,
    #                      "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
    #                          message.from_user), reply_markup=markup)


    elif selected_workout == "27":
        bot.send_document(chat_id=chat_id,
                          document=open('Коэффициент.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/susizohiza')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "28":
        bot.send_document(chat_id=chat_id,
                          document=open('Правило раскрытия скобок.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/pumedoxilu')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "29":
        bot.send_document(chat_id=chat_id,
                          document=open('Подобные слагаемые.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/givonolepa')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)



    elif selected_workout == "30":
        bot.send_document(chat_id=chat_id,
                          document=open('Решение линейных уравнений.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/punemehema')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "31":
        bot.send_document(chat_id=chat_id,
                          document=open('Координатная плоскость. Координата точки..jpg', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/foxesirode')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)





    else:
        bot.send_message(chat_id, "Пожалуйста, выберите вариант из списка.")

def progress_guide1(message):
    text = "\U0001F447"
    chat_id = message.chat.id
    selected_workout = message.text
    if selected_workout == "1":
        bot.send_document(chat_id=chat_id,
                          document=open('Угол.png', 'rb'))
        # markup = types.InlineKeyboardMarkup()
        # button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
        #                                      url='https://edu.skysmart.ru/student/gikezopota')
        # markup.add(button1)
        # bot.send_message(message.chat.id,
        #                  "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
        #                      message.from_user), reply_markup=markup)

    elif selected_workout == "2":
        bot.send_document(chat_id=chat_id,
                          document=open('Угловой градус, измерение углов.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/tituhakuza')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "3":
        bot.send_document(chat_id=chat_id,
                          document=open('Окружность, круг.png', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/fivorurana')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    elif selected_workout == "4":
        bot.send_document(chat_id=chat_id,
                          document=open('Взаимное расположение двух прямых на плоскости.jpg', 'rb'))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f"Проверить свои знания{text}",
                                             url='https://edu.skysmart.ru/student/beponosoxa')
        markup.add(button1)
        bot.send_message(message.chat.id,
                         "{0.first_name}, изучив теорию, ты можешь проверить свои знания".format(
                             message.from_user), reply_markup=markup)

    else:
        bot.send_message(chat_id, "Пожалуйста, выберите вариант из списка.")

@bot.message_handler(commands=['vpr'])
def vpr(message):
    text = "\U0001F447"
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(f"Подготовиться к ВПР{text}",
                                         url='https://edu.skysmart.ru/student/dozekeriho')
    markup.add(button1)
    bot.send_message(message.chat.id,
                     "{0.first_name}, изучив всю теорию, ты можешь подготовиться к ВПР!".format(
                         message.from_user), reply_markup=markup)


bot.polling()

if __name__ == "__main__":
    bot.polling(none_stop=True)