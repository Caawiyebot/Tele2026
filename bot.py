import telebot
from telebot import types
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# --- Configuration ---
# FADLAN BEDDEL 'YOUR_BOT_TOKEN' token-kaaga dhabta ah ee Telegram
TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Database setup (SQLite fudud)
Base = declarative_base()
DATABASE_URL = 'sqlite:///ai_course_data.db'

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    type = Column(String, nullable=False) # 'Free' or 'Paid'
    link = Column(String, nullable=True)
    telegram_id = Column(String, nullable=True)

class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True)
    course_title = Column(String, nullable=False)
    lesson_number = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    video_link = Column(String, nullable=True)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# --- Initial Data Population ---
def populate_data():
    session = Session()
    
    # Check if data already exists to prevent duplication
    if session.query(Course).count() > 0:
        session.close()
        return

    # Courses Data
    courses_data = [
        # Free Courses
        {"title": "AI Video Editing", "description": "Waxaa jira sagaal cashar oo bilaash ah oo ku saabsan hababka ugu dambeeyay ee video editing iyadoo la isticmaalayo adeegyada iyo website-yada casriga ah.", "type": "Free", "link": "https://chat.whatsapp.com/DIu9h23H5R28ozxfMFTkdq", "telegram_id": None},
        {"title": "AI Automation", "description": "Baro sida loo otomatigeyo hawlaha iyadoo la isticmaalayo AI. Casharada waxaa ku jira manhajka AI iyo Chatbot-yada.", "type": "Free", "link": "https://classroom.google.com/c/ODAzMzUwNDIyOTU0?cjc=sdvvlyc2", "telegram_id": None},
        {"title": "AI Shopify", "description": "Baro sida loo dhiso dukaanka Shopify iyadoo la isticmaalayo AI.", "type": "Free", "link": "https://chat.whatsapp.com/DIu9h23H5R28ozxfMFTkdq", "telegram_id": None},
        {"title": "Adobe Premiere Pro", "description": "Casharada aasaasiga ah ee video editing iyadoo la isticmaalayo Adobe Premiere Pro CC 2020.", "type": "Free", "link": "https://www.messenger.com/channel/soomaalipodcast/AbZkquUZAfzDLfvI/", "telegram_id": None},
        {"title": "Basic Language", "description": "Casharada luqadda aasaasiga ah oo ay bixiyaan macallimiin Soomaali ah.", "type": "Free", "link": "https://www.messenger.com/channel/soomaalipodcast", "telegram_id": "@somalienglish3"},
        {"title": "Intermediate Language", "description": "Casharada luqadda dhexe oo loogu talagalay kuwa doonaya inay horumariyaan luqaddooda.", "type": "Free", "link": "https://www.messenger.com/channel/soomaalipodcast/Aba-uQI70rr-LJXY/", "telegram_id": "@somalienglish1"},
        
        # Paid Courses (Placeholder for contact info)
        {"title": "Premium Courses", "description": "Koorsooyin premium ah oo leh khidmad yar oo bille ah. Waxaad heli doontaa casharo gaar ah afar habeen toddobaadkii.", "type": "Paid", "link": "https://chat.whatsapp.com/KzkcjwraeYhCsUXaexgNyM", "telegram_id": "@Mfaratoon"},
    ]

    for data in courses_data:
        session.add(Course(**data))

    # Lessons Data (Example for AI Automation/Chatbot Course)
    # Waxaan isticmaalaynaa casharada manhajka AI iyo Chatbot-yada ee aan horey u sameeyay
    lessons_data = [
        {"course_title": "AI Automation", "lesson_number": 1, "title": "Hordhac ku saabsan AI iyo Chatbots", "content": "Qeexidda AI, taariikhda, iyo codsiyada muhiimka ah.", "video_link": "https://shorturl.at/omOCW"},
        {"course_title": "AI Automation", "lesson_number": 2, "title": "Hababka Barashada Mashiinka", "content": "Barashada la kormeeran, aan la kormeeran, iyo barashada xoojinta.", "video_link": "https://shorturl.at/omOCW"},
        # Ku dar casharada kale ee manhajka halkan
    ]

    for data in lessons_data:
        session.add(Lesson(**data))

    session.commit()
    session.close()

