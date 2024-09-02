from project import main, is_valid, month_to_integer, calculate_age, calculate_days
from datetime import date
from freezegun import freeze_time
from io import StringIO
import pytest


def test_is_valid():
    assert is_valid("October 20, 2000") == ('October', '20', '2000')
    assert is_valid("nov 02,2001") == ('nov', '02', '2001')


def test_is_valid_valueerror():
    with pytest.raises(ValueError):
        is_valid("October 20 2000")
    with pytest.raises(ValueError):
        is_valid("Septembers 05, 2003")
    with pytest.raises(ValueError):
        is_valid("jan 34, 2005")
    with pytest.raises(ValueError):
        is_valid("Feb 11, 200")


def test_month_to_integer():
    assert month_to_integer("oct") == 10
    assert month_to_integer("november") == 11


def test_month_to_integer_valueerror():
    with pytest.raises(ValueError):
        month_to_integer('Septembers')
    with pytest.raises(ValueError):
        month_to_integer('febraury')

@freeze_time("2023-08-21")
def test_calculate_age():
    assert calculate_age("october", 20, 2000, date.today()) == 22
    assert calculate_age("nov", 0o2, 2001, date.today()) == 21

@freeze_time("2023-08-21")
def test_calculate_days():
    assert calculate_days("october", 20, date.today()) == 60
    assert calculate_days("nov", 0o2, date.today()) == 73

@freeze_time("2023-08-21")
def test_main_output(monkeypatch, capfd):
    monkeypatch.setattr('sys.stdin', StringIO('October 20, 2000\n'))

    main()
    cature = capfd.readouterr()
    assert "Your age as of August 21, 2023 is 22 years old." in cature.out
    assert "60 days before your Birthday!" in cature.out
