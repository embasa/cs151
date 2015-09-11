__author__ = 'bruno'
from addressbook.AddressBookGUI import *

class AddressBookDialogue(AddressBookGUI):
    """
    This class is meant to manage the window with the name and
    list with the given AddressBook instance
    """
    def __init__(self):
        """
        Not familiar with what needs to be in this Constructor
        :return:
        """
        print("ADB constructor")
        super(AddressBookDialogue, self).__init__()

    def show(self):
        """
        Does its own thing then calls parent
        :return:
        """
        super(AddressBookDialogue, self).show()

