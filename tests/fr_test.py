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
        "number": "-2222",
        "letters": "moins deux mille deux cent vingt-deux",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "-25",
        "letters": "moins vingt-cinq",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": -25,
        "letters": "moins vingt-cinq",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "0",
        "letters": "zéro",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "0,0001",
        "letters": "un centième de cent",
        "mode": "EUR",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "0,0001",
        "letters": "zéro virgule cent millionièmes",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "0,0002",
        "letters": "deux centièmes de cent",
        "mode": "EUR",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "0,01",
        "letters": "zéro virgule un centième",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "0,01",
        "letters": "un cent",
        "mode": "EUR",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "0,02",
        "letters": "zéro virgule deux centièmes",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "1",
        "letters": "premier",
        "mode": "ordinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "5,100",
        "letters": "cinq euros et dix cents",
        "mode": "EUR",
        "language": "fr_BE",
    },
    {
        "number": "9",
        "letters": "neuvième",
        "mode": "ordinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "25",
        "letters": "vingt-cinq",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": False,
    },
    {
        "number": "25",
        "letters": "vingt-cinquième",
        "mode": "ordinal_nominal",
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
        "mode": "ordinal_adjectival",
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
        "number": "180",
        "letters": "cent quatre-vingts",
        "mode": "cardinal",
        "language": "fr_BE",
    },
    {
        "number": "183",
        "letters": "cent quatre-vingt-trois",
        "mode": "cardinal",
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
        "mode": "ordinal_adjectival",
        "language": "fr_BE",
    },
    {
        "number": "200",
        "letters": "deux centième",
        "mode": "ordinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "3300",
        "letters": "trois mille trois cents",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "420,69",
        "letters": "quatre cent vingt euros et soixante-neuf cents",
        "mode": "EUR",
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
        "number": "1001",
        "letters": "mille-un",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": True,
    },
    {
        "number": "1001",
        "letters": "mille-une",
        "gender": "feminine",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": True,
    },
    {
        "number": 2000,
        "letters": "deux mille",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": 2000,
        "letters": "deux-mille",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": True,
    },
    {
        "number": "80000",
        "letters": "quatre-vingt mille",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "80000",
        "letters": "quatre-vingt-mille",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": True,
    },
    {
        "number": "1000001",
        "letters": "un-million-une",
        "gender": "feminine",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": True,
    },
    {
        "number": "1000001",
        "letters": "un-million-unes",
        "gender": "feminine",
        "plural": True,
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": True,
    },
    {
        "number": "80000000",
        "letters": "quatre-vingts millions",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "80008000",
        "letters": "quatre-vingts millions huit mille",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    {
        "number": "80008000",
        "letters": "quatre-vingts-millions-huit-mille",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": True,
    },
    {
        "number": "2000000000",
        "letters": "deux milliards",
        "mode": "cardinal_nominal",
        "language": "fr_BE",
    },
    # The biggest number that can be written in French
    {
        "number": (
            "9999999999999999999999999999999999999999999999999999999999999999"
            "99,9999999999999999999999999999999999999999999999999999999999999"
            "99"
        ),
        "letters": (
            "neuf-cent-nonante-neuf-décilliards-neuf-cent-nonante-neuf-"
            "décillions-neuf-cent-nonante-neuf-nonilliards-neuf-cent-nonante-"
            "neuf-nonillions-neuf-cent-nonante-neuf-octilliards-neuf-cent-"
            "nonante-neuf-octillions-neuf-cent-nonante-neuf-septilliards-"
            "neuf-cent-nonante-neuf-septillions-neuf-cent-nonante-neuf-"
            "sextilliards-neuf-cent-nonante-neuf-sextillions-neuf-cent-"
            "nonante-neuf-quintilliards-neuf-cent-nonante-neuf-quintillions-"
            "neuf-cent-nonante-neuf-quadrilliards-neuf-cent-nonante-neuf-"
            "quadrillions-neuf-cent-nonante-neuf-trilliards-neuf-cent-"
            "nonante-neuf-trillions-neuf-cent-nonante-neuf-billiards-neuf-"
            "cent-nonante-neuf-billions-neuf-cent-nonante-neuf-milliards-"
            "neuf-cent-nonante-neuf-millions-neuf-cent-nonante-neuf-mille-"
            "neuf-cent-nonante-neuf virgule neuf-cent-nonante-neuf-millièmes-"
            "neuf-cent-nonante-neuf-millionièmes-neuf-cent-nonante-neuf-"
            "milliardièmes-neuf-cent-nonante-neuf-billionièmes-neuf-cent-"
            "nonante-neuf-billiardièmes-neuf-cent-nonante-neuf-trillionièmes-"
            "neuf-cent-nonante-neuf-trilliardièmes-neuf-cent-nonante-neuf-"
            "quadrillionièmes-neuf-cent-nonante-neuf-quadrilliardièmes-neuf-"
            "cent-nonante-neuf-quintillionièmes-neuf-cent-nonante-neuf-"
            "quintilliardièmes-neuf-cent-nonante-neuf-sextillionièmes-neuf-"
            "cent-nonante-neuf-sextilliardièmes-neuf-cent-nonante-neuf-"
            "septillionièmes-neuf-cent-nonante-neuf-septilliardièmes-neuf-"
            "cent-nonante-neuf-octillionièmes-neuf-cent-nonante-neuf-"
            "octilliardièmes-neuf-cent-nonante-neuf-nonillionièmes-neuf-cent-"
            "nonante-neuf-nonilliardièmes-neuf-cent-nonante-neuf-"
            "décillionièmes-neuf-cent-nonante-neuf-décilliardièmes"
        ),
        "mode": "cardinal_nominal",
        "language": "fr_BE",
        "post_1990_orthographe": True,
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
