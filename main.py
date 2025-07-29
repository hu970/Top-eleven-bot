import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bienvenue sur Top Eleven Coach Bot ! Tape /aide pour voir les commandes disponibles."
    )

async def aide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Pépites", callback_data='pepites'),
            InlineKeyboardButton("Tactiques", callback_data='tactiques'),
            InlineKeyboardButton("Contact", callback_data='contact'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
   
    await update.message.reply_text(
        "Choisis une option ci-dessous :",
        reply_markup=reply_markup
    )
   
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
   
    data = query.data
    if data == 'pepites':
        await pepites(update, context)
    elif data == 'tactiques':
        await tactiques(update, context)
    elif data == 'contact':
        await contact(update, context)

async def pepites(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.message.reply_text(
        "Voici quelques véritables jeunes pépites à acheter en priorité dans Top Eleven (générés par des stats de la communauté) :\n"
        "\n"
        "1. Manuel Duran (DC) - Espagnol - 18 ans - 79% de rendement\n"
        "2. Luis Romero (MC) - Argentin - 18 ans - Polyvalent\n"
        "3. Filip Stevanovic (AG) - Serbe - 18 ans - Très rapide\n"
        "4. Yassine Ba (AC) - Marocain - 18 ans - Bon ratio buts/match\n"
        "5. Ryu Tanaka (DD) - Japonais - 18 ans - Excellent récupérateur\n"
        "\n"
        "🧠 Astuce : privilégie les joueurs de 18 ans avec +80% de potentiel et un seul poste (gain de XP plus rapide)."
    )

async def tactiques(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.message.reply_text(
        "⚔️ Tactiques efficaces pour dominer Top Eleven :\n\n"
        "1️⃣ 4-3-3 Attaque (Pressing haut, passes courtes)\n"
        "   ➤ Idéal pour les équipes fortes et agressives\n\n"
        "2️⃣ 4-1-2-1-2 Losange (Contre rapide, passes longues)\n"
        "   ➤ Parfait contre les équipes à 3 milieux\n\n"
        "3️⃣ 3-5-2 (Large, pressing élevé)\n"
        "   ➤ Fonctionne bien contre les formations défensives\n\n"
        "⚠️ Astuce : n'oublie pas de t'adapter à l’adversaire et de changer de mentalité si tu perds à la mi-temps."
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.message.reply_text(
        "📩 Tu as une question, une suggestion ou un bug à signaler ?\n\n"
        "➡️ Envoie-moi directement un message ici sur le bot\n"
        "📬 Ou contacte le support : @KalyosSupport\n\n"
        "🕒 Temps de réponse moyen : moins de 24h.\n"
        "Merci de ton retour, on bosse pour rendre le bot meilleur chaque jour 💪"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aide", aide))
    app.add_handler(CommandHandler("pepites", pepites))
    app.add_handler(CommandHandler("tactiques", tactiques))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot démarré...")
    app.run_polling()  
