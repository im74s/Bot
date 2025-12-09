import logging

logger = logging.getLogger(__name__)

async def is_group_admin(client, message):
    """
    Returns True if message is in a group/supergroup and sender is an admin or creator.
    """
    chat = message.chat
    
    # Check if this is a group or supergroup
    if chat.type not in ("group", "supergroup"):
        logger.debug(f"Not a group: chat_type={chat.type}")
        return False

    user = message.from_user
    
    # Handle cases where from_user is None (anonymous admin or channel)
    if not user:
        # Check if it's an anonymous admin
        if hasattr(message, 'sender_chat') and message.sender_chat:
            if message.sender_chat.id == chat.id:
                logger.info(f"Anonymous admin detected in chat {chat.id}")
                return True
        
        logger.debug(
            f"is_group_admin: message.from_user is None (anonymous admin or channel sender). "
            f"chat_id={chat.id} message_id={getattr(message, 'id', None)}"
        )
        return False

    # Try to get the member status
    try:
        member = await client.get_chat_member(chat.id, user.id)
        status = member.status
        is_admin = status in ("administrator", "creator")
        
        # Detailed logging for debugging
        logger.info(
            f"Admin check: "
            f"user_id={user.id}, "
            f"username={user.username or 'N/A'}, "
            f"first_name={user.first_name or 'N/A'}, "
            f"status={status}, "
            f"is_admin={is_admin}, "
            f"chat_id={chat.id}"
        )
        
        return is_admin
        
    except Exception as e:
        # Log the error with full details
        logger.error(
            f"is_group_admin: get_chat_member FAILED! "
            f"user_id={user.id}, "
            f"username={user.username or 'N/A'}, "
            f"chat_id={chat.id}, "
            f"chat_title={chat.title or 'N/A'}, "
            f"error={type(e).__name__}: {e}"
        )
        
        # Return False on error (the bot might not have proper permissions)
        return False
