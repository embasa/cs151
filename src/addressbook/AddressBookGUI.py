or__ = 'bruno'

class AddressBookGUI(object):
    """
    This is the parent class of AddressBookImportDialogue, AddressBookEntryDialogue and
    AddressBookDialogue, it holds methods and variables that
    are shared among the two children classes
    """

    def __init__(self):
        """
        Does things, and then shows itself
        :return:
        """
        print("constructor")

    def show(self, typeOfObject):
        """
        This method will be used to create a GUI for addressbook project
        sets the size of window. This method, based on the type of instance
        passed behaves differently.
        :param : an instance of one of the types needed.
        :return:
        """
        print("show")

