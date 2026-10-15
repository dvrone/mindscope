# Har bir savol: soha, matn va 4 ta variant.
# Har variantda "score" (1-4): 4 eng yuqori emotsional intellektni bildiradi.

EQ_QUESTIONS = [
    # O'zini anglash
    {
        "area": "self_awareness",
        "text": "Kayfiyatingiz birdan yomonlashsa, siz...",
        "options": [
            {"text": "Sababini o'ylab, nima his qilayotganimni aniqlayman", "score": 4},
            {"text": "Biror narsa bilan chalg'iyman", "score": 2},
            {"text": "Atrofdagilardan g'azablanaman", "score": 1},
            {"text": "Sababini bilmasam ham, o'tib ketishini kutaman", "score": 3},
        ],
    },
    {
        "area": "self_awareness",
        "text": "O'z kuchli va zaif tomonlaringizni qanchalik bilasiz?",
        "options": [
            {"text": "Ularni aniq ayta olaman va ustida ishlayman", "score": 4},
            {"text": "Ko'pini bilaman, lekin hammasini emas", "score": 3},
            {"text": "Bu haqda kam o'ylaganman", "score": 2},
            {"text": "Boshqalar aytmasa, bilmayman", "score": 1},
        ],
    },
    {
        "area": "self_awareness",
        "text": "Xato qilganingizda birinchi bo'lib nima qilasiz?",
        "options": [
            {"text": "Aybni boshqalarga yoki vaziyatga yuklayman", "score": 1},
            {"text": "Xatoni tan olib, undan saboq olaman", "score": 4},
            {"text": "Hech kim sezmasin deb yashirishga harakat qilaman", "score": 2},
            {"text": "O'zimni ko'p ayblab, kayfiyatim tushadi", "score": 3},
        ],
    },
    # O'zini boshqarish
    {
        "area": "self_regulation",
        "text": "Kimdir sizni jahlingizni chiqarsa, siz...",
        "options": [
            {"text": "Darhol keskin javob qaytaraman", "score": 1},
            {"text": "Chuqur nafas olib, tinchlangach gapiraman", "score": 4},
            {"text": "Jim bo'lib qolaman, lekin ichimda g'azab saqlanadi", "score": 2},
            {"text": "Suhbatni tark etaman", "score": 3},
        ],
    },
    {
        "area": "self_regulation",
        "text": "Muhim ish oldida bosim va stressni his qilsangiz...",
        "options": [
            {"text": "Vazifalarni ro'yxatga olib, birin-ketin bajaraman", "score": 4},
            {"text": "Ishni oxirgi daqiqaga qoldiraman", "score": 2},
            {"text": "Tashvishdan hech narsaga qo'lim bormaydi", "score": 1},
            {"text": "Biroz dam olib, keyin boshlayman", "score": 3},
        ],
    },
    {
        "area": "self_regulation",
        "text": "Kutilmagan reja o'zgarishiga munosabatingiz?",
        "options": [
            {"text": "Xafa bo'laman va uzoq vaqt o'zimga kelolmayman", "score": 1},
            {"text": "Tezda yangi rejaga moslashaman", "score": 4},
            {"text": "Norozi bo'laman, lekin baribir moslashaman", "score": 3},
            {"text": "Barchasini bekor qilgim keladi", "score": 2},
        ],
    },
    # Empatiya
    {
        "area": "empathy",
        "text": "Do'stingiz xafa bo'lib sizga kelsa, siz...",
        "options": [
            {"text": "Darhol maslahat berib, yechim taklif qilaman", "score": 3},
            {
                "text": "Avval diqqat bilan tinglayman, his-tuyg'ularini tushunishga harakat qilaman",
                "score": 4,
            },
            {"text": "Muammosi unchalik katta emasligini aytaman", "score": 1},
            {
                "text": "Mavzuni o'zgartirib, kayfiyatini ko'tarishga urinaman",
                "score": 2,
            },
        ],
    },
    {
        "area": "empathy",
        "text": "Odamning gapirmasdan turib ham kayfiyatini sezasizmi?",
        "options": [
            {"text": "Ko'pincha sezaman", "score": 4},
            {"text": "Ba'zan sezaman", "score": 3},
            {"text": "Kamdan-kam", "score": 2},
            {"text": "Aytmasa, bilmayman", "score": 1},
        ],
    },
    {
        "area": "empathy",
        "text": "Boshqa odam fikringizga qo'shilmasa, siz...",
        "options": [
            {"text": "Uning fikri noto'g'ri deb hisoblayman", "score": 1},
            {"text": "Nega bunday o'ylashini tushunishga harakat qilaman", "score": 4},
            {"text": "Bahslashmay, shunchaki rozi bo'lgandek turaman", "score": 2},
            {"text": "O'z fikrimni aytib, uniki bilan solishtiraman", "score": 3},
        ],
    },
    # Ijtimoiy ko'nikmalar
    {
        "area": "social",
        "text": "Jamoada nizo chiqsa, siz...",
        "options": [
            {"text": "Aralashmayman, o'zlari hal qilishsin", "score": 2},
            {
                "text": "Tomonlarni tinglab, kelishuvga erishishga yordam beraman",
                "score": 4,
            },
            {"text": "Ko'proq o'zimga yaqin tomonni qo'llayman", "score": 1},
            {"text": "Rahbarga aytaman", "score": 3},
        ],
    },
    {
        "area": "social",
        "text": "Yangi odamlar bilan munosabat o'rnatish siz uchun...",
        "options": [
            {"text": "Juda qiyin, shuning uchun bundan qochaman", "score": 1},
            {"text": "Oson, tez til topishaman", "score": 4},
            {"text": "Biroz vaqt kerak, lekin uddalayman", "score": 3},
            {"text": "Faqat zarur bo'lgandagina urinaman", "score": 2},
        ],
    },
    {
        "area": "social",
        "text": "Biror kishiga tanqidiy fikr bildirishingiz kerak bo'lsa...",
        "options": [
            {"text": "Ochiq va qattiq aytaman, nima bo'lsa bo'lsin", "score": 2},
            {"text": "Hurmat bilan, aniq misollar va yechim bilan aytaman", "score": 4},
            {"text": "Aytmayman, munosabat buzilmasin", "score": 1},
            {"text": "Yumshoq aytaman, lekin maqsadni aniq bildirmayman", "score": 3},
        ],
    },
]
