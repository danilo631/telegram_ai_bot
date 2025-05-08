from telegram import Update
from telegram.ext import ContextTypes

BLOCKED_DOMAINS = ["youtube.com", "youtu.be", "tiktok.com"]

async def verificar_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    if any(domain in texto for domain in BLOCKED_DOMAINS) or "http" in texto and not texto.startswith("https"):
        await update.message.delete()
        await update.message.reply_text("🚫 Links de YouTube, TikTok ou suspeitos não são permitidos.")

async def verificar_nome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not user.username or not user.last_name:
        await update.message.reply_text(
            f"⚠️ @{user.username or 'usuário'}: você precisa definir nome de usuário e sobrenome para participar do grupo."
        )
