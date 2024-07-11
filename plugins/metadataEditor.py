from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Example in-memory storage for metadata (you may replace with a database in production)
metadata_storage = {}

# Command to merge channels with metadata
def merge_channels(update: Update, context: CallbackContext) -> None:
    # Assuming the command format is "/merge @channel1 @channel2 #tag1,tag2 Description text"
    # Parse command arguments
    args = context.args
    if len(args) < 3:
        update.message.reply_text("Invalid command format. Use /merge @channel1 @channel2 #tags Description")
        return
    
    # Extract channels, tags, and description
    channel1 = args[0]
    channel2 = args[1]
    tags = args[2].split(',')
    description = ' '.join(args[3:])  # Description is everything after tags
    
    # Simulate storing metadata
    metadata_storage[channel1] = {
        'tags': tags,
        'description': description
    }
    
    metadata_storage[channel2] = {
        'tags': tags,
        'description': description
    }
    
    update.message.reply_text(f"Channels {channel1} and {channel2} merged successfully with metadata:\nTags: {tags}\nDescription: {description}")

# Command to get metadata of a channel
def get_metadata(update: Update, context: CallbackContext) -> None:
    channel_name = context.args[0] if context.args else None
    
    if not channel_name or channel_name not in metadata_storage:
        update.message.reply_text("Channel not found or metadata unavailable.")
        return
    
    metadata = metadata_storage[channel_name]
    tags = metadata['tags']
    description = metadata['description']
    
    update.message.reply_text(f"Metadata for {channel_name}:\nTags: {tags}\nDescription: {description}")

def main() -> None:
    # Set up the Telegram bot
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dispatcher = updater.dispatcher
    
    # Register command handlers
    dispatcher.add_handler(CommandHandler("merge", merge_channels))
    dispatcher.add_handler(CommandHandler("getmetadata", get_metadata))
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
