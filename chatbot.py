from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import sqlite3

# ---------- DATABASE ----------
conn = sqlite3.connect("chat_memory.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER,
    message TEXT,
    reply TEXT
)
""")
conn.commit()

# ---------- STORE REPLIES ----------
async def record_replies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if not msg or not msg.reply_to_message:
        return

    # Ignore bot messages
    if msg.from_user.is_bot or msg.reply_to_message.from_user.is_bot:
        return

    original = msg.reply_to_message.text
    reply = msg.text

    if not original or not reply:
        return

    cur.execute(
        "INSERT INTO memory (chat_id, message, reply) VALUES (?, ?, ?)",
        (msg.chat_id, original.lower(), reply)
    )
    conn.commit()

# ---------- BOT REPLY ----------
async def smart_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg:
        return

    # Only respond when mentioned
    if not context.bot.username.lower() in msg.text.lower():
        return

    query = msg.text.lower().replace(f"@{context.bot.username.lower()}", "").strip()

    cur.execute(
        "SELECT reply FROM memory WHERE message LIKE ? ORDER BY RANDOM() LIMIT 1",
        (f"%{query}%",)
    )
    row = cur.fetchone()

    if row:
        await msg.reply_text(row[0])
    else:
        await msg.reply_text("Hmm… I’ve seen this before but can’t recall properly.")

# ---------- RUN ----------
app = ApplicationBuilder().token("8447652823:AAEJFNUs8ABv-FOc40kEP3JwnKMHyAS5yt0").build()

app.add_handler(MessageHandler(filters.TEXT & filters.REPLY, record_replies))
app.add_handler(MessageHandler(filters.TEXT & filters.Entity("mention"), smart_reply))

app.run_polling()
