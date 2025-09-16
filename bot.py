#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN", "8121877943:AAEPprLrwI627XQd9Al7CQGTLvQtyopRKcE")

class DaryReiBot:
    def __init__(self):
        self.application = Application.builder().token(BOT_TOKEN).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Настройка обработчиков команд"""
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("catalog", self.catalog_command))
        self.application.add_handler(CallbackQueryHandler(self.button_callback))
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик команды /start"""
        welcome_text = """🕯 Магазин авторских свечей DaryRei

✨ Уют, аромат и тепло в каждой свече.

Нажмите Старт, чтобы начать работу 🔥"""
        
        keyboard = [
            [InlineKeyboardButton("🚀 Начать покупки", callback_data="start_shopping")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(welcome_text, reply_markup=reply_markup)
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик команды /help"""
        help_text = """Доступные команды:
/start - Начать работу с ботом
/help - Показать эту справку
/catalog - Открыть каталог товаров"""
        await update.message.reply_text(help_text)
    
    async def catalog_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик команды /catalog"""
        await self.show_main_menu(update, context)
    
    async def show_main_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Показать главное меню"""
        text = "Выберите действие:"
        keyboard = [
            [InlineKeyboardButton("ℹ️ О нас", callback_data="about_us")],
            [InlineKeyboardButton("📢 Перейти на основной канал", callback_data="main_channel")],
            [InlineKeyboardButton("🛒 Открыть магазин", callback_data="open_mini_app")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        if update.callback_query:
            await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
        else:
            await update.message.reply_text(text, reply_markup=reply_markup)
    
    async def show_about_us(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Показать раздел 'О нас'"""
        about_text = """Иногда все, что нужно - это отключить мысли и просто улыбаться. 😊 Здесь ты не найдешь место для философских размышлений. Мои свечи идеально подойдут для душевного отдыха в одиночестве или в компании. 🤗 А выбранные запахи, помогут расслабиться, отвлечься от забот и провести вечер с удовольствием. 🕯️

Бывают дни, когда хочется спрятаться от забот, забраться под плед с чашкой чая ☕, и зажечь свечу, которое не требует усилий, но при этом гарантированно поднимает настроение. 😌 Именно для таких случаев и создана эта подборка.

Тебя ждут легкие, теплые, местами романтичные нотки аромата свечей - идеальные спутники для уютного вечера. 🌙✨"""
        
        keyboard = [
            [InlineKeyboardButton("❓ Часто задаваемые вопросы", callback_data="faq")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(about_text, reply_markup=reply_markup)
    
    async def show_main_channel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Показать ссылку на основной канал"""
        text = "Переходите на наш основной канал для новостей и обновлений:"
        keyboard = [
            [InlineKeyboardButton("📢 @daryreflexive1999", url="https://t.me/daryreflexive1999")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    
    async def show_faq(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Показать FAQ"""
        text = "Часто задаваемые вопросы:"
        keyboard = [
            [InlineKeyboardButton("🚚 Сколько времени занимает доставка?", callback_data="faq_delivery")],
            [InlineKeyboardButton("🕯️ Памятка по уходу за свечами", callback_data="faq_care")],
            [InlineKeyboardButton("🪔 Можно ли выбрать воск?", callback_data="faq_wax")],
            [InlineKeyboardButton("🎨 Можно ли выбрать цвет свечи?", callback_data="faq_color")],
            [InlineKeyboardButton("✨ Как сделать свечу уникальной?", callback_data="faq_unique")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_about")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    
    async def show_faq_delivery(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Показать ответ о доставке"""
        text = "Обычно от 2-х дней (зависит от расстояния). 📦"
        keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="faq")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    
    async def show_faq_care(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Показать памятку по уходу за свечами"""
        text = """⚠️ Памятка по уходу за свечами:

• Перед тем как зажечь свечу, обрежьте фитиль (0,5–0,6 см). ✂️
• Зажигайте свечу минимум на час, чтобы воск растаял правильно. ⏰
• Повторное зажигание — не ранее, чем через 2 часа. ⏳
• Не держите свечу дольше 4 часов. 🕐
• Гасите крышкой. 🛡️
• Не оставляйте без присмотра. 👀
• Хранить в прохладном, сухом месте, вдали от солнца. 🌡️"""
        
        keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="faq")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    
    async def show_faq_wax(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Показать ответ о воске"""
        text = "Да, использую соевый и кокосовый воск. 🌱🥥"
        keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="faq")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    
    async def show_faq_color(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Показать ответ о цвете свечи"""
        text = "Да, до двух оттенков или градиент. 🌈"
        keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="faq")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    
    async def show_faq_unique(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Показать ответ об уникальности свечи"""
        text = "Можно добавить сухоцветы, фрукты, сладости, шиммер или минералы. 🌸🍓✨"
        keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="faq")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    
    async def open_mini_app(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Открыть мини-приложение"""
        text = "Открываем магазин..."
        keyboard = [
            [InlineKeyboardButton("🛒 Открыть магазин", web_app=WebAppInfo(url="https://soda2l.github.io/daryrei-mini-app/"))],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    
    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик нажатий на кнопки"""
        query = update.callback_query
        await query.answer()
        
        data = query.data
        
        if data == "start_shopping":
            await self.show_main_menu(update, context)
        elif data == "about_us":
            await self.show_about_us(update, context)
        elif data == "main_channel":
            await self.show_main_channel(update, context)
        elif data == "faq":
            await self.show_faq(update, context)
        elif data == "back_to_main":
            await self.show_main_menu(update, context)
        elif data == "back_to_about":
            await self.show_about_us(update, context)
        elif data == "faq_delivery":
            await self.show_faq_delivery(update, context)
        elif data == "faq_care":
            await self.show_faq_care(update, context)
        elif data == "faq_wax":
            await self.show_faq_wax(update, context)
        elif data == "faq_color":
            await self.show_faq_color(update, context)
        elif data == "faq_unique":
            await self.show_faq_unique(update, context)
        elif data == "open_mini_app":
            await self.open_mini_app(update, context)
    
    def run(self):
        """Запуск бота"""
        logger.info("Запуск бота DaryRei...")
        self.application.run_polling()

if __name__ == "__main__":
    bot = DaryReiBot()
    bot.run()
