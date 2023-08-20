#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from console import HBNBCommand


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_create_without_attributes(self):
        new_instance = HBNBCommand()
        new_instance.onecmd("create State")

    def test_create_with_attributes(self):
        new_instance = HBNBCommand()
        new_instance.onecmd("create State name=\"California\"")

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
