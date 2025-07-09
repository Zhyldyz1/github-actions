# app/test_app.py
import pytest
from app.main import ColorToggler

def test_initial_color():
    toggler = ColorToggler()
    assert toggler.current_color == "red"

def test_first_click_to_green():
    toggler = ColorToggler()
    toggler.click()
    assert toggler.current_color == "green"

def test_second_click_to_red():
    toggler = ColorToggler()
    toggler.click() # red -> green
    toggler.click() # green -> red
    assert toggler.current_color == "red"

def test_multiple_clicks():
    toggler = ColorToggler()
    toggler.click() # red -> green
    toggler.click() # green -> red
    toggler.click() # red -> green
    assert toggler.current_color == "green"
    toggler.click() # green -> red
    assert toggler.current_color == "red"
