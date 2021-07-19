import pytest
import model
import main
import unittest.mock

records = {}


#@unittest.mock.patch('builtins.input')
def test_interactive_create():
    main.main(records=records, args=None)
    #name = 'asd'
    #phone = '123'
    #model.create_record(records=records, name=name, phone=phone)
    #assert records[name] == phone

def test_create_wrong_name():
    name = 'asd1'
    phone = '123'
    with pytest.raises(ValueError):
        model.create_record(records=records, name=name, phone=phone)
        assert records[name] == phone

def test_create_wrong_phone():
    name = 'asd'
    phone = '123a'
    with pytest.raises(ValueError):
        model.create_record(records=records, name=name, phone=phone)
        assert records[name] == phone
