from myfirsttestnotebook import some_function


def test_some_function():
    #assert some_function(2) == 4
    assert some_function(3) == 6
    assert some_function(0) == 0
    assert some_function(-1) == -2
