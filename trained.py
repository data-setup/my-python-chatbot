from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import csv

# إنشاء كائن البوت
bot = ChatBot(
    'Abdalnasir',
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "maximum_similarity_threshold": 0.95,
            "default_response": "Sorry! Can you rephrase that?"
        }
    ]
)

# استيراد المحادثات من ملف
def import_conversations(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        conversation_list = list(reader)
    return conversation_list

# اسم الملف الذي يحتوي على المحادثات
filename = 'conversations.txt'
conversations = import_conversations(filename)

# تدريب البوت
trainer = ListTrainer(bot)
trainer.train(conversations)

# الدخول في حلقة التفاعل
while True:
    try:
        user_input = input("User: ")
        bot_response = bot.get_response(user_input)
        print(bot_response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        # إنهاء البرنامج بشكل مناسب عند استقبال إشارة إنهاء
        break
