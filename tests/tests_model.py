import pytest
import model

records = {}
right_name = 'asd'
right_phone = '123'
new_phone = '321'
non_existent_name = 'dsa'

def test_create():
    model.create_record(records=records, name=right_name, phone=right_phone)
    assert records[right_name] == right_phone

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

def test_read_existent():
    model.read_record(records=records, name=right_name)
    assert records[right_name] == right_phone


def test_read_not_existent():
    with pytest.raises(KeyError):
        model.read_record(records=records, name='dsa')

def test_update():
    model.update_record(records=records, name=right_name, phone=new_phone)
    assert records[right_name] == '321'

def test_update_not_existent():
    with pytest.raises(KeyError):
        model.update_record(records=records, name=non_existent_name)

def test_delete():
    model.delete_record(records=records, name=right_name)
    with pytest.raises(KeyError):
        assert records[right_name] == right_phone

def test_delete_not_existent():
    with pytest.raises(KeyError):
        model.delete_record(records=records, name=non_existent_name)