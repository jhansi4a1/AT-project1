##pytest for title of the page##

from project import scrapping

def test_Name_zenclass():
    name='title'
    assert scrapping().Name_zenclass(name)=='zenclass' 