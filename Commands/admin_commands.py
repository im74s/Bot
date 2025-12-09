from pyrogram.handlers import MessageHandler
from pyrogram import filters
from . import kick, ban, mute, unmute, promote, demote, unban

def register_admin_commands(app):
    # register each handler on the running client instance
    app.add_handler(MessageHandler(kick.kick, filters.command("kick") & filters.group))
    app.add_handler(MessageHandler(ban.ban, filters.command("ban") & filters.group))
    app.add_handler(MessageHandler(mute.mute, filters.command("mute") & filters.group))
    app.add_handler(MessageHandler(unmute.unmute, filters.command("unmute") & filters.group))
    app.add_handler(MessageHandler(promote.promote, filters.command("promote") & filters.group))
    app.add_handler(MessageHandler(demote.demote, filters.command("demote") & filters.group))
    app.add_handler(MessageHandler(unban.unban, filters.command("unban") & filters.group))
