__author__ = 'bruno'

class AddressBookGUI(object):
    """
    This is the parent class of AddressBookEntryDialogue and
    AddressBookDialogue, it holds methods and variables that
    are shared among the two children classes
    """
    def __init__(self):
        """
        Constructor for GUI
        :return:
        """
        pass

    def show(self):
        """
        This method will be used to create a GUI for addressbook project
        :return:
        """
        print("show")

    def eventListener(self):
        """
        This is a method that will listen for button clicks
        :return:
        """
