import pickle
import openpyxl

# TASK 1

new_dict = {}
with open(r"homeworks/context_manager/task1.txt") as file:
    text_lines = file.readlines()
    for index, line in enumerate(text_lines):
        index += 1
        if index % 2 == 0:
            value = line
            new_dict[key] = value
        else:
            key = line

print(new_dict.keys())
print(new_dict.values(), "\n")
# print(new_dict)
# print(text_lines)

with open(r"homeworks/context_manager/task1.txt", "w") as file:
    for index, line in enumerate(text_lines):
        if index % 2 != 0:
            file.write(line.strip("\n"))

with open(r"homeworks/context_manager/task1.txt") as file:
    text_lines = file.readlines()
print(text_lines)

# TASK 2

with open(r"homeworks/context_manager/task2", "rb") as task_2:
    info = pickle.load(task_2)
    mean_of_numbers = sum(info) / len(info)
print(mean_of_numbers)


# TASK 3


class ExcelOpener(object):
    def __init__(self, path):
        self.path = path
        self.excel_file = openpyxl.load_workbook(self.path)

    def __enter__(self):
        return self.excel_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.excel_file.save(self.path)
            self.excel_file.close()
        else:
            print("\nYOU HAVE A WRONG CODE IN EXCEL_OPENER. REWRITE PLEASE\n")
            self.excel_file.close()
            return True


with ExcelOpener("homeworks/context_manager/excel.xlsx") as excel_file:
    first_sheet = excel_file.active
    text = first_sheet.cell(row=1, column=1)
    print(first_sheet["A1"].value)
    text.value = 'text55'
    raise Exception
