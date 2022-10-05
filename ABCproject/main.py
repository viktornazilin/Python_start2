from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import Updater,ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, ContextTypes



async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def noword(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

#КОМАНДА ДЛЯ ДЗ
async def delword(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    txt = update.message.text
    print(f"Исходный текст: {txt}")
    find_txt = "абв"
    lst = [i for i in txt.split() if find_txt not in i]
    await update.message.reply_text(f'Результат: {" ".join(lst)}')

app = ApplicationBuilder().token("5352600050:AAF_Z8lJNkllOvvieD7-CWdtsEAJe1v9Peo").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("noword", noword))
app.add_handler(CommandHandler("delword", delword))
app.run_polling()