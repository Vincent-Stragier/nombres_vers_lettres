# -*- coding: utf-8 -*-
"""Main entry point for the application when run with the -m switch."""
import argparse
import os
import sys

from nombres_vers_lettres.constants import VALID_FEMININE, VALID_MASCULINE
from nombres_vers_lettres.make_letters import float_to_letters


def main():
    """Main entry point for the application when run with the -m switch."""

    parser = argparse.ArgumentParser(os.path.basename(sys.argv[0]))

    # Add the positional argument for the number
    parser.add_argument(
        "number",
        type=str,
        help="The number as a string to convert to letters (in French)",
    )

    # Add mutually exclusive arguments for nominal, cardinal and ordinal
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--mode",
        type=str,
        help=(
            "The mode to use for the conversion "
            "(nominal, cardinal or ordinal)"
        ),
        default=None,
    )
    group.add_argument(
        "--nominal",
        "-n",
        action="store_true",
        help=(
            "Convert the number to nominal letters (e.g. 'un' -> 'une') "
            "(default)"
        ),
        default=None,
    )
    group.add_argument(
        "--cardinal",
        "-c",
        action="store_true",
        help="Convert the number to cardinal letters (e.g. 'un' -> 'un')",
        default=None,
    )
    group.add_argument(
        "--ordinal",
        "-o",
        action="store_true",
        help="Convert the number to ordinal letters (e.g. 'un' -> 'premier')",
        default=None,
    )

    # Add mutually exclusive arguments for masculine and feminine
    group = parser.add_mutually_exclusive_group()

    feminine = ", ".join(VALID_FEMININE)
    masculine = ", ".join(VALID_MASCULINE)

    group.add_argument(
        "--gender",
        "-g",
        help=(
            "The gender to use for the conversion "
            f"({feminine} or {masculine}), default is masculine"
        ),
        type=str,
        default=None,
    )

    group.add_argument(
        "--masculine",
        "-m",
        action="store_true",
        help="Convert the number to masculine letters (e.g. 'un' -> 'un')",
        default=None,
    )
    group.add_argument(
        "--feminine",
        "-f",
        action="store_true",
        help="Convert the number to feminine letters (e.g. 'un' -> 'une')",
        default=None,
    )

    parser.add_argument(
        "--use-tiret",
        "-t",
        action="store_true",
        help="Use the tiret character everywhere (e.g. 'vingt-et-un')",
        default=None,
    )

    # parser.add_argument(
    #     "--config", "-c", type=str, help="Path to the config file"
    # )
    # parser.add_argument(
    #     "--prompt",
    #     "-p",
    #     type=str,
    #     default="",
    #     help="Use the prompt file instead of the default text",
    # )

    args = parser.parse_args()

    # if args.config:
    # print(args)
    print(
        float_to_letters(
            args.number, post_1990_orthograph=args.post_1990_orthograph
        )
    )


if __name__ == "__main__":
    main()

elif __name__ == "nombres_vers_lettres.__main__":
    # Do nothing
    pass

else:
    raise RuntimeError("Only for use with the -m switch, not as a Python API")
