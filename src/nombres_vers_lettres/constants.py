# -*- coding: utf-8 -*-
"""Constants used in the application."""

CURRENCY_FORMS_FR = {
    "EUR": (("euro", "euros"), ("centime", "centimes")),
    "USD": (("dollar", "dollars"), ("cent", "cents")),
    "FRF": (("franc", "francs"), ("centime", "centimes")),
    "GBP": (("livre", "livres"), ("penny", "pence")),
    "CNY": (("yuan", "yuans"), ("fen", "jiaos")),
    "JPY": (("yen", "yens"), ("sen", "sens")),
    "CAD": (("dollar", "dollars"), ("cent", "cents")),
    "AUD": (("dollar", "dollars"), ("cent", "cents")),
    "CHF": (("franc", "francs"), ("centime", "centimes")),
    "HKD": (("dollar", "dollars"), ("cent", "cents")),
    "NZD": (("dollar", "dollars"), ("cent", "cents")),
    "KRW": (("won", "wons"), ("jeon", "jeons")),
    "MXN": (("peso", "pesos"), ("centavo", "centavos")),
    "SGD": (("dollar", "dollars"), ("cent", "cents")),
    "INR": (("roupie", "roupies"), ("paisa", "paise")),
    "RUB": (("rouble", "roubles"), ("kopeck", "kopecks")),
    "ZAR": (("rand", "rands"), ("cent", "cents")),
    "BRL": (("real", "reals"), ("centavo", "centavos")),
    "TRY": (("livre", "livres"), ("kuruş", "kuruş")),
    "TWD": (("dollar", "dollars"), ("cent", "cents")),
    "DKK": (("couronne", "couronnes"), ("øre", "øre")),
    "NOK": (("couronne", "couronnes"), ("øre", "øre")),
    "SEK": (("couronne", "couronnes"), ("øre", "øre")),
    "THB": (("baht", "bahts"), ("satang", "satangs")),
    "IDR": (("roupie", "roupies"), ("sen", "sens")),
    "MYR": (("ringgit", "ringgits"), ("sen", "sens")),
    "PHP": (("peso", "pesos"), ("sentimo", "sentimos")),
    "CZK": (("couronne", "couronnes"), ("halerz", "halerz")),
    "PLN": (("zloty", "zlotys"), ("grosz", "grosz")),
    "BGN": (("lev", "levs"), ("stotinka", "stotinki")),
    "HUF": (("forint", "forints"), ("fillér", "fillérs")),
    "RON": (("leu", "lei"), ("bani", "bani")),
    "HRK": (("kuna", "kunas"), ("lipa", "lipas")),
    "ISK": (("couronne", "couronnes"), ("eyrir", "eyrir")),
    "RSD": (("dinar", "dinars"), ("para", "para")),
    "ILS": (("shekel", "shekels"), ("agora", "agorot")),
    "AED": (("dirham", "dirhams"), ("fils", "fils")),
    "SAR": (("riyal", "riyals"), ("halala", "halalas")),
    "BHD": (("dinar", "dinars"), ("fils", "fils")),
    "KWD": (("dinar", "dinars"), ("fils", "fils")),
    "QAR": (("riyal", "riyals"), ("dirham", "dirhams")),
    "OMR": (("riyal", "riyals"), ("baisa", "baisas")),
    "JOD": (("dinar", "dinars"), ("piastre", "piastres")),
    "LBP": (("livre", "livres"), ("piastre", "piastres")),
    "EGP": (("livre", "livres"), ("piastre", "piastres")),
    "KZT": (("tenge", "tenges"), ("tïın", "tïın")),
    "KGS": (("som", "soms"), ("tyiyn", "tyiyn")),
    "UZS": (("sum", "sums"), ("tiyin", "tiyins")),
    "TJS": (("somoni", "somonis"), ("diram", "dirams")),
    "AZN": (("manat", "manats"), ("qəpik", "qəpiks")),
    "GEL": (("lari", "laris"), ("tetri", "tetris")),
    "AMD": (("dram", "drams"), ("luma", "lumas")),
    "AFN": (("afghani", "afghanis"), ("pul", "puls")),
    "BDT": (("taka", "takas"), ("poisha", "poishas")),
    "LKR": (("roupie", "roupies"), ("cent", "cents")),
    "MMK": (("kyat", "kyats"), ("pya", "pyas")),
    "VND": (("dong", "dongs"), ("hao", "xu")),
    "KHR": (("riel", "riels"), ("sen", "sens")),
    "MOP": (("pataca", "patacas"), ("ho", "ho")),
    "MVR": (("rufiyaa", "rufiyaas"), ("laari", "laaris")),
    "NPR": (("roupie", "roupies"), ("paisa", "paise")),
    "PKR": (("roupie", "roupies"), ("paisa", "paise")),
}

NUMBERS = {
    0: "zéro",
    1: "un",
    2: "deux",
    3: "trois",
    4: "quatre",
    5: "cinq",
    6: "six",
    7: "sept",
    8: "huit",
    9: "neuf",
    10: "dix",
    11: "onze",
    12: "douze",
    13: "treize",
    14: "quatorze",
    15: "quinze",
    16: "seize",
}

# Belgium French
# Democratic Republic of the Congo French
TENS = {
    10: "dix",
    20: "vingt",
    30: "trente",
    40: "quarante",
    50: "cinquante",
    60: "soixante",
    70: "septante",
    80: "quatre-vingt",
    90: "nonante",
    100: "cent",
}

# France French
# Canada French
TENS_FR = {
    70: "soixante-dix",
    90: "quatre-vingt-dix",
}
TENS_FR = TENS | TENS_FR

# Swiss French
# Aosta Valley French
TENS_CH = {80: "huitante"}
TENS_CH = TENS_FR | TENS_CH

LANGUAGES_TENS = {
    "fr_BE": TENS,
    "fr_CD": TENS,
    "fr_FR": TENS_FR,
    "fr_CA": TENS_FR,
    "fr_CH": TENS_CH,
    "fr_IT": TENS_CH,
}

# Long and short scales
# Échelle longue (-illion) et échelle courte (-illiard)
BIG_NUMBERS_BY_RANK = {
    0: "",
    1: "dix",
    2: "cent",
    3: "mille",
    6: "million",
    9: "milliard",
    12: "billion",
    15: "billiard",
    18: "trillion",
    21: "trilliard",
    24: "quadrillion",
    27: "quadrilliard",
    30: "quintillion",
    33: "quintilliard",
    36: "sextillion",
    39: "sextilliard",
    42: "septillion",
    45: "septilliard",
    48: "octillion",
    51: "octilliard",
    54: "nonillion",
    57: "nonilliard",
    60: "décillion",
    63: "décilliard",
}

VALID_FEMININE = ("feminine", "féminin", "feminin", "f")
VALID_MASCULINE = ("masculine", "masculin", "m")
