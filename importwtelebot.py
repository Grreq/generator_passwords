import telebot
from telebot import types
import string
import random

TOKEN = "7072858424:AAGpYv0QSBVOUHxHUepRh7Nnt-g7pIBPmZE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    full_name = message.from_user.full_name
    if message.from_user.full_name == "Родион":
        textstart = f"Hello my owner!👋\nClick the menu, or enter the button /help, To view the menu."
    else:
        textstart = f"Welcome, {full_name}!👋\nClick the menu or enter the button /help , To view the menu."
    bot.send_message(message.chat.id, text=textstart)


# сделать инлайн кнопки тут
@bot.message_handler(commands=["help"])
def menu(message):
    text_command = """Commands:\n
/start - Starts the bot's work.\n
/help - The bot outputs all commands that it can process.\n
/buttons - The bot outputs all buttons that it can process.n
"""
    bot.send_message(message.chat.id, text=text_command)


@bot.message_handler(commands=['buttons'])
def return_commands(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    text_menu = """Buttons:\n\nGenerate 🎲 - generate passwords for you,  in range 16 - 20 letters!
    \nCreate🪄 - creates a password personally for you, using the characters you need!
    \nCheck security🛡️ - performs a password security check!
    \nNew Email🆕 - is generate new random Email for you!
    """
    item_generate = types.KeyboardButton("Generate 🎲")
    item_check_security = types.KeyboardButton("Check security🛡️")
    item_create_personal = types.KeyboardButton("Create🪄")
    item_gen_name_mail = types.KeyboardButton("New Email🆕")
    item_back = types.KeyboardButton("Back↩️")
    markup.row(item_generate, item_create_personal, item_check_security)
    markup.row(item_gen_name_mail)
    bot.send_message(message.chat.id, text_menu, reply_markup=markup)

def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    full_name = message.from_user.full_name
    text = "Choose what you want to generate:"
    item_passwords = types.KeyboardButton("Passwords🔑")
    item_emails = types.KeyboardButton("Emails📬")

    markup.add(item_passwords, item_emails)
    bot.send_message(message.chat.id, text=text, reply_markup=markup)
    
def generate_password(message):
    punctuation = "+-_!*?"
    text_wait = f"Passwords for you:"

    characters = string.ascii_letters + string.digits + punctuation
    length = random.randint(10, 20)
    password = ''
    password2 = ''
    password3 = ''
    for i in range(length):
        password += ''.join(random.choice(characters))
        password2 += ''.join(random.choice(characters))
        password3 += ''.join(random.choice(characters))
    textpswrd1 = password
    textpswrd2 = password2
    textpswrd3 = password3

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_Generate = types.KeyboardButton("Generate 🎲")
    item_security = types.KeyboardButton("Check security🛡️")
    item_back = types.KeyboardButton("Back⬅️")
    markup.add(item_Generate, item_security, item_back)

    bot.send_message(message.chat.id, text=text_wait, reply_markup=markup)
    bot.send_message(message.chat.id, textpswrd1)
    bot.send_message(message.chat.id, textpswrd2)
    bot.send_message(message.chat.id, textpswrd3)

# Сделать генерацию ника почты
def name_to_mail(message):
    post = ""
    post2 = ""
    mail = ["@Gmail.ru", "@mail.ru", "@bk.ru", "@inbox.ru"]
    separator = random.choice("-_.")
    randomail = random.choice(mail)
    for i in range(5):
        email = string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters
        post += ''.join(random.choice(email))
        post2 += ''.join(random.choice(email))
    username = post + separator + post2 + randomail
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_username = types.KeyboardButton("New Email🆕")
    item_back = types.KeyboardButton("Back↩️")
    markup.add(item_username, item_back)
    bot.send_message(message.chat.id, username, reply_markup=markup)


def create_personal(message):
    text_for_personal_password = "How long password do you want?(letters)🔤"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_length_8 = types.KeyboardButton("8")
    item_length_12 = types.KeyboardButton("12")
    item_length_16 = types.KeyboardButton("16")
    item_length_20 = types.KeyboardButton("20")
    random_item = types.KeyboardButton("Randomly from 8 to 20")
    item_security = types.KeyboardButton("Check security🛡️")
    item_back = types.KeyboardButton("Back⬅️")
    markup.row(item_length_8, item_length_12, item_length_16, item_length_20)
    markup.row(random_item)
    markup.row(item_security, item_back)

    bot.send_message(message.chat.id, text=text_for_personal_password, reply_markup=markup)


# сделать команду проверки безопасный ли пароль
def security(message):
    text = "Send me any password and I'll check it!"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_Generate = types.KeyboardButton("Generate 🎲")
    item_security = types.KeyboardButton("Check security🛡️")
    item_back = types.KeyboardButton("Back⬅️")
    markup.add(item_Generate, item_security, item_back)
    bot.send_message(message.chat.id, text, reply_markup=markup)

def file(message):
    id = "1244894486"
    bot.send_message(message.chat.id, message.id)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Generate 🎲':
            generate_password(message)
        elif message.text == 'Passwords🔑':
            text = "Your choose | Passwords🔑 |:"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_generate = types.KeyboardButton("Generate 🎲")
            item_personal_password = types.KeyboardButton("Create🪄")
            item_security = types.KeyboardButton("Check security🛡️")
            item_back = types.KeyboardButton("Back↩️")
            markup.row(item_generate, item_personal_password, item_security)
            markup.add(item_back)
            bot.send_message(message.chat.id, text, reply_markup=markup)
        elif message.text == "Emails📬":
            text = "Your choose | Emails📬 |:"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_username = types.KeyboardButton("New Email🆕")
            item_back = types.KeyboardButton("Back↩️")
            markup.add(item_username, item_back)
            bot.send_message(message.chat.id, text, reply_markup=markup)
        elif message.text == 'Check security🛡️':
            security(message)
        elif message.text == "Create🪄":
            create_personal(message)
        elif message.text == "New Email🆕":
            name_to_mail(message)
        elif message.text == 'or':
            text = "You can't choose 'or'"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_passwords = types.KeyboardButton("Passwords🔑")
            item_emails = types.KeyboardButton("Emails📬")
            markup.add(item_passwords, item_emails)
            bot.send_message(message.chat.id, text, reply_markup=markup)
        elif message.text == "8":
            punctuation = "+-_!*?"
            characters = string.ascii_letters + string.digits + punctuation
            length = 8
            count = 0
            password = ''
            for i in range(length):
                password += ''.join(random.choice(characters))
                count += 1
            text = f"The length of this password - {count} letters"
            bot.send_message(message.chat.id, password)
            bot.send_message(message.chat.id, text)
        elif message.text == "12":
            punctuation = "+-_!*?"
            characters = string.ascii_letters + string.digits + punctuation
            length = 12
            count = 0
            password = ''
            for i in range(length):
                password += ''.join(random.choice(characters))
                count += 1
            text = f"The length of this password - {count} letters"
            bot.send_message(message.chat.id, password)
            bot.send_message(message.chat.id, text)
        elif message.text == "16":
            punctuation = "+-_!*?"
            characters = string.ascii_letters + string.digits + punctuation
            length = 16
            count = 0
            password = ''
            for i in range(length):
                password += ''.join(random.choice(characters))
                count += 1
            text = f"The length of this password - {count} letters"
            bot.send_message(message.chat.id, password)
            bot.send_message(message.chat.id, text)
        elif message.text == "20":
            punctuation = "+-_!*?"
            characters = string.ascii_letters + string.digits + punctuation
            length = 20
            count = 0
            password = ''
            for i in range(length):
                password += ''.join(random.choice(characters))
                count += 1
            text = f"The length of this password - {count} letters"
            bot.send_message(message.chat.id, password)
            bot.send_message(message.chat.id, text)
        elif message.text == "Randomly from 8 to 20":
            punctuation = "+-_!*?"
            characters = string.ascii_letters + string.digits + punctuation
            length = random.randint(8, 20)
            count = 0
            password = ''
            for i in range(length):
                password += ''.join(random.choice(characters))
                count += 1
            text = f"The length of this random password - {count} letters"
            bot.send_message(message.chat.id, password)
            bot.send_message(message.chat.id, text)
        elif message.text == "Back↩️":
            back(message)
        elif message.text == "Back⬅️":
            text = "Return to | Passwords🔑 |:"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_generate = types.KeyboardButton("Generate 🎲")
            item_personal_password = types.KeyboardButton("Create🪄")
            item_security = types.KeyboardButton("Check security🛡️")
            item_back = types.KeyboardButton("Back↩️")
            markup.row(item_generate, item_personal_password, item_security)
            markup.add(item_back)
            bot.send_message(message.chat.id, text, reply_markup=markup)
        elif message.text == "админ9486":
            file(message)
        else:
            length = random.randint(10, 16)
            password_message = message.text
            for i in range(len(password_message)):
                upper_case = any([1 if i in string.ascii_uppercase else 0
                                  for i in password_message])
                lower_case = any([1 if i in string.ascii_lowercase else 0
                                  for i in password_message])
                special = any([1 if i in string.punctuation else 0
                               for i in password_message])
                digits = any([1 if i in string.digits else 0
                              for i in password_message])
            if len(password_message) >= 10:
                check_length = True
            else:
                check_length = False
                characters = [upper_case, lower_case, special, digits, check_length]
                score = 0

            for i in range(len(characters)):
                if characters[i]:
                    score += 1
            
            text = "Only Latin letters can be used in the password"
            text_deficiency = f"This password is {score}/5"
            if score == 5:
                bot.send_message(message.chat.id, text_deficiency)
            elif score < 5:
                text_deficiency += "\nMissing:"
                if upper_case == False:
                    text_deficiency += "\nUpper Case (ABCD)"
                if lower_case == False:
                    text_deficiency += "\nLower Case (abcd)"
                if special == False:
                    text_deficiency += "\nSpecial characters (+-_!?*)"
                if digits == False:
                    text_deficiency += "\nDigits (1234)"
                if check_length == False:
                    text_deficiency += "\nLength < 10"
                bot.send_message(message.chat.id, text_deficiency)
            
            elif score == 0:
                bot.send_message(message.chat.id, text)
                
if __name__ == "__main__":
    bot.polling(none_stop=True)
