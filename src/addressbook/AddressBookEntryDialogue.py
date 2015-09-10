__author__ = 'bruno'
from addressbook import AddressBookGUI
from addressbook.AddressBookEntry import *

class AddressBookEntryDialogue( AddressBookGUI ):
    """
    This class is intended to manage the dialogue box
    for adding/editing AddressBookEntry's
    """
    def __init__(self):
        """
        Constructor for AddressBookDialogue
        :return:
        """
        pass

    def makeAddressBookEntry(self):
        """
        This method is needed to return an AddressBook instance that is populated with
        typed fields
        :return:
        """
        entry = AddressBookEntry()
        return entry

