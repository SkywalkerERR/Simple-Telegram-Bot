import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()  

ADMIN_ID = os.getenv("ADMIN_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user    

    await update.message.reply_text(f'{os.getenv("TEXT")}')
 
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"🔔 Новый пользователь\n"
             f"Имя: {user.first_name}\n"
             f"ID: {user.id}\n"
             f"Username: @{user.username or 'нет'}"
    )

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler("start", start))
    
    application.run_polling()

if __name__ == '__main__':
    main()