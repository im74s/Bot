import importlib
from pyrogram import filters
from .utils import admin_only

USER_COMMANDS = []
ADMIN_COMMANDS = []

_USER_MODULES = [
    "help",
    "start",
    "ping",
    "echo",
    "id",
    "whois",
    "timecmd",
    "roll",
    "flip",
    "choose",
    "joke",
    "quote",
    "meme",
    "avatar",
    "stats",
    "uptime",
    "calc",
    "math",
    "translate",
    "weather",
    "setreminder",
    "reminderlist",
    "cancelreminder",
    "note",
    "notes",
    "listnotes",
    "delnote",
    "dice",
    "cat",
    "dog",
    "shorten",
]

_ADMIN_MODULES = [
    "ban",
    "kick",
    "mute",
    "unmute",
    "promote",
    "demote",
    "unban",
    "pin",
    "unpin",
    "warn",
    "unwarn",
    "clean",
    "purge",
    "delmsg",
    "lockdown",
    "unlock",
    "muteall",
    "unmuteall",
]

def register(app):
    global USER_COMMANDS, ADMIN_COMMANDS
    USER_COMMANDS = []
    ADMIN_COMMANDS = []

    # Register user commands normally
    for name in _USER_MODULES:
        mod = importlib.import_module(f"Commands.{name}")
        if hasattr(mod, "COMMAND_INFO"):
            USER_COMMANDS.append(mod.COMMAND_INFO)
        if hasattr(mod, "register"):
            mod.register(app)

    # Register admin commands centrally
    for name in _ADMIN_MODULES:
        mod = importlib.import_module(f"Commands.{name}")

        if hasattr(mod, "COMMAND_INFO"):
            ADMIN_COMMANDS.append(mod.COMMAND_INFO)

        handler = getattr(mod, "handler", None)
        if not handler:
            continue

        command = mod.COMMAND_INFO["name"].lstrip("/")

        @app.on_message(filters.command(command) & filters.group)
        @admin_only
        async def admin_wrapper(client, message, _handler=handler):
            await _handler(client, message)
