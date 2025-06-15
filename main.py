import json
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# تحميل الردود من ملف JSON
with open("config.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً يا نجم! أنا بوت الهزار 🤣")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    for keyword, reply in responses.items():
        if keyword in msg:
            await update.message.reply_text(reply)
            return

def main():
    import os
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("BOT_TOKEN not found in environment variables.")
        return
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()