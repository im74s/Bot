# This module imports each command module, collects its COMMAND_INFO and registers it.
from . import utils

USER_COMMANDS = []
ADMIN_COMMANDS = []

# List of command module names to import and register
_USER_MODULES = [
    "testadmin",
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
    "help",
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
    "promote",
    "demote",
    "pin",
    "unpin",
    "mute",
    "unmute",
    "warn",
    "unwarn",
    "setwelcome",
    "delwelcome",
    "broadcast",
    "lockdown",
    "unlock",
    "setrules",
    "delrules",
    "getadmins",
    "muteall",
    "unmuteall",
    "clean",
    "purge",
    "delmsg",
    "addmod",
    "removemod",
    "setlog",
    "getlog",
    "restart",
    "evalcmd",
    "groupstats",
]

def register(app):
    import importlib
    global USER_COMMANDS, ADMIN_COMMANDS
    USER_COMMANDS = []
    ADMIN_COMMANDS = []
    # import user modules
    for m in _USER_MODULES:
        mod = importlib.import_module(f"Commands.{m}")
        if hasattr(mod, "COMMAND_INFO"):
            USER_COMMANDS.append(mod.COMMAND_INFO)
        if hasattr(mod, "register"):
            mod.register(app)
    # import admin modules
    for m in _ADMIN_MODULES:
        mod = importlib.import_module(f"Commands.{m}")
        if hasattr(mod, "COMMAND_INFO"):
            ADMIN_COMMANDS.append(mod.COMMAND_INFO)
        if hasattr(mod, "register"):
            mod.register(app)
