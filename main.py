import telebot
import logging
import random
from background import keep_alive
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'ваш токен'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = telebot.TeleBot("6379079116:AAHSN2ciYVdekNf0zcv6_zKxLpL2SzQiB8M", parse_mode=None)

words = "бот соси сасать саси сосать".split()
dogs = "член члены хуй хуи".split()
plac = "отсоси саси соси отсаси".split()
space = "конча сперма кончу сперму".split()
skatilos = "Скатился скатился Скатилась скатилась Скатилось скатилось".split()

text_photo = 'кринж', 'норм', 'шедеврально', 'хератень'
text_random = 'ШКИБИДИ ДОП ДОП ДОП', 'Чем гуще лес, шкибиди доп ес ес', 'Го в доту', \
    'С 8 марта', 'Конспект', 'Абстракт', 'Сну    8 марта', 'С 8 марта', \
    'Фурион фурион по фарму чемпион\nБыстрее всех голду зарабатывает он', '', '', '', '', \
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', \
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''

g = '🟥🟥🟥🟥🟥🟥🟥🟥🟥\n'
i = '🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥\n'
t = '🟥⬜️⬛️⬜️⬛️⬛️⬛️⬜️🟥\n'
l = '🟥⬜️⬛️⬜️⬛️⬜️⬜️⬜️🟥\n'
e = '🟥⬜️⬛️⬛️⬛️⬛️⬛️⬜️🟥\n'
r = '🟥⬜️⬜️⬜️⬛️⬜️⬛️⬜️🟥\n'
x = '🟥⬜️⬛️⬛️⬛️⬜️⬛️⬜️🟥\n'
u = '🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥\n'
y = '🟥🟥🟥🟥🟥🟥🟥🟥🟥'

text_gitler = g + i + t + l + e + r + x + u + y

fact_random = 'Левон - жирное чмо', 'Игорь - пидорасина', 'Оганесян - педик'

quotes_random = \
    'Пабло не тот кто Пабло, а Пабло тот кто кактус..\n Владимир Владимирович 2021', \
        '3 медведя не банан..\n Нейросеть 2023', \
        'Если ты не ел волка, ты не яблоко..\n Нейросеть 2023', \
        'Трактор, самолёт, качели, вилка огурец, шкибиди доб ес ес.. \n Михаил 2023', \
        'Тимон не пумба, шкаф не пумба..\n Владимир Владимирович 2023', \
        'Инглиш перфект еври ван свинка пепа срет в диван..\n Владимир Владимирович 2023', \
        'Настоящий конспект, не тот где Елена Плаксина, а тот где 5 параграф..\n Михаил 2023', \
        'Лес, собака, стул, мопед, здравствуй, мама, я - валет..\n Владимир Владимирович 2023',\
        'Хотите стать такими же богатыми и успешными, как я? Инвестируйте!\n Михаил 2022'
holiday_random = 'С 8 марта!', 'С 23 февраля!', 'С 1 апреля!', 'С днем отца!', \
    'С днем матери!', 'С днем дауна!'

sticker_random = 'CAACAgIAAxkBAAECT1NlcC-jvhKe8P06Jgg95Pg_ATB6pQAC8xQAAu3wMUsHcIOXD50OJjME', \
    'CAACAgIAAxkBAAECT11lcDKxRfMstoWSkgaBK1vMzojGYQACQQ8AAuigMEshnEAaDp66hDME', \
    'CAACAgIAAxkBAAECT19lcDK1wJM_ELmw4BF2nt5-CBmhGQACrxEAAuPSMEtF72q7bOvDFzME', \
    'CAACAgIAAxkBAAECT2FlcDK2vC4-nTRTDPHK5IhIi8OwHgACDxoAAi2voUsF3JEtnISDxTME', \
    'CAACAgIAAxkBAAECT2NlcDK4zcMdk_rouyuCWHJgyPSIAQAClioAAnjEyEpT4JffH6VpZzME', \
    'CAACAgIAAxkBAAECT2VlcDK92qlKnv9wq3l3qJj7NVu51AACFxgAAkF2KEs7WveJLsi4RDME', \
    'CAACAgIAAxkBAAECT2dlcDK-ybkBjSGEG38I8HjQaErXjgACWhYAAiTJKEue6ZBO4JL3djME', \
    'CAACAgIAAxkBAAECT2tlcDLNaKoJO4Zs4b6GQ_w4IevWtwACdhAAAuQd6Uhy3X4hkD8FhzME', \
    'CAACAgIAAxkBAAECT3tlcDUlXk6SRUs1OU42hpfYxsmWhwACbxAAAjX24Us5Ka2ytSMRnDME', \
    'CAACAgIAAxkBAAECT4JlcDWltKvdnaVhzCg0mg2dmVZ0mAACcQ8AAl3h4UtjxyjnFwXPHjME', \
    'CAACAgIAAxkBAAECT4NlcDWlbtgZRpYDED3MmDgmTp8CHwACvhAAAlJS2EtQhYxsQLCr3TME', \
    'CAACAgIAAxkBAAECT4RlcDWlYWwtgXXzf2ehJoaKVIRUUQAChhEAAioR4UuBQmTKYc87PTME', \
    'CAACAgIAAxkBAAECT4VlcDWl46GC7RhxTGLEHdzcuXPw0AACmxEAAqM12Uv_xZITcLrGezME', \
    'CAACAgIAAxkBAAECT4dlcDWlyHzSLzsJ2OKoFx4Re64htAACZQwAAn9X8EqFTcbnsCMuIjME', \
    'CAACAgIAAxkBAAECT4ZlcDWlJngCiLh1m6wUkrpG640uewAC3RIAAlGIOElultL6nnxL1TME', \
    'CAACAgIAAxkBAAECT4dlcDWlyHzSLzsJ2OKoFx4Re64htAACZQwAAn9X8EqFTcbnsCMuIjME', \
    'CAACAgIAAxkBAAECT4hlcDWlYa8P4e0NSYvI6QVP4r7-4gACMQoAAsmu-EpY5HhyRkNidDME'

