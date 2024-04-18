# استيراد الفئة ChatBot من مكتبة chatterbot
from chatterbot import ChatBot

# إنشاء كائن البوت مع الخيارات اللازمة
bot = ChatBot(
    'SQLMemoryTerminal',  # اسم البوت
    read_only=False,  # السماح للبوت بالتعلم من التفاعلات (لا يعمل بوضع القراءة فقط)
    storage_adapter='chatterbot.storage.SQLStorageAdapter',  # استخدام محول التخزين SQL لحفظ البيانات
    logic_adapters=[  # استخدام خوارزمية BestMatch في المنطق
        {
            "import_path": "chatterbot.logic.BestMatch",  # المسار إلى خوارزمية BestMatch
            "maximum_similarity_threshold": 0.95,  # الحد الأقصى لمعيار التشابه للإجابات
            "default_response": "Sorry! Can you rephrase that?"  # الرد الافتراضي إذا لم يتم العثور على إجابة مناسبة
        }
    ],
    database='db.sqlite3'  # اسم قاعدة البيانات حيث سيتم تخزين البيانات
)

# الدخول في حلقة لا نهائية للتفاعل مع البوت
while True:
    inp = input("User: ")  # استقبال الإدخال من المستخدم
    res = bot.get_response(inp)  # الحصول على الاستجابة من البوت
    print(res)  # طباعة استجابة البوت
