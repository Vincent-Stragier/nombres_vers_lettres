# -*- coding: utf-8 -*-
"""This modules aims to convert numbers to letters in French.

Interesting links:

https://fr.wikipedia.org/wiki/Noms_des_grands_nombres
https://fr.wikipedia.org/wiki/Nombres_en_fran%C3%A7ais
"""
import re
import traceback

from nombres_vers_lettres.constants import (  # CURRENCY_FORMS_FR,
    BIG_NUMBERS_BY_RANK,
    CURRENCY_FORMS_FR,
    CURRENCY_FORMS_FR_CODES,
    FRENCH_FRENCH_LIKE,
    LANGUAGES_DECADES,
    NUMBERS,
    VALID_FEMININE,
    VALID_MASCULINE,
)


def make_currency(
    number: float | int | str,
    currency: str = "EUR",
    post_1990_orthographe: bool = True,
    language: str = "fr_BE",
) -> str:
    """Convert a number to a currency.

    Args:
        number (float | int | str): The number to convert.
        currency (str, optional): Defaults to "EUR".
        decimal_rank (bool, optional): Defaults to True.
        post_1990_orthographe (bool, optional): Defaults to False.

    Returns:
        str: The number in letters.
    """
    number_int_or_float, number_str = numbers(number, mode="float")

    # Check if the number is an integer
    if "." not in number_str:
        plural = 1 if number_int_or_float > 1 else 0

        return (
            integer_to_letters(
                number_str,
                post_1990_orthographe=post_1990_orthographe,
                language=language,
            )
            + " "
            + CURRENCY_FORMS_FR[currency][0][plural]
        )

    if -1 < number_int_or_float < 1:
        number_str = number_str.split(".")[1].rstrip("0").ljust(2, "0")

        separator = " "
        if len(number_str) > 2:
            number_str = number_str[:2] + "." + number_str[2:]
            separator = " de "

        plural = 1 if float(number_str) > 1 else 0

        if number_int_or_float < 0:
            number_str = "-" + number_str

        return (
            float_to_letters(
                number_str,
                post_1990_orthographe=post_1990_orthographe,
                language=language,
            ).replace("zéro virgule ", "")
            + separator
            + CURRENCY_FORMS_FR[currency][1][plural]
        )

    integer_part, decimal_part = number_str.split(".")

    return (
        make_currency(
            integer_part,
            currency=currency,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )
        + " et "
        + make_currency(
            f"0.{decimal_part}",
            currency=currency,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )
    )


def numbers(
    number: int | float | str, mode: str = "int"
) -> tuple[float | int, str]:
    """Create a float or int and a string of the number.

    Args:
        number (int | float | str): The number to convert.
        mode (str, optional): The mode to use. Defaults to "int".

    Raises:
        ValueError: If the number is invalid.

    Returns:
        tuple[float | int, str]: The number as a float or int and a string.
    """
    number_str = ""
    number_int_or_float = 0

    if isinstance(number, str):
        number_str = number
        number_str = re.sub(r"[^\-\d\.\,\n]+", "", number_str)

        if number_str.count(".") > 1:
            raise ValueError("Invalid number: too many decimal points (.)")

        if number_str.count(",") > 1:
            raise ValueError("Invalid number: too many decimal points (,)")

        # Only keep the decimal point
        number_str = number_str.replace(",", ".")

        if "-" in number_str and not number_str.startswith("-"):
            raise ValueError(
                "Invalid number: negative sign must be at the beginning"
            )

        if number_str.count("-") > 1:
            raise ValueError("Invalid number: too many negative signs")

        if number_str == "":
            raise ValueError("Invalid number: empty string")

        # Create a number
        if "." not in number_str:
            number_int_or_float = int(number_str)

        else:
            number_int_or_float = float(number_str)

    if isinstance(number, (int, float)):
        number_int_or_float = number

        if mode == "int" or number % 1 == 0:
            number_str = f"{number:.0f}"

        elif mode == "float":
            number_str = f"{number}"

    return number_int_or_float, number_str


