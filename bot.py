from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token('8487022975:AAFib8aJQtMXpCoj7l_K2dnW3uW7brcxA_w').build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
