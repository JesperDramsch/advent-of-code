# Test Working solutions to Build a nice Day Class
import sys
sys.path.insert(0, '.')
from util import Day

def test_reset():
    day = Day(1,1)
    day.load()
    
    test = day.data[0]

    day.data[0] = None

    assert day.data[0] == None

    day.reset()
    assert day.data[0] == test