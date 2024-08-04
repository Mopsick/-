import telebot
from datetime import datetime, timedelta

# Замените 'ВАШ_ТОКЕН' на токен, полученный от BotFather
TOKEN = '7392633575:AAEtAMYFY_7sA73pPlZmWGDI51MqeLcoYuQ'
bot = telebot.TeleBot(TOKEN)


# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Добро пожаловать бот по тренеровкам!")


# @bot.message_handler(func=lambda message: True)


workouts = {}

journals = {}

available_workouts = {
    "1": {
        "name": "Кардиотренировка",
        "description": "Кардиотренировки укрепляют сердечно-сосудистую систему, способствуют сжиганию калорий и улучшению общего самочувствия.",
        "exercises": [
            "Бег на беговой дорожке или на улице (20-30 минут)",
            "Прыжки на скакалке (3 подхода по 5 минут с минутным отдыхом между подходами)",
            "Велосипед (30 минут на стационарном велосипеде или на свежем воздухе)",
            "Степпер или ходьба по ступенькам (15-20 минут)"
        ]
    },
    "2": {
        "name": "Силовая тренировка",
        "description": "Силовые тренировки направлены на укрепление мышц, увеличение мышечной массы и улучшение общей силы.",
        "exercises": [
            "Приседания со штангой (3 подхода по 8-12 повторений)",
            "Тяга гантелей в наклоне (3 подхода по 8-12 повторений)",
            "Жим лежа на скамье (3 подхода по 8-12 повторений)",
            "Подтягивания на турнике (3 подхода максимальное количество раз)"
        ]
    },
    "3": {
        "name": "Тренировка на гибкость",
        "description": "Тренировки на гибкость помогают улучшить подвижность суставов, увеличить амплитуду движений и предотвратить травмы.",
        "exercises": [
            "Растяжка 'бабочка' (удерживайте позицию 1-2 минуты)",
            "Наклоны к ногам, сидя на полу (удерживайте позицию 1-2 минуты)",
            "Лодочка (удерживайте позицию 30 секунд)",
            "Поза ребёнка (удерживайте 1-2 минуты)"
        ]
    },
    "4": {
        "name": "Функциональная тренировка",
        "description": "Функциональные тренировки улучшают работу всего тела, координацию движений и способствуют эффективному сжиганию калорий.",
        "exercises": [
            "Бёрпи (3 подхода по 10 повторений)",
            "Планка (удерживайте 30-60 секунд)",
            "Отжимания (3 подхода по 10-15 повторений)",
            "Приседания с прыжком (3 подхода по 10-15 повторений)"
        ]
    }
}



@bot.message_handler(commands=['add_workout'])
def add_workout(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Выберите тренировку из списка:")
    for key, workout in available_workouts.items():
        bot.send_message(chat_id, f"{key}. {workout['name']}")


def process_selected_workout(message):
    chat_id = message.chat.id
    selected_workout = message.text
    if selected_workout in available_workouts:
        workouts[chat_id] = available_workouts[selected_workout]
        bot.send_message(chat_id, f"Тренировка '{workouts[chat_id]['name']}' добавлена.")
        bot.send_message(chat_id, "Введите время тренировки в формате HH:MM (например, 18:00):")
        bot.register_next_step_handler(message, process_workout_time)
    else:
        bot.send_message(chat_id, "Пожалуйста, выберите тренировку из списка.")


def process_workout_time(message):
    chat_id = message.chat.id
    workout_time_str = message.text
    workout_time = datetime.strptime(workout_time_str, "%H:%M")
    workouts[chat_id]["time"] = workout_time

    bot.send_message(chat_id, f"Тренировка '{workouts[chat_id]['name']}' добавлена на {workout_time_str}.")


@bot.message_handler(commands=['delete_workout'])
def delete_workout(message):
    chat_id = message.chat.id
    if chat_id in workouts and workouts[chat_id]:
        bot.send_message(chat_id, "Выберите тренировку для удаления:")
        for i, workout in enumerate(workouts[chat_id]):
            bot.send_message(chat_id, f"{i + 1}. {workout['name']} в {workout['time'].strftime('%H:%M')}")

        bot.register_next_step_handler(message, process_selected_delete_workout)
    else:
        bot.send_message(chat_id, "У вас нет добавленных тренировок.")


def process_selected_delete_workout(message):
    chat_id = message.chat.id
    selected_number = int(message.text)
    if selected_number <= len(workouts[chat_id]) and selected_number > 0:
        deleted_workout_name = workouts[chat_id].pop(selected_number - 1)["name"]
        bot.send_message(chat_id, f"Тренировка '{deleted_workout_name}' удалена.")
    else:
        bot.send_message(chat_id, "Неверный номер тренировки.")

@bot.message_handler(commands=['write_journal'])
def write_journal(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Введите свои заметки о тренировке и данные о весе:")

    bot.register_next_step_handler(message, process_journal_entry)


def process_journal_entry(message):
    chat_id = message.chat.id
    journal_entry = message.text

    if chat_id not in journals:
        journals[chat_id] = []

    journals[chat_id].append(journal_entry)

    bot.send_message(chat_id, "Заметка добавлена в ваш дневник тренировок.")

@bot.message_handler(commands=['read_journal'])
def read_journal(message):
    chat_id = message.chat.id

    if chat_id in journals and journals[chat_id]:
        bot.send_message(chat_id, "Ваш дневник тренировок:")
        for entry in journals[chat_id]:
            bot.send_message(chat_id, entry)


bot.polling()

if __name__ == "__main__":
    bot.polling(none_stop=True)
