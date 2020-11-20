from model.group_form import GroupForm
import random
import string
import os.path
import getopt
import sys
from comtypes.client import CreateObject


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.xlsx"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


# Define random groups
def random_string(prefix, maxlen):
    # Picking symbols for random choice: ascii_letters, digits, punctuation and a number spaces
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " " * 10
    # Random choice of symbols, generated for cycle of random length, not higher than max length
    list_random_symbols = [random.choice(symbols) for i in range(random.randrange(maxlen))]
    random_string_from_symbols_list = prefix + "".join(list_random_symbols)
    return random_string_from_symbols_list


testdata = [GroupForm(group_name=random_string("GN__", 5), group_header=random_string("GH__", 10),
                      group_footer=random_string("GF__", 15)) for i in range(n)]

# Access the file with data.
generator_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(generator_dir)
# Open Excel workbook
xl = CreateObject("Excel.Application")
# Visibility settings, 0 - not visible, 1 - visible
xl.Visible = 1
wb = xl.Workbooks.Add()
# Insert data
for i in range(n):
    group_to_excel = testdata[i].group_name
    xl.Range["A{}".format(i+1)].Value[()] = group_to_excel
# Save and close
file_to_save = os.path.join(root_dir, f)
wb.SaveAs(file_to_save)
xl.Quit()