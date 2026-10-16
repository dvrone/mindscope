# Har bir savol: o'lchov, matn va ikkita variant (a, b)
# a va b qaysi harfga ball qo'shishini ko'rsatadi

MBTI_QUESTIONS = [
    # E / I
    {
        "dimension": "EI",
        "text": "Dam olish kunida siz ko'proq nimani afzal ko'rasiz?",
        "a": {"text": "Do'stlar bilan uchrashish va gaplashish", "letter": "E"},
        "b": {"text": "Uyda yolg'iz tinch vaqt o'tkazish", "letter": "I"},
    },
    {
        "dimension": "EI",
        "text": "Yangi odamlar bilan tanishishda siz...",
        "a": {"text": "Birinchi bo'lib gap boshlayman", "letter": "E"},
        "b": {"text": "Avval kuzataman, keyin gaplashaman", "letter": "I"},
    },
    {
        "dimension": "EI",
        "text": "Uzoq kundan keyin energiyangiz qayerdan tiklanadi?",
        "a": {"text": "Odamlar orasida bo'lishdan", "letter": "E"},
        "b": {"text": "Yolg'izlikdan", "letter": "I"},
    },
    # S / N
    {
        "dimension": "SN",
        "text": "Yangi narsani o'rganayotganda siz...",
        "a": {"text": "Aniq faktlar va amaliy misollarni yoqtiraman", "letter": "S"},
        "b": {"text": "G'oya va umumiy tasavvurni yoqtiraman", "letter": "N"},
    },
    {
        "dimension": "SN",
        "text": "Siz o'zingizni qanday ta'riflaysiz?",
        "a": {"text": "Real va amaliy", "letter": "S"},
        "b": {"text": "Xayolparast va ijodkor", "letter": "N"},
    },
    {
        "dimension": "SN",
        "text": "Muammoni hal qilishda siz...",
        "a": {"text": "Sinalgan va tanish usullarga tayanaman", "letter": "S"},
        "b": {"text": "Yangi, noodatiy yechim izlayman", "letter": "N"},
    },
    # T / F
    {
        "dimension": "TF",
        "text": "Qaror qabul qilganda siz nimaga ko'proq tayanasiz?",
        "a": {"text": "Mantiq va xolis tahlilga", "letter": "T"},
        "b": {"text": "His-tuyg'u va odamlarga ta'siriga", "letter": "F"},
    },
    {
        "dimension": "TF",
        "text": "Do'stingiz xato qilsa, siz...",
        "a": {"text": "Xatosini ochiq va to'g'ri aytaman", "letter": "T"},
        "b": {"text": "Xafa qilmaslik uchun yumshoq gapiraman", "letter": "F"},
    },
    {
        "dimension": "TF",
        "text": "Sizga qaysi ta'rif ko'proq mos?",
        "a": {"text": "Adolatli va mantiqiy", "letter": "T"},
        "b": {"text": "Mehribon va tushunuvchan", "letter": "F"},
    },
    # J / P
    {
        "dimension": "JP",
        "text": "Kunlik rejangiz qanday bo'ladi?",
        "a": {"text": "Oldindan aniq rejalashtiraman", "letter": "J"},
        "b": {"text": "Vaziyatga qarab, erkin harakat qilaman", "letter": "P"},
    },
    {
        "dimension": "JP",
        "text": "Topshiriq muddati yaqinlashganda siz...",
        "a": {"text": "Allaqachon tugatib bo'lganman", "letter": "J"},
        "b": {"text": "Oxirgi daqiqalarda eng yaxshi ishlayman", "letter": "P"},
    },
    {
        "dimension": "JP",
        "text": "Sizning ish stolingiz odatda...",
        "a": {"text": "Tartibli va joy-joyida", "letter": "J"},
        "b": {"text": "Biroz tartibsiz, lekin o'zim topaman", "letter": "P"},
    },
    # Qo'shimcha savollar
    {
        "dimension": "EI",
        "text": "Guruhda suhbat paytida siz odatda...",
        "a": {"text": "Ko'p gapiraman va fikrimni darhol aytaman", "letter": "E"},
        "b": {"text": "Ko'proq tinglayman va o'ylab gapiraman", "letter": "I"},
    },
    {
        "dimension": "EI",
        "text": "Katta tadbirda siz...",
        "a": {"text": "Ko'plab odamlar bilan gaplashaman", "letter": "E"},
        "b": {"text": "Bir-ikki yaqin odam bilan chuqur suhbatlashaman", "letter": "I"},
    },
    {
        "dimension": "SN",
        "text": "Sizni nima ko'proq qiziqtiradi?",
        "a": {"text": "Hozir nima bor va qanday ishlaydi", "letter": "S"},
        "b": {"text": "Nima bo'lishi mumkin va nima uchun", "letter": "N"},
    },
    {
        "dimension": "SN",
        "text": "Hikoya yoki voqeani eshitganda siz...",
        "a": {"text": "Aniq tafsilotlarga e'tibor beraman", "letter": "S"},
        "b": {"text": "Umumiy ma'no va yashirin mazmunni izlayman", "letter": "N"},
    },
    {
        "dimension": "TF",
        "text": "Bahsda g'alaba qozonish uchun siz...",
        "a": {"text": "Dalil va faktlarni keltiraman", "letter": "T"},
        "b": {"text": "Suhbatdoshning his-tuyg'ularini hisobga olaman", "letter": "F"},
    },
    {
        "dimension": "TF",
        "text": "Rahbar bo'lsangiz, qaysi sifat muhimroq?",
        "a": {"text": "Adolat va qat'iyat", "letter": "T"},
        "b": {"text": "Hamdardlik va g'amxo'rlik", "letter": "F"},
    },
    {
        "dimension": "JP",
        "text": "Sayohatga chiqishdan oldin siz...",
        "a": {"text": "Marshrut va joylarni oldindan belgilab qo'yaman", "letter": "J"},
        "b": {"text": "Borib ko'rgach, qayerga borishni hal qilaman", "letter": "P"},
    },
    {
        "dimension": "JP",
        "text": "Ish yoki o'qishni boshlashda siz...",
        "a": {"text": "Jadval tuzib, unga amal qilaman", "letter": "J"},
        "b": {"text": "Kayfiyatim kelganda boshlayman", "letter": "P"},
    },
]
