import pytest
import model
import main
import unittest.mock
import sys
import argparse

records = {}


@unittest.mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(kwarg1='--operation create', kwarg2='--name asd'), kwarg3 = '--phone 123')
def test_args_create(m: unittest.mock.Mock):
    # m.side_effect = ['1,' 'asd', '123']
    main.main(records=records)
    assert records['asd'] == '123'




