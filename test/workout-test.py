import os
import pytest 

from app.workout import WORKOUT

def test_workout():
    assert WORKOUT == "workout"