def big_number_from_rank(rank: int) -> str:
    """Get the big number from a rank.

    Args:
        rank (int): The rank of the number.

    Raises:
        ValueError: If the rank is negative.

    Returns:
        str: The big number.
    """
    if rank < 0:
        raise ValueError(f"Number must be positive (received {rank})")

    try:
        return BIG_NUMBERS_BY_RANK[rank]
    except KeyError as exception:
        traceback.print_exc()
        raise ValueError(
            f"Rank value ({rank = }) out of range."
        ) from exception


def decimal_from_rank(rank: int) -> str:
    """Get the decimal number from a rank.

    Args:
        rank (int): The rank of the number.

    Raises:
        ValueError: If the rank is negative.

    Returns:
        str: The decimal number.
    """
    if rank < 0:
        raise ValueError(f"Number must be positive (received {rank})")

    return make_ordinal(BIG_NUMBERS_BY_RANK.get(rank, "ERROR_NO_RANK_FOUND"))


def make_ordinal(
    cardinal_number_str: str,
    gender: str = "masculin",
    plural: bool = False,
) -> str:
    """Convert a cardinal number to an ordinal number.

    Args:
        cardinal_number_str (str): The cardinal number to convert.
        gender (str): masculine or feminine (the gender of the ordinal number).
        plural (bool): If True, the ordinal number will be plural.

    Returns:
        str: The ordinal number.
    """
    # Number is already an ordinal number
    if cardinal_number_str.endswith(("ième", "ièmes")):
        if cardinal_number_str.endswith("s"):
            cardinal_number_str = cardinal_number_str[:-1]

        return cardinal_number_str + ("s" if plural else "")

    if cardinal_number_str in ("un", "une"):
        if gender in VALID_FEMININE:
            return "première" if not plural else "premières"

        if gender in VALID_MASCULINE:
            return "premier" if not plural else "premiers"

    ordinal_number_str = cardinal_number_str
    suffix = "ième"

    if plural:
        suffix += "s"

    match cardinal_number_str[-1]:
        case "e":
            return cardinal_number_str[:-1] + suffix
        case "f":
            return cardinal_number_str[:-1] + "v" + suffix
        case "q":
            ordinal_number_str += "u" + suffix
        case "s":
            return cardinal_number_str[:-1] + suffix
        case _:
            ordinal_number_str += suffix

    return ordinal_number_str


# If you can build a number between 0 and 99, you can build any number.


def positive_integer_up_to_one_hundred(
    number: int,
    gender: str = "masculin",
    plural: bool = False,
    ordinal: bool = False,
    post_1990_orthographe: bool = False,
    language: str = "fr_BE",
) -> str:
    """Convert a integer between 0 and 100 included to letters.

    Args:
        number (int): The number to convert.
        ordinal (bool, optional): If True, use ordinal numbers.
        Defaults to False.
        post_1990_orthographe (bool, optional): If True, use tiret with "et".
        Defaults to False.

    Raises:
        ValueError: If the number is over 99.
    """
    if number > 100:
        raise ValueError(
            f"Number must be under or equal to 100 (received {number})"
        )

    if number % 1 != 0:
        raise ValueError(
            "Number must be an integer "
            f"(received {number}, type {type(number)})"
        )

    # 80 is a special case (4 times 20)
    decades = LANGUAGES_DECADES[language]
    if number == 80 and decades[80] == "quatre-vingt" and ordinal is False:
        return decades[number] + ("s" if decades[number] else "")

    UN = "une" if gender in VALID_FEMININE and ordinal is False else "un"

    if number == 1:
        return UN + "s" if plural else UN

    # Directly lookup decades
    if number in (NUMBERS | decades):
        return (NUMBERS | decades).get(number, "")

    if language in FRENCH_FRENCH_LIKE:
        if 71 < number < 80:
            return "soixante-" + positive_integer_up_to_one_hundred(
                number - 60
            )

        if 90 < number < 100:
            return "quatre-vingt-" + positive_integer_up_to_one_hundred(
                number - 80
            )

        if number == 71:
            return (
                "soixante-et-onze"
                if post_1990_orthographe
                else "soixante et onze"
            )

    if number % 10 == 1:
        if number == 81 and decades[80] == "quatre-vingt":
            return f"quatre-vingt-{UN}"

        if post_1990_orthographe:
            return decades[number - 1] + f"-et-{UN}"

        return decades[number - 1] + f" et {UN}"

    return decades[number - number % 10] + "-" + NUMBERS[number % 10]


