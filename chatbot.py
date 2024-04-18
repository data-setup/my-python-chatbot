# استيراد الوحدات اللازمة من مكتبة chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# إنشاء كائن البوت مع بعض الخيارات
bot = ChatBot(
    'Mansour',  # اسم البوت
    read_only=False,  # يسمح للبوت بالتعلم من التجارب
    logic_adapters=[  # قائمة المنطق المستخدم
        {
            "import_path": "chatterbot.logic.BestMatch",  # استخدام خوارزمية BestMatch للإجابة
            "maximum_similarity_threshold": 0.95,  # الحد الأقصى للتشابه للاعتبار إجابة مطابقة
            "default_response": "Sorry! Can you rephrase that?"  # الإجابة الافتراضية عند عدم القدرة على الإجابة
        }
    ]
)

# محادثة تجريبية لتدريب البوت
conv = [
    ('hi', 'hello'),  # عند قول "hi"، يجيب البوت "hello"
    ('how old are u?', 'I am ageless'),  # البوت يجيب على سؤال عن العمر بأنه بلا عمر
    ('where are u from', 'from ur imagination')  # البوت يجيب على سؤال المنشأ بأنه من خيال المستخدم
]

# إنشاء مدرب القائمة وتدريب البوت
trainer = ListTrainer(bot)
trainer.train(conv)

# الدخول في حلقة للتفاعل مع البوت
while True:
    inp = input("User: ")  # أخذ الإدخال من المستخدم
    res = bot.get_response(inp)  # الحصول على الإجابة من البوت
    print(res)  # طباعة الإجابة