# --- Keyboard Markup Functions ---
def main_menu_markup():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        types.KeyboardButton('Courses 📚'),
        types.KeyboardButton('AI Chatbot 🤖'),
        types.KeyboardButton('AI Video Editing 🎬'),
        types.KeyboardButton('Adobe Premiere Pro 🎥'),
        types.KeyboardButton('Basic Language 🔤'),
        types.KeyboardButton('Intermediate Language 🔠'),
        types.KeyboardButton('Learn AI 🧠'),
        types.KeyboardButton('Talk to Human 👨‍💼')
    )
    return markup

def courses_menu_markup():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        types.KeyboardButton('Free 🆓'),
        types.KeyboardButton('Paid 💰'),
        types.KeyboardButton('Back 🔙')
    )
    return markup

def free_courses_menu_markup():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        types.KeyboardButton('AI Video Editing 🎬'),
        types.KeyboardButton('AI Automation ⚙️'),
        types.KeyboardButton('AI Shopify 🛒'),
        types.KeyboardButton('Adobe Premiere Pro 🎥'),
        types.KeyboardButton('Basic Language 🔤'),
        types.KeyboardButton('Intermediate Language 🔠'),
        types.KeyboardButton('Back 🔙')
    )
    return markup

def back_markup():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(types.KeyboardButton('Back 🔙'))
    return markup

# --- Inline Keyboard Functions ---
def get_lesson_inline_markup(course_title):
    session = Session()
    lessons = session.query(Lesson).filter_by(course_title=course_title).all()
    session.close()
    
    markup = types.InlineKeyboardMarkup()
    for lesson in lessons:
        # Isticmaal callback_data si aad u maamusho jawaabta
        markup.add(types.InlineKeyboardButton(f"Cashar {lesson.lesson_number}: {lesson.title}", callback_data=f"lesson_{lesson.id}"))
    
    # Ku dar button-ka WhatsApp Community
    markup.add(types.InlineKeyboardButton("WhatsApp Group 💬", url="https://shorturl.at/3HXba"))
    
    return markup

# --- Message Handlers ---

@bot.message_handler(commands=['start', 'back'])
def send_welcome(message):
    populate_data() # Hubi in xogta la buuxiyay
    bot.send_message(message.chat.id, "Ku soo dhawoow Chatbot-ka Koorsooyinka AI! Fadlan dooro mid ka mid ah doorashooyinka hoose:", reply_markup=main_menu_markup())

@bot.message_handler(func=lambda message: message.text == 'Back 🔙')
def handle_back(message):
    # Tani waa mid fudud, waxaad u baahan tahay inaad ku darto logic-ka xaaladda (state) si aad u ogaato meesha laga soo laabanayo
    send_welcome(message)

@bot.message_handler(func=lambda message: message.text == 'Courses 📚')
def handle_courses(message):
    bot.send_message(message.chat.id, "Fadlan dooro nooca koorsada:", reply_markup=courses_menu_markup())

@bot.message_handler(func=lambda message: message.text == 'Free 🆓')
def handle_free_courses(message):
    text = "Waxaan bixinaa koorsooyinka ugu horreeya ee Soomaalida ee ku saabsan abuurista chatbot-yada ku hadla luqaddaada, iyada oo aan loo baahnayn aqoonta barnaamijyada. Tani waa isbeddel caalami ah, waxaana kaa caawin doonnaa inaad isticmaasho AI taleefankaaga ama kombuyuutarkaaga si aad u abuurto chatbot-yo AI iyo video editing iyadoo la isticmaalayo AI. Ka mid ah koorsooyinka aan siinay bulshada Soomaaliyeed waa kuwan soo socda:"
    bot.send_message(message.chat.id, text, reply_markup=free_courses_menu_markup())

