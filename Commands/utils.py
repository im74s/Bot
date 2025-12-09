import logging

logger = logging.getLogger(__name__)

async def is_group_admin(client, message):
    # Returns True if message is in a group/supergroup and sender is an admin or creator
    chat = message.chat
    if chat.type not in ("group", "supergroup"):
        return False

    user = message.from_user
    if not user:
        # This can happen when the sender is a channel or the admin posts anonymously.
        # We cannot resolve the real user id in that case so treat as non-admin.
        logger.debug("is_group_admin: message.from_user is None (anonymous admin or channel sender). chat_id=%s message_id=%s", chat.id, getattr(message, 'message_id', None))
        return False

    try:
        member = await client.get_chat_member(chat.id, user.id)
        status = getattr(member, "status", None)
        return status in ("administrator", "creator")
    except Exception as e:
        # Log the error so you can see why get_chat_member failed
        logger.exception("is_group_admin: get_chat_member failed for user %s in chat %s", user.id, chat.id)
        return False
