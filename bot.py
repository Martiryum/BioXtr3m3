import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContexTypes, CommandHandler
async def start(update: Update, contex: ContexTypes.DEFAULT_TYPE):
await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
​​if name == 'main':
application = ApplicationBuilder().token('8487022975:AAH0MmFQEnjEastyxRWnKT-SxVBPyXJqda0').build()
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)
application.run_polling()