@bot.message_handler(func=lambda message: message.text == 'Paid 💰')
def handle_paid_courses(message):
    session = Session()
    paid_course = session.query(Course).filter_by(type='Paid').first()
    session.close()
    
    text = paid_course.description if paid_course else "Koorsooyin premium ah oo leh khidmad yar oo bille ah. Tani waxay ku siin doontaa casharo gaar ah afar habeen toddobaadkii. La xiriir macallinka iyo Kooxda AI iyada oo loo marayo kanaaladan:"
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("WhatsApp Group 💬", url=paid_course.link if paid_course else "WHATSAPP_GROUP_LINK_PAID"))
    markup.add(types.InlineKeyboardButton(f"Telegram ID: {paid_course.telegram_id}" if paid_course else "Telegram ID: @Mfaratoon", url=f"https://t.me/{paid_course.telegram_id.replace('@', '')}" if paid_course and paid_course.telegram_id else "https://t.me/Mfaratoon"))
    markup.add(types.InlineKeyboardButton("WhatsApp Community 💬", url="https://shorturl.at/3HXba"))
    
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'AI Chatbot 🤖')
def handle_ai_chatbot(message):
    text = "Halkan, waxaad ku baran doontaa inaad abuurto chatbot-yo aan codayn lahayn iyada oo aan lagu lahayn khibrad hore oo IT ama barnaamijyada. Tan waxaa ka mid ah abuurista chatbot-yo gaar ah oo Telegram, WhatsApp, iyo Messenger ah. Fadlan iska diiwaangeli halkan, ka dibna dir links-kan labada ah sida button 'Lesson' ah:"
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Register 📝", url="https://shorturl.at/O3TSv"))
    markup.add(types.InlineKeyboardButton("AI Automation and Chatbots Course 🤖", callback_data="show_lessons_AI Automation"))
    markup.add(types.InlineKeyboardButton("WhatsApp Group 💬", url="https://shorturl.at/3HXba"))
    
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'AI Video Editing 🎬')
def handle_ai_video_editing(message):
    session = Session()
    course = session.query(Course).filter_by(title='AI Video Editing').first()
    session.close()
    
    text = course.description if course else "Waxaa jira sagaal cashar oo bilaash ah oo ku saabsan hababka ugu dambeeyay ee video editing iyadoo la isticmaalayo adeegyada iyo website-yada casriga ah. Waxaan ka hadli doonaa kuwan si faahfaahsan sagaalka cashar. Si aad u hesho casharada, fadlan raac links-ka hoose:"
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("9 AI Video Editing Lessons 🎬", url=course.link if course else "https://www.youtube.com/user/MrFaraton"))
    markup.add(types.InlineKeyboardButton("WhatsApp Group 💬", url="https://shorturl.at/3HXba"))
    
    bot.send_message(message.chat.id, text, reply_markup=markup)

# --- Callback Query Handler ---
@bot.callback_query_handler(func=lambda call: call.data.startswith('show_lessons_'))
def callback_show_lessons(call):
    course_title = call.data.replace('show_lessons_', '')
    
    # Hubi in ardaygu diiwaangashan yahay (Tani waa meesha aad ku darto logic-kaaga)
    # Hadda, waxaan u malaynaynaa inuu diiwaangashan yahay
    
    bot.send_message(call.message.chat.id, f"Casharrada Koorsada: {course_title}", reply_markup=get_lesson_inline_markup(course_title))
    bot.answer_callback_query(call.id, "Casharrada ayaa la soo bandhigay!")

@bot.callback_query_handler(func=lambda call: call.data.startswith('lesson_'))
def callback_lesson(call):
    lesson_id = int(call.data.replace('lesson_', ''))
    session = Session()
    lesson = session.query(Lesson).get(lesson_id)
    session.close()
    
    if lesson:
        text = f"**Cashar {lesson.lesson_number}: {lesson.title}**\n\n{lesson.content}"
        
        markup = types.InlineKeyboardMarkup()
        if lesson.video_link:
            markup.add(types.InlineKeyboardButton("Daawo Fiidyowga 🎥", url=lesson.video_link))
        
        bot.send_message(call.message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, "Casharka lama helin.")
        
    bot.answer_callback_query(call.id)

# --- Start Polling ---
if __name__ == '__main__':
    print("Bot-ka ayaa bilaabmaya...")
    populate_data()
    bot.infinity_polling()
