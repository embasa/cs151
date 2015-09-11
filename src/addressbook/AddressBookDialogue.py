__author__ = 'bruno'
from addressbook.AddressBookGUI import *
from addressbook.AddressBook import *

class AddressBookDialogue(AddressBookGUI):
    """
    This class is meant to manage the window with the name and
    list with the given AddressBook instance
    """
    def __init__(self, addressBook):
        """
        Not familiar with what needs to be in this Constructor
        :param addressBook: an instance , addressBookof an AddressBook manipulate
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

