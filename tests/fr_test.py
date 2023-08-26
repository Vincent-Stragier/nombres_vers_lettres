# -*- coding: utf-8 -*-
r"""Test of the __main__ module.

Run the test with:
pytest -v tests\fr_test.py
"""
import pytest
from nombres_vers_lettres.make_letters import make_letters

TEST_DATA = [
    # Belgium French
    {
        "number": "0",
        "letters": "zéro",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "28",
        "letters": "vingt-huit",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "31",
        "letters": "trente et un",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "51",
        "letters": "cinquante et un",
        "language": "fr_BE",
        "mode": "cardinal_nominal",
        "post_1990_orthographe": False,
    },
    {
        "number": "51",
        "letters": "cinquante-et-un",
        "language": "fr_BE",
        "mode": "cardinal_nominal",
        "post_1990_orthographe": True,
    },
    {
        "number": "61",
        "letters": "soixante et un",
        "language": "fr_BE",
        "mode": "cardinal_nominal",
        "post_1990_orthographe": False,
    },
    {
        "number": "61",
        "letters": "soixante-et-un",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": True,
    },
    {
        "number": "70",
        "letters": "septante",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "80",
        "letters": "quatre-vingts",
        "mode": "cardinal_nominal",
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
        "mode": "ordinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "81",
        "letters": "quatre-vingt-un",
        "mode": "cardinal_nominal",
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
        "mode": "ordinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "90",
        "letters": "nonante",
        "mode": "cardinal_nominal",
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
        "mode": "ordinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "100",
        "letters": "cent",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "128",
        "letters": "cent vingt-huit",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "200",
        "letters": "deux cents",
        "mode": "cardinal_nominal",
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
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "777",
        "letters": "sept cent septante-sept",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "851",
        "letters": "huit cent cinquante et un",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
    },
    {
        "number": "1000",
        "letters": "mille",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "80000",
        "letters": "quatre-vingt mille",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "80000000",
        "letters": "quatre-vingts millions",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "2000000000",
        "letters": "deux milliards",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    # France French
    {
        "number": "0",
        "letters": "zéro",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
    },
    {
        "number": "51",
        "letters": "cinquante et un",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
    },
    {
        "number": "61",
        "letters": "soixante et un",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
        "post_1990_orthographe": False,
    },
    {
        "number": "61",
        "letters": "soixante-et-un",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
        "post_1990_orthographe": True,
    },
    {
        "number": "71",
        "letters": "soixante et onze",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
        "post_1990_orthographe": False,
    },
    {
        "number": "71",
        "letters": "soixante-et-onze",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
        "post_1990_orthographe": True,
    },
    {
        "number": "91",
        "letters": "quatre-vingt-onze",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
        "post_1990_orthographe": False,
    },
    {
        "number": "100",
        "letters": "cent",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
    },
    {
        "number": "777",
        "letters": "sept cent soixante-dix-sept",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
    },
    {
        "number": "851",
        "letters": "huit cent cinquante et un",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
    },
    {
        "number": "1000",
        "letters": "mille",
        "mode": "cardinal_nominal",
        "language": "fr_FR",
    },
]


@pytest.mark.parametrize("parameters_dict", TEST_DATA)
def test_numbers(parameters_dict):
    """Test the numbers."""
    function_parameters = parameters_dict.copy()
    del function_parameters["letters"]
    assert make_letters(**function_parameters) == parameters_dict["letters"]
