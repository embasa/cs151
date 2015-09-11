__author__ = 'bruno'
from addressbook.AddressBookGUI import *
from addressbook.AddressBookEntry import *

class  AddressBookImportDialogue(AddressBookGUI):
    """
    This class is intended to manage the Import dialogue.
    A user will be able to map columns to fields in this
    class
    """
    def __init__(self):
        """
        Constructor for the AddressBOokImportDialogue
        :return:
        """
        print("ABID constructor")
        super(AddressBookImportDialogue, self).__init__()

    def show(self):
        """
        This method does its own thing then calls parent show
        :return:
        """
        super(AddressBookImportDialogue, self).show()

