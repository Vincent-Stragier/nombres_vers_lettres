# -*- coding: utf-8 -*-
SPECIAL_NUMBERS = {
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

TENS_FRENCH = {
    70: "soixante-dix",
    90: "quatre-vingt-dix",
}


# def compute_rank(number: int | float) -> int:
#     """Compute the rank of a number.

#     Args:
#         number (int): The number to compute the rank of.

#     Returns:
#         int: The rank of the number.
#     """
#     if number < 0:
#         raise ValueError(f"Number must be positive (received {number})")

#     return len(str(number).split(".", maxsplit=1)[0]) - 1


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
