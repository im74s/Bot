```python name=bot/handlers/admin.py
"""
bot/handlers/admin.py

Admin command handlers for a Pyrogram-based Telegram bot (Bot API mode).

Commands implemented:
 - /kick      : remove member from group (kick)
 - /ban       : ban member
 - /unban     : unban member
 - /mute      : restrict member so they cannot send messages
 - /unmute    : restore sending permissions
 - /promote   : promote member to admin (optional title)
 - /demote    : remove admin rights

Notes:
 - All handlers are async and use Pyrogram filters.
 - Target user is resolved from a reply or from a username/ID argument.
 - Executor must be an admin to run the commands.
 - The bot itself must have the required permissions; checks are done where sensible.
 - No external libraries or databases are used.
"""

from typing import Optional, Tuple

from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatPermissions, ChatMember
from pyrogram.errors import RPCError, UserNotParticipant, PeerIdInvalid, BadRequest


async def get_target_user(client: Client, message: Message) -> Tuple[Optional[User], Optional[str]]:
    """
    Resolve the target user for an admin command.

    Priority:
      1. If the command message is a reply, return the replied-to user.
      2. Else, parse the first argument (username starting with @, numeric id, or plain username)
         and use client.get_users(...) to resolve it.

    Returns:
      (User, None) on success
      (None, error_message) on failure
    """
    # 1) From reply
    if message.reply_to_message and message.reply_to_message.from_user:
        return message.reply_to_message.from_user, None

    # 2) From command argument
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2 or not parts[1].strip():
        return None, "Please reply to a user's message or provide their username/ID."

    target_raw = parts[1].strip().split()[0]  # only first token
    # allow @username or plain username or id
    try:
        user = await client.get_users(target_raw)
        return user, None
    except (RPCError, ValueError) as e:
        return None, f"Could not find user '{target_raw}': {e}"


async def is_admin(client: Client, chat_id: int, user_id: int) -> bool:
    """
    Check whether the given user is an administrator (or creator) in the chat.
    Returns True if the user is 'administrator' or 'creator', False otherwise.
    """
    try:
        member: ChatMember = await client.get_chat_member(chat_id, user_id)
        return member.status in ("administrator", "creator")
    except RPCError:
        return False


# -------- Handlers --------

@Client.on_message(filters.command("kick") & filters.group)
async def cmd_kick(client: Client, message: Message):
    """
    /kick - remove member from group (kick)
    Usage: reply to user OR /kick @username_or_id
    """
    if not await is_admin(client, message.chat.id, message.from_user.id):
        await message.reply_text("You must be an admin to use /kick.")
        return

    bot_me = await client.get_me()
    if not await is_admin(client, message.chat.id, bot_me.id):
        await message.reply_text("I need to be an admin with ban/restrict permissions to kick users.")
        return

    target_user, err = await get_target_user(client, message)
    if err:
        await message.reply_text(err)
        return

    if target_user.id == bot_me.id:
        await message.reply_text("I cannot kick myself.")
        return

    try:
        # Ban then unban immediately to "kick" (remove member from group)
        await client.ban_chat_member(message.chat.id, target_user.id)
        await client.unban_chat_member(message.chat.id, target_user.id)
        await message.reply_text(f"User {target_user.mention} has been kicked.")
    except RPCError as e:
        await message.reply_text(f"Failed to kick {target_user.mention}: {e}")


@Client.on_message(filters.command("ban") & filters.group)
async def cmd_ban(client: Client, message: Message):
    """
    /ban - ban member from the chat
    Usage: reply to user OR /ban @username_or_id
    """
    if not await is_admin(client, message.chat.id, message.from_user.id):
        await message.reply_text("You must be an admin to use /ban.")
        return

    bot_me = await client.get_me()
    if not await is_admin(client, message.chat.id, bot_me.id):
        await message.reply_text("I need to be an admin with ban/restrict permissions to ban users.")
        return

    target_user, err = await get_target_user(client, message)
    if err:
        await message.reply_text(err)
        return

    if target_user.id == bot_me.id:
        await message.reply_text("I cannot ban myself.")
        return

    try:
        await client.ban_chat_member(message.chat.id, target_user.id)
        await message.reply_text(f"User {target_user.mention} has been banned.")
    except RPCError as e:
        await message.reply_text(f"Failed to ban {target_user.mention}: {e}")


@Client.on_message(filters.command("unban") & filters.group)
async def cmd_unban(client: Client, message: Message):
    """
    /unban - unban member
    Usage: reply to user OR /unban @username_or_id
    """
    if not await is_admin(client, message.chat.id, message.from_user.id):
        await message.reply_text("You must be an admin to use /unban.")
        return

    bot_me = await client.get_me()
    if not await is_admin(client, message.chat.id, bot_me.id):
        await message.reply_text("I need to be an admin with ban/restrict permissions to unban users.")
        return

    target_user, err = await get_target_user(client, message)
    if err:
        await message.reply_text(err)
        return

    try:
        await client.unban_chat_member(message.chat.id, target_user.id)
        await message.reply_text(f"User {target_user.mention} has been unbanned.")
    except RPCError as e:
        await message.reply_text(f"Failed to unban {target_user.mention}: {e}")


@Client.on_message(filters.command("mute") & filters.group)
async def cmd_mute(client: Client, message: Message):
    """
    /mute - restrict member so they cannot send messages
    Usage: reply to user OR /mute @username_or_id
    """
    if not await is_admin(client, message.chat.id, message.from_user.id):
        await message.reply_text("You must be an admin to use /mute.")
        return

    bot_me = await client.get_me()
    if not await is_admin(client, message.chat.id, bot_me.id):
        await message.reply_text("I need to be an admin with restrict permissions to mute users.")
        return

    target_user, err = await get_target_user(client, message)
    if err:
        await message.reply_text(err)
        return

    if target_user.id == bot_me.id:
        await message.reply_text("I cannot mute myself.")
        return

    try:
        permissions = ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False
        )
        await client.restrict_chat_member(message.chat.id, target_user.id, permissions=permissions)
        await message.reply_text(f"User {target_user.mention} has been muted.")
    except RPCError as e:
        await message.reply_text(f"Failed to mute {target_user.mention}: {e}")


@Client.on_message(filters.command("unmute") & filters.group)
async def cmd_unmute(client: Client, message: Message):
    """
    /unmute - restore sending permissions
    Usage: reply to user OR /unmute @username_or_id
    """
    if not await is_admin(client, message.chat.id, message.from_user.id):
        await message.reply_text("You must be an admin to use /unmute.")
        return

    bot_me = await client.get_me()
    if not await is_admin(client, message.chat.id, bot_me.id):
        await message.reply_text("I need to be an admin with restrict permissions to unmute users.")
        return

    target_user, err = await get_target_user(client, message)
    if err:
        await message.reply_text(err)
        return

    try:
        permissions = ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_send_polls=True
        )
        await client.restrict_chat_member(message.chat.id, target_user.id, permissions=permissions)
        await message.reply_text(f"User {target_user.mention} has been unmuted.")
    except RPCError as e:
        await message.reply_text(f"Failed to unmute {target_user.mention}: {e}")


@Client.on_message(filters.command("promote") & filters.group)
async def cmd_promote(client: Client, message: Message):
    """
    /promote - promote user to admin with basic rights
    Usage: reply to user OR /promote @username_or_id [optional title]
    """
    if not await is_admin(client, message.chat.id, message.from_user.id):
        await message.reply_text("You must be an admin to use /promote.")
        return

    bot_me = await client.get_me()
    if not await is_admin(client, message.chat.id, bot_me.id):
        await message.reply_text("I need to be an admin with promote permissions to promote users.")
        return

    # Check bot has promote permission
    try:
        bot_member = await client.get_chat_member(message.chat.id, bot_me.id)
        # Some chats may not expose detailed rights; best-effort check:
        if getattr(bot_member, "can_promote_members", False) is False and bot_member.status != "creator":
            await message.reply_text("I don't have permission to promote members. Please grant me promote rights.")
            return
    except RPCError:
        await message.reply_text("Could not verify my permissions. Aborting.")
        return

    target_user, err = await get_target_user(client, message)
    if err:
        await message.reply_text(err)
        return

    # parse optional title
    parts = message.text.split(maxsplit=2)
    title = None
    if len(parts) >= 3:
        title = parts[2].strip()

    try:
        # Grant a set of reasonable basic admin rights
        await client.promote_chat_member(
            message.chat.id,
            target_user.id,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=False,
            can_manage_video_chats=False,
            can_manage_chat=False,
        )
    except RPCError as e:
        await message.reply_text(f"Failed to promote {target_user.mention}: {e}")
        return

    # Try to set custom title if provided
    if title:
        try:
            # Some Pyrogram versions expose this helper under different names.
            # Try common method names but ignore failures and inform the user.
            try:
                # pyrogram >=1.0 style
                await client.set_administrator_custom_title(message.chat.id, target_user.id, title)
            except AttributeError:
                try:
                    # alternative naming
                    await client.set_chat_administrator_custom_title(message.chat.id, target_user.id, title)
                except AttributeError:
                    # fallback to raw API call
                    await client.call("setChatAdministratorCustomTitle", {
                        "chat_id": message.chat.id,
                        "user_id": target_user.id,
                        "custom_title": title
                    })
        except RPCError as e:
            await message.reply_text(f"Promoted {target_user.mention}, but failed to set title: {e}")
            return
        except Exception:
            # best-effort: if setting title failed due to missing method, still inform success
            await message.reply_text(f"Promoted {target_user.mention}. Could not set custom title (not supported).")
            return

    await message.reply_text(f"User {target_user.mention} has been promoted{(f' with title \"{title}\"' if title else '')}.")


@Client.on_message(filters.command("demote") & filters.group)
async def cmd_demote(client: Client, message: Message):
    """
    /demote - remove admin rights from a user
    Usage: reply to user OR /demote @username_or_id
    """
    if not await is_admin(client, message.chat.id, message.from_user.id):
        await message.reply_text("You must be an admin to use /demote.")
        return

    bot_me = await client.get_me()
    if not await is_admin(client, message.chat.id, bot_me.id):
        await message.reply_text("I need to be an admin with promote permissions to demote users.")
        return

    # Check bot has promote permission
    try:
        bot_member = await client.get_chat_member(message.chat.id, bot_me.id)
        if getattr(bot_member, "can_promote_members", False) is False and bot_member.status != "creator":
            await message.reply_text("I don't have permission to change admins. Please grant me promote rights.")
            return
    except RPCError:
        await message.reply_text("Could not verify my permissions. Aborting.")
        return

    target_user, err = await get_target_user(client, message)
    if err:
        await message.reply_text(err)
        return

    try:
        # Remove admin rights by setting all promotion flags to False
        await client.promote_chat_member(
            message.chat.id,
            target_user.id,
            is_anonymous=False,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_video_chats=False,
            can_manage_chat=False,
        )
        await message.reply_text(f"User {target_user.mention} has been demoted.")
    except RPCError as e:
        await message.reply_text(f"Failed to demote {target_user.mention}: {e}")
```
