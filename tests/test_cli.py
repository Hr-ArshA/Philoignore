import pytest, argparse

from Philoignore.cli import parser


def test_argparse():
    args = parser.parse_args([])
    assert args.ask == []

    args = parser.parse_args(['capital', 'France'])
    assert args.ask == ['capital', 'France']

