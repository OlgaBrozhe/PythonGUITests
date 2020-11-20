import pytest
from fixture.application import Application
import importlib
import os.path
import xlrd


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Users\\olgab\\PycharmProjects\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


# Load test data from Excel file
def pytest_generate_tests(metafunc):
    # To load test data - form fixture, use parameters with prefix "data_", but remove the prefix (first 5 symbols)
    for fixture in metafunc.fixturenames:
        if fixture.startswith("excel_"):
            testdata = load_from_excel(fixture[11:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.{}".format(module)).testdata


def load_from_excel(file):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    excel_file = os.path.join(root_dir, "data/{}.xlsx".format(file))
    wb = xlrd.open_workbook(excel_file)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    excel_data = []
    for i in range(sheet.nrows):
        excel_data.append(sheet.cell_value(i, 0))
    return excel_data


