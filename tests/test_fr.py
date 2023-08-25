# -*- coding: utf-8 -*-
r"""Test of the __main__ module.

Run the test with:
pytest -v tests\test_fr_BE.py
"""
import pytest
from nombres_vers_lettres.make_letters import make_letters

TEST_DATA = [
    # Belgium French
    {
        "number": "0",
        "letters": "zéro",
        "mode": "nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "28",
        "letters": "vingt-huit",
        "mode": "nominal",
        "language": "fr_BE",
    },
    {
        "number": "31",
        "letters": "trente et un",
        "mode": "nominal",
        "language": "fr_BE",
    },
    {
        "number": "51",
        "letters": "cinquante et un",
        "language": "fr_BE",
        "mode": "nominal",
        "post_1990_orthographe": False,
    },
    {
        "number": "51",
        "letters": "cinquante-et-un",
        "language": "fr_BE",
        "mode": "nominal",
        "post_1990_orthographe": True,
    },
    {
        "number": "61",
        "letters": "soixante et un",
        "language": "fr_BE",
        "mode": "nominal",
        "post_1990_orthographe": False,
    },
    {
        "number": "61",
        "letters": "soixante-et-un",
        "mode": "nominal",
        "language": "fr_BE",
        "post_1990_orthographe": True,
    },
    {
        "number": "70",
        "letters": "septante",
        "mode": "nominal",
        "language": "fr_BE",
    },
    {
        "number": "80",
        "letters": "quatre-vingts",
        "mode": "nominal",
        "language": "fr_BE",
    },
    {
        "number": "80",
        "letters": "quatre-vingt",
        "mode": "cardinal",
        "language": "fr_BE",
    },
    {
        "number": "80",
        "letters": "quatre-vingtième",
        "mode": "ordinal",
        "language": "fr_BE",
    },
    {
        "number": "81",
        "letters": "quatre-vingt-un",
        "mode": "nominal",
        "language": "fr_BE",
    },
    {
        "number": "81",
        "letters": "quatre-vingt-un",
        "mode": "cardinal",
        "language": "fr_BE",
    },
    {
        "number": "81",
        "letters": "quatre-vingt-unième",
        "mode": "ordinal",
        "language": "fr_BE",
    },
    {
        "number": "90",
        "letters": "nonante",
        "mode": "nominal",
        "language": "fr_BE",
    },
    {
        "number": "90",
        "letters": "nonante",
        "mode": "cardinal",
        "language": "fr_BE",
    },
    {
        "number": "90",
        "letters": "nonantième",
        "mode": "ordinal",
        "language": "fr_BE",
    },
    {
        "number": "100",
        "letters": "cent",
        "mode": "nominal",
        "language": "fr_BE",
    },
    {
        "number": "128",
        "letters": "cent vingt-huit",
        "mode": "nominal",
        "language": "fr_BE",
    },
    {
        "number": "200",
        "letters": "deux cents",
        "mode": "nominal",
        "language": "fr_BE",
    },
    {
        "number": "200",
        "letters": "deux cent",
        "mode": "cardinal",
        "language": "fr_BE",
    },
    {
        "number": "200",
        "letters": "deux centièmes",
        "mode": "ordinal",
        "language": "fr_BE",
    },
    {
        "number": "777",
        "letters": "sept cent septante-sept",
        "mode": "nominal",
        "language": "fr_BE",
    },
    {
        "number": "851",
        "letters": "huit cent cinquante et un",
        "mode": "nominal",
        "language": "fr_FR",
    },
    {
        "number": "1000",
        "letters": "mille",
        "mode": "nominal",
        "language": "fr_BE",
    },
    # France French
    {"number": "0", "letters": "zéro", "mode": "nominal", "language": "fr_FR"},
    {
        "number": "51",
        "letters": "cinquante et un",
        "mode": "nominal",
        "language": "fr_FR",
    },
    {
        "number": "61",
        "letters": "soixante et un",
        "mode": "nominal",
        "language": "fr_FR",
        "post_1990_orthographe": False,
    },
    {
        "number": "61",
        "letters": "soixante-et-un",
        "mode": "nominal",
        "language": "fr_FR",
        "post_1990_orthographe": True,
    },
    {
        "number": "71",
        "letters": "soixante et onze",
        "mode": "nominal",
        "language": "fr_FR",
        "post_1990_orthographe": False,
    },
    {
        "number": "71",
        "letters": "soixante-et-onze",
        "mode": "nominal",
        "language": "fr_FR",
        "post_1990_orthographe": True,
    },
    {
        "number": "91",
        "letters": "quatre-vingt-onze",
        "mode": "nominal",
        "language": "fr_FR",
        "post_1990_orthographe": False,
    },
    {
        "number": "100",
        "letters": "cent",
        "mode": "nominal",
        "language": "fr_FR",
    },
    {
        "number": "777",
        "letters": "sept cent soixante-dix-sept",
        "mode": "nominal",
        "language": "fr_FR",
    },
    {
        "number": "851",
        "letters": "huit cent cinquante et un",
        "mode": "nominal",
        "language": "fr_FR",
    },
    {
        "number": "1000",
        "letters": "mille",
        "mode": "nominal",
        "language": "fr_FR",
    },
]


@pytest.mark.parametrize("parameters_dict", TEST_DATA)
def test_numbers(parameters_dict):
    """Test the numbers."""
    function_parameters = parameters_dict.copy()
    del function_parameters["letters"]
    assert make_letters(**function_parameters) == parameters_dict["letters"]
