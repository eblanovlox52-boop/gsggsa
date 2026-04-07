from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

TOKEN = "8685550779:AAHiAFCBI95Fm76Pu1AHxAqDls0Lczel4p8"
ADMIN_ID = 8519899945

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("⭐ Купить звёзды", callback_data="buy_stars")],
        [InlineKeyboardButton("🏠 Аренда NFT", callback_data="rent_nft")],
        [InlineKeyboardButton("🖼 Купить NFT", callback_data="buy_nft")],
        [InlineKeyboardButton("👑 Премиум", callback_data="premium")],
        [InlineKeyboardButton("📞 Поддержка", callback_data="support")],
        [InlineKeyboardButton("J❤️", callback_data="fun")]
    ]
    await update.message.reply_text(
        "✨ GRAVINDES STORE ✨\n\n🔥 Telegram Stars, NFT, Premium\n\n👇 Выберите действие:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    
    if query.data == "buy_stars":
        await query.edit_message_text("⭐ 50⭐ - 50₽\n100⭐ - 90₽\n\n📞 @Gravindes", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    elif query.data == "rent_nft":
        await query.edit_message_text("🏠 Аренда NFT:\n7 дней - 100⭐\n30 дней - 300⭐\n\n📞 @Gravindes", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    elif query.data == "buy_nft":
        await query.edit_message_text("🖼 NFT:\nОбычный - 150⭐\nРедкий - 400⭐\n\n📞 @Gravindes", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    elif query.data == "premium":
        await query.edit_message_text("👑 Premium:\n1 мес - 150₽\n3 мес - 400₽\n\n📞 @Gravindes", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    elif query.data == "support":
        await query.edit_message_text("📞 Поддержка: @Gravindes", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    elif query.data == "fun":
        await query.edit_message_text("J❤️\n\n@Gravindes желает хорошего дня! 🚀", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    elif query.data == "back":
        await start(update, context)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()