def positive_integer_under_one_thousand(
    number: int,
    gender: str = "masculin",
    plural: bool = False,
    ordinal: bool = False,
    post_1990_orthographe: bool = False,
    language: str = "fr_BE",
) -> str:
    """Convert a integer between 0 and under 1000 to letters.

    Args:
        number (int): The number to convert.
        ordinal (bool, optional): If True, use ordinal numbers.
        Defaults to False.
        post_1990_orthographe (bool, optional): If True, use tiret with "et",
        etc.
        Defaults to False.

    Raises:
        ValueError: If the number is over 999.
    """
    space = " " if not post_1990_orthographe else "-"

    if number >= 1000:
        raise ValueError(f"Number must be under 1000 (received {number})")

    if number % 1 != 0:
        raise ValueError(
            "Number must be an integer "
            f"(received {number}, type {type(number)})"
        )

    if number <= 100:
        return positive_integer_up_to_one_hundred(
            number,
            gender=gender,
            plural=plural,
            ordinal=ordinal,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    # Form numbers over 100
    # Form the part under 100 (xx)
    under_hundred_part_str = positive_integer_up_to_one_hundred(
        number % 100,
        ordinal=ordinal,
        post_1990_orthographe=post_1990_orthographe,
        language=language,
    )
    under_hundred_part_str = (
        space + under_hundred_part_str if number % 100 != 0 else ""
    )

    # Form the part over 100 (yxx)
    hundreds_part = (number - (number % 100)) // 100
    hundreds_part_str = (
        positive_integer_up_to_one_hundred(
            hundreds_part,
            ordinal=ordinal,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )
        + space
    )
    if hundreds_part == 1:
        hundreds_part_str = ""
    cent = "cent" + (
        "s"
        if hundreds_part > 1 and number % 100 == 0 and ordinal is False
        else ""
    )

    return hundreds_part_str + cent + under_hundred_part_str


def integer_to_letters(
    number: int | str,
    decimal: bool = False,
    decimal_rank: bool = True,
    plural: bool = False,
    gender: str = "masculin",
    ordinal: bool = False,
    post_1990_orthographe: bool = False,
    language: str = "fr_BE",
) -> str:
    """Convert an integer to letters.

    Args:
        number (int | str): The number to convert.
        decimal (bool, optional): If True, the number is a decimal.
        Defaults to False.
        decimal_rank (bool, optional): If True, keep the decimal rank for
        low ranks. Defaults to True.
        ordinal (bool, optional): If True, use ordinal numbers.
        Defaults to False.
        post_1990_orthographe (bool, optional): If True, use tiret with "et",
        etc.
        Defaults to False.

    Raises:
        ValueError: If the number is not an integer.

    Returns:
        str: The number in letters.
    """
    number_int, number_str = numbers(number, mode="int")

    if not isinstance(number_int, int):
        raise ValueError(
            "Number must be an integer "
            f"(received {number}, type {type(number)})"
        )

    # Check if the number is negative
    if number_int < 0:
        return "moins " + integer_to_letters(
            number_str.replace("-", ""), language=language
        )

    # We already have a function for numbers under 1000
    if number_int < 1000 and not decimal:
        return positive_integer_under_one_thousand(
            number_int,
            gender=gender,
            plural=plural,
            ordinal=ordinal,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    # Compute "rank"
    rank = len(number_str) // 3 * 3

    if len(number_str) % 3:
        rank += 3

    number_groups = []

    if not decimal:
        ranks = big_number_from_rank
        while len(number_str) > 0:
            number_groups.append(number_str[-3:])
            number_str = number_str[:-3]
        number_groups.reverse()

    else:
        ranks = decimal_from_rank
        # We are grouping the decimal part
        while len(number_str) > 0:
            number_groups.append(number_str[:3])
            number_str = number_str[3:]

    number_str = ""
    for index, group in enumerate(number_groups):
        # Compute current rank
        group_rank = 3 * (index + 1)
        if not decimal:
            group_rank = rank - group_rank

        # The group is empty, we skip it
        if int(group) == 0:
            continue

        # Add a space or a tiret between groups
        space = " " if not post_1990_orthographe else "-"
        if number_str != "":
            number_str += space

        rank_str = ranks(group_rank)
        if group_rank > 3:
            rank_str += "s" if int(group) > 1 and group_rank > 2 else ""

            # We need to pad the group with 0s
            if decimal and len(group) < 3:
                group = group.ljust(3, "0")
                rank_str += "s"

        # With low ranks, we keep the decimal rank
        elif decimal:
            # Recompute rank
            rank_str = ranks(len(group))
            rank_str += "s" if int(group) > 1 and group_rank > 2 else ""

            # We may remove the decimal rank for low ranks
            if len(group) < 3 and decimal_rank is False:
                rank_str = ""

        # Use ordinal in from of "mille" or
        # if the user wants to use ordinal numbers
        use_ordinal = group_rank == 3 or ordinal

        # We don't say "un cent" or "un mille", we say "mille" or "cent"
        # We do say "un million" or "un milliard", etc.
        # We do say "un dixième", "un centième", etc.
        if int(group) == 1 and group_rank < 6 and not decimal:
            group_str = ""

        else:
            group_str = positive_integer_under_one_thousand(
                int(group),
                ordinal=use_ordinal,
                post_1990_orthographe=post_1990_orthographe,
                language=language,
            )
            group_str += space if rank_str != "" else ""

        number_str += group_str + rank_str

    return number_str


def float_to_letters(
    number: float | int | str,
    gender: str = "masculin",
    plural: bool = False,
    decimal_rank: bool = True,
    post_1990_orthographe: bool = False,
    language: str = "fr_BE",
) -> str:
    """Convert a float to letters.

    Args:
        number (float | int): The number to convert.
        decimal_rank (bool, optional): If True, keep the decimal rank for low
        ranks. Defaults to True.

    Returns:
        str: The number in letters.
    """
    number, exact_number = numbers(number, mode="float")

    # Check if the number is negative
    if number < 0:
        # Recursively call the function
        return "moins " + float_to_letters(
            exact_number.replace("-", ""),
            gender=gender,
            plural=plural,
            decimal_rank=decimal_rank,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    number_str = exact_number.split(".")
    integer_part = number_str[0]

    # If the number is an integer, we don't need to convert the decimal part
    if len(number_str) == 1:
        return integer_to_letters(
            integer_part,
            gender=gender,
            plural=plural,
            decimal_rank=decimal_rank,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    decimal_part = number_str[1]

    return (
        integer_to_letters(
            integer_part,
            ordinal=False,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )
        + " virgule "
        + integer_to_letters(
            decimal_part,
            decimal=True,
            decimal_rank=decimal_rank,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )
    )


def make_letters(
    number: float | int | str,
    mode: str = "ordinal",
    gender: str = "masculin",
    plural: bool = False,
    language: str = "fr_BE",
    post_1990_orthographe: bool = False,
) -> str:
    """Convert a number to letters.

    Args:
        number (float | int | str): The number to convert.
        mode (str, optional): The mode to use. Defaults to "ordinal".
        language (str, optional): The language to use. Defaults to "fr_BE".
        post_1990_orthographe (bool, optional): If True, use tiret with "et",
        etc.
        Defaults to False.

    Returns:
        str: The number in letters.
    """
    if mode in ("cardinal", "cardinal_nominal"):
        # un, deux, trois virgule cinq
        return float_to_letters(
            number,
            gender=gender,
            plural=plural,
            decimal_rank=True,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    if isinstance(number, float):
        if number % 1 == 0:
            number = int(number)
        else:
            raise ValueError(
                "Invalid number: float number must be an integer "
                f"(received {number}, type {type(number)})"
            )

    if mode in ("ordinal_adjectival", "ordinal"):
        # la page trois, la page deux cent, etc.
        ordinal_adjectival = integer_to_letters(
            number,
            ordinal=True,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

        return ordinal_adjectival

    if mode == "ordinal_nominal":
        # 3 -> troisième, etc.
        return make_ordinal(
            integer_to_letters(
                number,
                post_1990_orthographe=post_1990_orthographe,
                language=language,
            ),
            gender=gender,
            plural=plural,
        )

    if mode in CURRENCY_FORMS_FR_CODES:
        return make_currency(
            number,
            currency=mode,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    raise ValueError(f"Invalid mode {mode = }")
