from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
from app.handlers import start, responder_pergunta
from app.moderation import verificar_links, verificar_nome
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "7658263327:AAHFYobdunYAPXjoYDHD9vAg3ayZgdBQm7Q")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, verificar_links))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, verificar_nome))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_pergunta))

if __name__ == "__main__":
    print("🤖 Bot rodando...")
    app.run_polling()