abstract = 'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n' \
           'Конспект 6 параграфа\n'

bot = telebot.TeleBot('6379079116:AAHSN2ciYVdekNf0zcv6_zKxLpL2SzQiB8M')


@bot.message_handler(content_types=['text'])
def say_text(message):
    #    bot.reply_to(message, "игорь пидарасина")хо

    if message.text == '/help@gitler1939_bot':
        bot.send_message(message.chat.id, 'Сам помогай себе, немощ')
        return

    if message.text == '/help':
        bot.send_message(message.chat.id, 'Сам помогай себе, немощ')
        return

    if message.text == 'Гимн':
        audio = open(r'media/Gimn.m4a', 'rb')
        bot.send_chat_action(message.chat.id, 'upload_audio')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        return

    if message.text == '/gimn':
        audio = open(r'media/Gimn.m4a', 'rb')
        bot.send_chat_action(message.chat.id, 'upload_audio')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        return

    if message.text == '/gimn@gitler1939_bot':
        audio = open(r'media/Gimn.m4a', 'rb')
        bot.send_chat_action(message.chat.id, 'upload_audio')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        return

    if message.text == '/igor@gitler1939_bot':
        with open("media/igor.jpg", "rb") as file:
            f = file.read()
        bot.send_photo(message.chat.id, f, "")
        return

    if message.text == '/igor':
        with open("media/igor.jpg", "rb") as file:
            f = file.read()
        bot.send_photo(message.chat.id, f, "")
        return

    if message.text == 'Игорь':
        with open("media/igor.jpg", "rb") as file:
            f = file.read()
        bot.send_photo(message.chat.id, f, "")
        return

    if message.text == 'Интересные факты':
        bot.send_message(message.chat.id, random.choice(fact_random))
        return

    text = message.text.lower()

    if message.text == 'Цитаты':
        bot.send_message(message.chat.id, random.choice(quotes_random))
        return

    if message.text == 'Свастика':
        bot.send_message(message.chat.id, text_gitler)
        return

    if message.text == 'С 8 марта':
        bot.send_message(message.chat.id, random.choice(holiday_random))
        return

    if message.text == 'Стикер':
        bot.send_sticker(message.chat.id, random.choice(sticker_random))
        return

    if message.text == '/sticker':
        bot.send_sticker(message.chat.id, random.choice(sticker_random))
        return

    if message.text == '/sticker@gitler1939_bot':
        bot.send_sticker(message.chat.id, random.choice(sticker_random))
        return

    if message.text == '/help@gitler1939_bot':
        bot.send_message(message.chat.id, 'Сам помогай себе, немощ')
        return

    if message.text == '/abstract@gitler1939_bot':
        bot.send_message(message.chat.id, abstract)
        return

    if message.text == '/abstract':
        bot.send_message(message.chat.id, abstract)
        return

    if message.text == 'Конспект':
        bot.send_message(message.chat.id, abstract)
        return

    if any(x in text for x in words):
        if any(x in text for x in dogs):
            bot.send_message(message.chat.id, "*  *")

        if any(x in text for x in plac):
            bot.send_message(message.chat.id, '*  *')

        if any(x in text for x in space):
            bot.send_message(message.chat.id, "*  *")

    else:
        bot.send_message(message.chat.id, random.choice(text_random))
        return

bot.infinity_polling()

keep_alive()
if __name__ == '__main__':
    executor.start_polling(bot, skip_updates=True)