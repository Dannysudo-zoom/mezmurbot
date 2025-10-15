from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
from flask import Flask
from threading import Thread
import os

# ==========================
# Bot Configuration
# ==========================
BOT_TOKEN = "7620770717:AAFaayATFoyIyuv6VDfmN41kMj5qj-v67B4"
FORM_LINK = "https://forms.gle/UDTpWGA49exBcZyMA"

# ==========================
# Keep Alive Web Server
# ==========================
app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "✅ Mezmur Lyrics Bot is running!"

def run():
    app_web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

# ==========================
# Bot Functions
# ==========================
async def send_main_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("📝 Submit Lyrics/ግጥምታት ንምልኣኽ", url=FORM_LINK)],
        [InlineKeyboardButton("📞 Contact Team/ኣድራሻ ኣዳለውቲ", callback_data="contact")],
        [InlineKeyboardButton("ℹ️ Project Details/ሓበሬታ ብዛዕባ ፕሮጀክት", callback_data="details")],
        [InlineKeyboardButton("🎵 Features Preview/ዕላማ ናይ ፕሮጀክት", callback_data="features")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    message_text = (
        "👋 *እንቋዕ ብደሓን መጻእኩም!*\n\n"
        "🎵 *ማዕከን ዲጂታል ጝጥምታት መዝሙር*\n\n"
        "ንመራሕቲ ኣምልኾን ኣባላት መዘምራንን፣ ናይ ኤርትራን ኢትዮጵያን መዝሙራት ንምእካብ ዝተሰርዐ ዲጂታላዊ መድረኽ እዩ።\n\n"
        "✨ *1ይ መድረኽ - ምእካብ ግጥምታት:*\n"
        "_ቁልፍታት ብምጥዋቅ ንምስታፍ ወይ ንምፍላጥ ሓበሬታ ይክኣል_"
    )

    if update.callback_query:
        await update.callback_query.edit_message_text(
            message_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
    elif update.message:
        await update.message.reply_text(
            message_text, reply_markup=reply_markup, parse_mode='Markdown'
        )

async def start(update: Update, context: CallbackContext):
    await send_main_menu(update, context)

async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == "contact":
        contact_text = (
            "📞 *Contact Excellent Digital Solutions*\n\n"
            "💼 *Project Lead:* B and D\n"
            "📧 *Email:* excellent.solutions2025@gmail.com\n"
            "📱 *Telegram:* @redeeming2024\n"
            "📞 *Phone:* +251 993 803 992\n\n"
            "⏰ *Response Time:* Within 24 hours\n\n"
            "_We're happy to answer any questions about the Digital Mezmur Lyrics Hub!_\n"
            "_ብዛዕባ እዚ ፕሮጀክት ምእካብ፣ ዘለኩም ሕቶታት ንምምላስ ድልዋት ኢና!_"
        )
        keyboard = [
            [InlineKeyboardButton("📝 Submit Lyrics/ ግጥምታት መዝሙር ንምልኣኽ 📝", url=FORM_LINK)],
            [InlineKeyboardButton("🔙 Back to Main/ ንምምላስ! 🔙 ", callback_data="main")]
        ]
        await query.edit_message_text(contact_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == "details":
        details_text = (
            "🔍 *Project Details - ዲጂታል መዝሙር ግጥሚ ማዕከን*\n\n"
            "🌟 *Mission:*\n"
            "To create a well-organized digital app that helps song leaders and choir members easily access Eritrean and Ethiopian gospel lyrics.\n\n"
            "📊 *Current Phase:*\n"
            "• Collecting lyrics from volunteers\n"
            "• Organizing songs by category and style\n"
            "• Building the database foundation\n\n"
            "🎯 *Timeline:*\n"
            "• Launch in 2–4 months\n"
            "• Monthly updates\n"
            "• Continuous lyrics additions\n\n"
            "_Submit lyrics to help build this resource!_\n"
            "_ግጥምታት መዝሙር ብምልኣኽ፣ ነዚ ዕዮ የፋጥኑ!_"
        )
        keyboard = [
            [InlineKeyboardButton("📝 Submit Lyrics", url=FORM_LINK)],
            [InlineKeyboardButton("🔙 Back to Main", callback_data="main")]
        ]
        await query.edit_message_text(details_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == "features":
        features_text = (
            "🎵 *Platform Features Preview/ ናይ ስራሕ ቅድመ እይታ*\n\n"
            "🔍 *For Gospel Leaders:*\n"
            "• Find songs by category (Worship, Repentance, etc.)\n"
            "• Search by title and style (Walz, Reggae, etc.)\n"
            "• Filter by scale and musical style\n\n"
            "🎤 *For Singers & Choir Members:*\n"
            "• Discover songs with similar scale/style\n"
            "• Understand lyrics meaning and themes\n"
            "• Organized by worship focus\n\n"
            "📚 *Song Organization:*\n"
            "• Sorted by category and style\n"
            "• Scale and key classification\n\n"
            "_Contribute to our growing database!_\n"
            "_ኣብ ምህናጽ ዝዓቢ ቋታ ናይ መዝሙር፣ ኣበርክቶኻ ኣዕዝዝ!_"
        )
        keyboard = [
            [InlineKeyboardButton("📝 Submit Lyrics", url=FORM_LINK)],
            [InlineKeyboardButton("🔙 Back to Main", callback_data="main")]
        ]
        await query.edit_message_text(features_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == "main":
        await send_main_menu(update, context)

# ==========================
# Main Bot Entry Point
# ==========================
def main():
    keep_alive()  # Start Flask web server
    bot_app = Application.builder().token(BOT_TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ Mezmur Lyrics Bot is running. Waiting for commands...")
    bot_app.run_polling()

if __name__ == '__main__':
    main()
