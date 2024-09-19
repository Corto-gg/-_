def test_function ():
    def inner_function ():
        print (" в области видимости функции test_function")
    inner_function()                                                       #Ничего не происходит


inner_function()                                                           #Ошибка т.к мы не можем достать значение функции извне







