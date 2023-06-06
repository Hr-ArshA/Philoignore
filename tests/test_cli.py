import pytest, argparse

from Philoignore.cli import parser


def test_argparse():
    args = parser.parse_args([])
    assert args.entry == []

    args = parser.parse_args(['python venv'])
    assert args.entry == ['python venv']

