# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() # не возвращает

#inner_function() # ОШИБКА (NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?)
                #ошибка из-за различия пространства имён, т.к. мы не можем доставать значения внутри функции (извне)

test_function()    #работает