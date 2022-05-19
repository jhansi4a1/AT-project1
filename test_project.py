##pytest##
##import class from project1##

from project1 import Jhansi
##pytest for url##
def test_project():
    url="https://www.zenclass.in/"
    assert Jhansi().project(url)=="https://www.zenclass.in/"

