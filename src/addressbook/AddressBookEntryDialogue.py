__author__ = 'bruno'
from addressbook.AddressBookGUI import *
from addressbook.AddressBookEntry import *

class AddressBookEntryDialogue(AddressBookGUI):
    """
    This class is intended to manage the dialogue box
    for adding/editing AddressBookEntry's
    """
    def __init__(self):
        """
        Constructor for AddressBookDialogue
        :return:
        """
        print("ABED constructor")
        super(AddressBookEntryDialogue, self).__init__()

    def show(self):
        """
        Does it's own thing and then calls parent show()
        :return:
        """
        super(AddressBookEntryDialogue, self).show()
