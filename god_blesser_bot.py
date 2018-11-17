import telebot
import time
import random

bot=telebot.TeleBot('689256335:AAFGWyEV9zSO38YUtz2zGX5uwZwq_m19v3I')

@bot.message_handler(commands=['god_bless_us'])
def send_bless(message):
    slova= ['Нехай жорстість дня буде для вас мінімальною',
    'Щоб увесь день у вас були лише приємні речі',
    'Трішечки непроємності трапляються',
    'Вчитись у вашій шаразі важко, але в принципі, терпимо',
    'Нехай сьогодні у вашу голову приходять лише переконливі твердження',
    'Благословляю вас на імунітет для омани, навіть невеликої',
    'Сьогодні ви маєте повне право сподіватись що нам пощастить',
    'Нехай сьогдні теореми доводитимуться самі',
    'Щасти вам сьогодні, але врахуйте: може статись так що і не пощастить',
    'Не робіть складних речей, ну може і не складних, але робити їх не треба',
    ]
    result=0
    with open('Data.txt', 'r') as file:
        for line in file:
            if str(message.chat.id) in line:
                mix=eval(line)
                result+=1
                if int(time.asctime().split(" ")[2])-mix[0]!=0:
                    with open('Data.txt', 'r+') as fio:

                        bot.send_message(message.chat.id, slova[random.randint(0,len(slova)-1)] )
                        data = fio.read()
                        text=str(data.replace(line,str("[" + str(time.asctime().split(" ")[2]) + "," + str(message.chat.id) + "]\n")))
                        with open('Data.txt', 'w') as fil:
                            fil.write(text)
                        try:
                            bot.pin_chat_message(message.chat.id, message.message_id+1)
                        except:
                            pass
                        return

                else:
                    bot.send_message(message.chat.id, 'Схоже , що сьогодні ти вже отримав благословення')
                    return
            else:
                continue
    if result==0:
        with open('Data.txt', 'r+') as fio:
            bot.send_message(message.chat.id, 'Blessing you')
            data = fio.read()
            fio.seek(0)
            fio.write("[" + str(time.asctime().split(" ")[2]) + "," + str(message.chat.id) + "]\n" + data)
            try:
                bot.pin_chat_message(message.chat.id, message.message_id + 1)
            except:
                pass
        return


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id,'Доброго дня смертні!\nДоступні команди:\n/god_bless_us - Благословлєніє от Бога нашого Бонда.\n/help - ну і для чого ця команда треба? ')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,'Команди доступні в данний момент часу:\n/god_bless_us - Благословлєніє от Бога нашого Бонда.\n/start- Почати віселіє.')

@bot.message_handler(func= lambda message : message.text == 'Захар миш' , content_types=['text'])
def say_true (message) :
    bot.send_message(message.chat.id , "Це правда кста")

bot.polling(none_stop=True)