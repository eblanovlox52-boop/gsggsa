from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

TOKEN = "8685550779:AAHiAFCBI95Fm76Pu1AHxAqDls0Lczel4p8"
ADMIN_ID = 8519899945

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("⭐ КУПИТЬ ЗВЁЗДЫ ⭐", callback_data="buy_stars")],
        [InlineKeyboardButton("💰 ПРОДАТЬ ЗВЁЗДЫ 💰", callback_data="sell_stars")],
        [InlineKeyboardButton("🏠 АРЕНДА NFT 🏠", callback_data="rent_nft")],
        [InlineKeyboardButton("🖼 КУПИТЬ NFT 🖼", callback_data="buy_nft")],
        [InlineKeyboardButton("🎁 КУПИТЬ ПОДАРОК 🎁", callback_data="buy_gift")],
        [InlineKeyboardButton("💎 КУПИТЬ TON 💎", callback_data="buy_ton")],
        [InlineKeyboardButton("👑 TELEGRAM PREMIUM 👑", callback_data="premium")],
        [InlineKeyboardButton("💳 ПОПОЛНИТЬ БАЛАНС 💳", callback_data="deposit")],
        [InlineKeyboardButton("👤 МОЙ ПРОФИЛЬ 👤", callback_data="profile")],
        [InlineKeyboardButton("📞 ПОДДЕРЖКА 📞", callback_data="support")],
        [InlineKeyboardButton("🧮 КАЛЬКУЛЯТОР 🧮", callback_data="calculator")],
        [InlineKeyboardButton("ℹ️ ИНФОРМАЦИЯ ℹ️", callback_data="info")],
        [InlineKeyboardButton("⭐ ОТЗЫВЫ ⭐", callback_data="reviews")],
        [InlineKeyboardButton("🏆 ТОП КЛИЕНТОВ 🏆", callback_data="top")],
        [InlineKeyboardButton("🤝 ПАРТНЁРСКАЯ ПРОГРАММА 🤝", callback_data="partner")],
        [InlineKeyboardButton("🎓 ОБУЧЕНИЕ ОСИНТ 🎓", callback_data="osint")],
        [InlineKeyboardButton("🔒 ДЭФ НАВСЕГДА 🔒", callback_data="def")],
        [InlineKeyboardButton("❤️ J ❤️", callback_data="fun")]
    ]
    
    await update.message.reply_text(
        "╔══════════════════════════════╗\n"
        "║   ✨ GRAVINDES STORE ✨      ║\n"
        "╚══════════════════════════════╝\n\n"
        "🔥 САМЫЕ НИЗКИЕ ЦЕНЫ!\n\n"
        "👤 Владелец: @Gravindes\n"
        "⭐ 1000+ довольных клиентов\n\n"
        "👇 ВЫБЕРИ ДЕЙСТВИЕ 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    
    if query.data == "back":
        await start(update, context)
    
    elif query.data == "buy_stars":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║       ⭐ ЗВЁЗДЫ ⭐               ║\n"
            "╚══════════════════════════════════╝\n\n"
            "📦 100⭐  ─  💰 110₽\n"
            "📦 150⭐  ─  💰 160₽\n"
            "📦 200⭐  ─  💰 250₽\n"
            "📦 250⭐  ─  💰 270₽\n"
            "📦 300⭐  ─  💰 350₽\n\n"
            "💳 ОПЛАТА НА КАРТУ:\n"
            "🏦 Т-Банк\n"
            "💳 2200 7021 4230 2590\n\n"
            "✅ ПОСЛЕ ОПЛАТЫ ПРИШЛИ ЧЕК @Gravindes\n"
            "📞 ДЛЯ ЗАКАЗА: @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "sell_stars":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║      💰 ПРОДАЖА ЗВЁЗД 💰         ║\n"
            "╚══════════════════════════════════╝\n\n"
            "💰 ЦЕНА ПОКУПКИ: 0.8₽ за 1⭐\n"
            "📉 МИНИМУМ: 100⭐\n\n"
            "📞 ПО ВОПРОСАМ ПРОДАЖИ: @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "rent_nft":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║      🏠 АРЕНДА NFT 🏠           ║\n"
            "╚══════════════════════════════════╝\n\n"
            "📦 7 ДНЕЙ   ─  💰 100⭐\n"
            "📦 30 ДНЕЙ  ─  💰 300⭐\n"
            "📦 90 ДНЕЙ  ─  💰 700⭐\n\n"
            "💳 ОПЛАТА НА КАРТУ:\n"
            "🏦 Т-Банк\n"
"💳 2200 7021 4230 2590\n\n"
            "✅ ПОСЛЕ ОПЛАТЫ ПРИШЛИ ЧЕК @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "buy_nft":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║       🖼 КУПИТЬ NFT 🖼           ║\n"
            "╚══════════════════════════════════╝\n\n"
            "📦 ОБЫЧНЫЙ NFT     ─  💰 400₽\n"
            "📦 ОБЫЧНЫЙ NFT+    ─  💰 700₽\n"
            "📦 ОБЫЧНЫЙ NFT++   ─  💰 1000₽\n"
            "📦 РЕДКИЙ NFT      ─  💰 1500₽\n"
            "📦 ЛЕГЕНДАРНЫЙ NFT ─  💰 2000₽\n\n"
            "💳 ОПЛАТА НА КАРТУ:\n"
            "🏦 Т-Банк\n"
            "💳 2200 7021 4230 2590\n\n"
            "✅ ПОСЛЕ ОПЛАТЫ ПРИШЛИ ЧЕК @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "buy_gift":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║      🎁 КУПИТЬ ПОДАРОК 🎁        ║\n"
            "╚══════════════════════════════════╝\n\n"
            "📦 ОБЫЧНЫЙ      ─  💰 400₽\n"
            "📦 УЛУЧШЕННЫЙ   ─  💰 700₽\n"
            "📦 ПРЕМИУМ      ─  💰 1000₽\n"
            "📦 РЕДКИЙ       ─  💰 1500₽\n"
            "📦 ЛЕГЕНДАРНЫЙ  ─  💰 2000₽\n\n"
            "💳 ОПЛАТА НА КАРТУ:\n"
            "🏦 Т-Банк\n"
            "💳 2200 7021 4230 2590\n\n"
            "✅ ПОСЛЕ ОПЛАТЫ ПРИШЛИ ЧЕК @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "buy_ton":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║       💎 КУПИТЬ TON 💎           ║\n"
            "╚══════════════════════════════════╝\n\n"
            "📦 1 TON   ─  💰 300₽\n"
            "📦 5 TON   ─  💰 1450₽\n"
            "📦 10 TON  ─  💰 2800₽\n\n"
            "💳 ОПЛАТА НА КАРТУ:\n"
            "🏦 Т-Банк\n"
            "💳 2200 7021 4230 2590\n\n"
            "✅ ПОСЛЕ ОПЛАТЫ ПРИШЛИ ЧЕК @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "premium":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║    👑 TELEGRAM PREMIUM 👑        ║\n"
            "╚══════════════════════════════════╝\n\n"
            "📦 1 МЕСЯЦ     ─  💰 250₽\n"
            "📦 3 МЕСЯЦА    ─  💰 700₽\n"
            "📦 6 МЕСЯЦЕВ   ─  💰 1300₽\n"
            "📦 12 МЕСЯЦЕВ  ─  💰 2500₽\n\n"
            "💳 ОПЛАТА НА КАРТУ:\n"
            "🏦 Т-Банк\n"
            "💳 2200 7021 4230 2590\n\n"
            "✅ ПОСЛЕ ОПЛАТЫ ПРИШЛИ ЧЕК @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "deposit":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║    💳 ПОПОЛНИТЬ БАЛАНС 💳        ║\n"
            "╚══════════════════════════════════╝\n\n"
            "💰 МИНИМУМ: 100₽\n\n"
            "💳 ОПЛАТА НА КАРТУ:\n"
            "🏦 Т-Банк\n"
            "💳 2200 7021 4230 2590\n\n"
            "✅ ПОСЛЕ ОПЛАТЫ ПРИШЛИ ЧЕК @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "profile":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            f"╔══════════════════════════════════╗\n"
            f"║       👤 МОЙ ПРОФИЛЬ 👤          ║\n"
            f"╚══════════════════════════════════╝\n\n"
            f"🆔 ID: {user.id}\n"
            f"📝 ИМЯ: {user.first_name}\n"
            f"📝 USERNAME: @{user.username if user.
username else 'нет'}\n"
            f"💰 БАЛАНС: 0₽",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "support":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║      📞 ПОДДЕРЖКА 📞             ║\n"
            "╚══════════════════════════════════╝\n\n"
            "👤 @Gravindes\n"
            "⏰ 24/7\n\n"
            "🔒 ГАРАНТИЯ ВОЗВРАТА СРЕДСТВ",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "calculator":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║      🧮 КАЛЬКУЛЯТОР 🧮           ║\n"
            "╚══════════════════════════════════╝\n\n"
            "100₽   →   90⭐\n"
            "200₽   →   180⭐\n"
            "500₽   →   450⭐\n"
            "1000₽  →   900⭐\n\n"
            "📞 ТОЧНЫЙ РАСЧЁТ: @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "info":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║     ℹ️ ИНФОРМАЦИЯ ℹ️            ║\n"
            "╚══════════════════════════════════╝\n\n"
            "✨ GRAVINDES STORE\n"
            "🔥 РАБОТАЕМ С 2024 ГОДА\n"
            "⭐ 1000+ КЛИЕНТОВ\n\n"
            "👤 @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "reviews":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║       ⭐ ОТЗЫВЫ ⭐              ║\n"
            "╚══════════════════════════════════╝\n\n"
            "«Отличный магазин!» — @client1\n\n"
            "«Лучшие цены!» — @client2\n\n"
            "📝 ОСТАВИТЬ ОТЗЫВ: @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "top":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║    🏆 ТОП КЛИЕНТОВ 🏆           ║\n"
            "╚══════════════════════════════════╝\n\n"
            "1. @client1 — 50000₽\n"
            "2. @client2 — 35000₽\n"
            "3. @client3 — 20000₽\n\n"
            "🔥 СТАНЬ ЛУЧШИМ!",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "partner":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║   🤝 ПАРТНЁРСКАЯ ПРОГРАММА 🤝    ║\n"
            "╚══════════════════════════════════╝\n\n"
            "💰 10% С ЗАКАЗА ДРУГА\n"
            "💳 ВЫПЛАТЫ КАЖДЫЙ ДЕНЬ\n\n"
            "📞 @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "osint":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║      🎓 ОБУЧЕНИЕ ОСИНТ 🎓        ║\n"
            "╚══════════════════════════════════╝\n\n"
            "💰 ЦЕНА: 1500₽\n\n"
            "💳 ОПЛАТА НА КАРТУ:\n"
            "🏦 Т-Банк\n"
            "💳 2200 7021 4230 2590\n\n"
            "✅ ПОСЛЕ ОПЛАТЫ ПРИШЛИ ЧЕК @Gravindes\n"
            "📞 ПО ВОПРОСАМ: @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "def":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║       🔒 ДЭФ НАВСЕГДА 🔒         ║\n"
"╚══════════════════════════════════╝\n\n"
            "💰 ЦЕНА: 1000₽\n\n"
            "💳 ОПЛАТА НА КАРТУ:\n"
            "🏦 Т-Банк\n"
            "💳 2200 7021 4230 2590\n\n"
            "✅ ПОСЛЕ ОПЛАТЫ ПРИШЛИ ЧЕК @Gravindes\n"
            "📞 ПО ВОПРОСАМ: @Gravindes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "fun":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text(
            "╔══════════════════════════════════╗\n"
            "║           ❤️ J ❤️               ║\n"
            "╚══════════════════════════════════╝\n\n"
            "@Gravindes ЖЕЛАЕТ ТЕБЕ\n"
            "ОТЛИЧНОГО ДНЯ! 🚀",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("✅ GRAVINDES STORE ЗАПУЩЕН!")
app.run_polling()
