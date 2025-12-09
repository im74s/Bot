import logging

logger = logging.getLogger(__name__)

async def is_group_admin(client, message):
    """
    Returns True if message is in a group/supergroup and sender is an admin or creator
    """
    chat = message.chat
    if chat.type not in ("group", "supergroup"):
        return False

    user = message.from_user
    if not user:
        # This can happen when the sender is a channel or the admin posts anonymously.
        if hasattr(message, 'sender_chat') and message.sender_chat and message.sender_chat.id == chat.id:
            # Anonymous admin
            return True
        logger.debug("is_group_admin: message.from_user is None (anonymous admin or channel sender). chat_id=%s message_id=%s", 
                     chat.id, getattr(message, 'id', None))
        return False

    try:
        member = await client.get_chat_member(chat.id, user.id)
        status = member.status
        is_admin = status in ("administrator", "creator")
        
        # Log for debugging
        logger.info(f"Admin check: user_id={user.id}, username={user.username}, status={status}, is_admin={is_admin}")
        
        return is_admin
    except Exception as e:
        # Log the actual error to help debug
        logger.error(f"is_group_admin: get_chat_member failed for user {user.id} ({user.username}) in chat {chat.id}: {e}")
        # In case of error, return False but this should be investigated
        return False
