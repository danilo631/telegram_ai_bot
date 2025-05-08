from telegram import Update
from telegram.ext import ContextTypes
from app.ai import gerar_resposta

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Olá! Sou um bot com IA integrada e funções de moderação.\n"
        "Adicione-me a um grupo como administrador para começar."
    )

async def responder_pergunta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pergunta = update.message.text
    resposta = gerar_resposta(pergunta)
    await update.message.reply_text(resposta)
