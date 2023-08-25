# -*- coding: utf-8 -*-
"""This modules aims to convert numbers to letters in French.

Interesting links:

https://fr.wikipedia.org/wiki/Noms_des_grands_nombres
https://fr.wikipedia.org/wiki/Nombres_en_fran%C3%A7ais
"""
import re
import traceback

from nombres_vers_lettres.constants import (
    BIG_NUMBERS_BY_RANK,
    CURRENCY_FORMS_FR,
    FRENCH_FRENCH_LIKE,
    LANGUAGES_DECADES,
    NUMBERS,
    VALID_FEMININE,
    VALID_MASCULINE,
)

# TODO: Add support for France's "soixante-dix" and "quatre-vingt-dix"
# TODO: Add support for "-"" or " " syntax
# TODO: Check ordinal/cardinal numbers


def make_currency(
    number: float | int | str,
    currency: str = "EUR",
    decimal_rank: bool = True,
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
        str: _description_
    """
    return (
        float_to_letters(
            number,
            decimal_rank=decimal_rank,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )
        + " "
        + CURRENCY_FORMS_FR[currency]
    )


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
    gender: str = "male",
    plural: bool = False,
) -> str:
    """Convert a cardinal number to an ordinal number.

    Args:
        cardinal_number_str (str): The cardinal number to convert.
        gender (str): male or female (the gender of the ordinal number).
        plural (bool): If True, the ordinal number will be plural.

    Returns:
        str: The ordinal number.
    """
    if cardinal_number_str.endswith("ième") or cardinal_number_str.endswith(
        "ièmes"
    ):
        if cardinal_number_str.endswith("s"):
            cardinal_number_str = cardinal_number_str[:-1]

        return cardinal_number_str + ("s" if plural else "")

    if cardinal_number_str == "un":
        if gender in VALID_FEMININE:
            return "première" if not plural else "premières"

        if gender in VALID_MASCULINE:
            return "premier" if not plural else "premiers"

    ordinal_number_str = cardinal_number_str
    suffix = "ième"
    if plural:
        suffix += "s"

    match cardinal_number_str[-1]:
        case "q":
            ordinal_number_str += "u" + suffix
        case "s":
            return cardinal_number_str[:-1] + suffix
        case "e":
            return cardinal_number_str[:-1] + suffix
        case _:
            ordinal_number_str += suffix

    return ordinal_number_str


# If you can build a number between 0 and 99, you can build any number.


def positive_integer_under_one_hundred(
    number: int,
    cardinal: bool = False,
    post_1990_orthographe: bool = False,
    language: str = "fr_BE",
) -> str:
    """Convert a integer between 0 and under 100 to letters.

    Args:
        number (int): The number to convert.
        cardinal (bool, optional): If True, use cardinal numbers.
        Defaults to False.
        post_1990_orthographe (bool, optional): If True, use tiret with "et".
        Defaults to False.

    Raises:
        ValueError: If the number is over 99.
    """
    if number >= 100:
        raise ValueError(f"Number must be under 100 (received {number})")

    if number % 1 != 0:
        raise ValueError(
            "Number must be an integer "
            f"(received {number}, type {type(number)})"
        )

    # 80 is a special case (4 time 20)
    decades = LANGUAGES_DECADES[language]
    if number == 80 and cardinal is False:
        return decades[number] + ("s" if decades[number] else "")

    # Directly lookup decades
    if number in (NUMBERS | decades):
        return (NUMBERS | decades).get(number, "")

    # # Directly lookup special numbers (0-16)
    # if number in NUMBERS:
    #     return NUMBERS[number]

    if language in FRENCH_FRENCH_LIKE:
        if 71 < number < 80:
            return "soixante-" + positive_integer_under_one_hundred(
                number - 60
            )

        if 90 < number < 100:
            return "quatre-vingt-" + positive_integer_under_one_hundred(
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
            return "quatre-vingt-un"

        if post_1990_orthographe:
            return decades[number - 1] + "-et-un"

        return decades[number - 1] + " et un"

    return decades[number - number % 10] + "-" + NUMBERS[number % 10]


def positive_integer_under_one_thousand(
    number: int,
    cardinal: bool = False,
    post_1990_orthographe: bool = False,
    language: str = "fr_BE",
) -> str:
    """Convert a integer between 0 and under 1000 to letters.

    Args:
        number (int): The number to convert.
        cardinal (bool, optional): If True, use cardinal numbers.
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

    if number < 100:
        return positive_integer_under_one_hundred(
            number,
            cardinal=cardinal,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    if number == 100:
        return "cent"

    # Form numbers over 100
    # Form the part under 100 (xx)
    under_hundred_part_str = positive_integer_under_one_hundred(
        number % 100,
        cardinal=cardinal,
        post_1990_orthographe=post_1990_orthographe,
        language=language,
    )
    under_hundred_part_str = (
        space + under_hundred_part_str if number % 100 != 0 else ""
    )

    # Form the part over 100 (yxx)
    hundreds_part = (number - (number % 100)) // 100
    hundreds_part_str = (
        positive_integer_under_one_hundred(
            hundreds_part,
            cardinal=cardinal,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )
        + space
    )
    if hundreds_part == 1:
        hundreds_part_str = ""
    cent = "cent" + (
        "s"
        if hundreds_part > 1 and number % 100 == 0 and cardinal is False
        else ""
    )

    return hundreds_part_str + cent + under_hundred_part_str


def integer_to_letters(
    number: int | str,
    decimal: bool = False,
    decimal_rank: bool = True,
    cardinal: bool = False,
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
        cardinal (bool, optional): If True, use cardinal numbers.
        Defaults to False.
        post_1990_orthographe (bool, optional): If True, use tiret with "et",
        etc.
        Defaults to False.

    Raises:
        ValueError: If the number is not an integer.

    Returns:
        str: The number in letters.
    """
    exact_number = ""
    if isinstance(number, str):
        exact_number = number
        number = int(number)

    if number % 1 != 0:
        raise ValueError(
            "Number must be an integer "
            f"(received {number}, type {type(number)})"
        )

    if number < 0:
        return "moins " + integer_to_letters(-number)

    if number < 1000 and not decimal:
        return positive_integer_under_one_thousand(
            number,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    # Divide number in groups of 3 digits
    # Convert number to string (remove scientific notation)
    number_str = exact_number

    if exact_number == "":
        number_str = f"{number:.0f}"

    # Compute "rank"
    rank = len(number_str) // 3 * 3

    if len(number_str) % 3:
        rank += 3

    # print(f"{number_str = }, {rank = }, {len(number_str) = }")

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

        # print(f'{group = }, {group_rank = }, {ranks[group_rank] = }')

        # The group is empty, we skip it
        if int(group) == 0:
            continue

        # Add a space between groups
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

        use_cardinals = group_rank > 2 or cardinal

        if int(group) == 1 and group_rank < 6:
            group_str = ""

        else:
            group_str = positive_integer_under_one_thousand(
                int(group),
                cardinal=use_cardinals,
                post_1990_orthographe=post_1990_orthographe,
                language=language,
            )
            group_str += space if rank_str != "" else ""

        number_str += group_str + rank_str

    return number_str


def float_to_letters(
    number: float | int | str,
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
    # If the number is a string there is not conversion error
    exact_number = ""
    if isinstance(number, str):
        exact_number = number
        exact_number = re.sub(r"[^\-\d\.\,\n]+", "", exact_number)

        if exact_number.count(".") > 1:
            raise ValueError("Invalid number: too many decimal points (.)")

        if exact_number.count(",") > 1:
            raise ValueError("Invalid number: too many decimal points (,)")

        exact_number = exact_number.replace(",", ".")

        if "-" in exact_number and not exact_number.startswith("-"):
            raise ValueError(
                "Invalid number: negative sign must be at the beginning"
            )

        if exact_number.count("-") > 1:
            raise ValueError("Invalid number: too many negative signs")

        number = 1
        if exact_number.startswith("-"):
            number = -1

    if number % 1 == 0 and exact_number == "":
        return integer_to_letters(
            int(number),
            decimal_rank=decimal_rank,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    # Check if the number is negative
    if number < 0:
        if exact_number != "":
            exact_number = exact_number.replace("-", "")
            number = exact_number
        return "moins " + float_to_letters(
            number,
            decimal_rank=decimal_rank,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    number_str = f"{number}".split(".")

    if exact_number != "":
        number_str = exact_number.split(".")

    integer_part = number_str[0]

    if len(number_str) == 1:
        return integer_to_letters(
            integer_part,
            decimal_rank=decimal_rank,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    decimal_part = number_str[1]

    return (
        integer_to_letters(
            integer_part,
            cardinal=True,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )
        + " virgule "
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
    mode: str = "nominal",
    language: str = "fr_BE",
    post_1990_orthographe: bool = False,
) -> str:
    """Convert a number to letters.

    Args:
        number (float | int | str): The number to convert.
        mode (str, optional): The mode to use. Defaults to "nominal".
        language (str, optional): The language to use. Defaults to "fr_BE".
        post_1990_orthographe (bool, optional): If True, use tiret with "et",
        etc.
        Defaults to False.

    Returns:
        str: The number in letters.
    """
    if mode == "nominal":
        return float_to_letters(
            number,
            decimal_rank=False,
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

    if mode == "cardinal":
        return integer_to_letters(
            number,
            decimal_rank=True,
            post_1990_orthographe=post_1990_orthographe,
            language=language,
        )

    if mode == "ordinal":
        return make_ordinal(
            integer_to_letters(
                number,
                decimal_rank=True,
                post_1990_orthographe=post_1990_orthographe,
                language=language,
            )
        )

    raise ValueError(f"Invalid mode {mode = }")
