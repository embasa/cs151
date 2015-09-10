__author__ = 'bruno'

class Storage(object):
    """
    This classes only purpose is to read and write AddressBook
    references to storage
    """

    def __init__(self):
        """
        I am unsure whether this needs a constructor
        so I need to figure that out
        :return:
        """
        pass

    def isFull(self):
        """
        A boolean to see if storage is full
        :return: returns True if full, false otherwise
        """
        print("isfull")
        return True

    def available(self):
        """
        This method is in notes, no idea why. Maybe accident
        :return:
        """
        print("available")

    def writeToDisk(self, addressBook, path):
        """
        This method is used to save AddressBook's name and Entries at the given path
        :param addressBook: Instance of type AddressBook
        :param path: string containing path
        :return:
        """
        print("writeToDisk")

    def readFromDisk(self, addressBook, path):
        """
        This method is intended to populate the reference passed as parameter
        and return a copy of the reference possibly
        that is populated using information given in path
        :param addressBook: a reference to an AddressBook object
        :param path: a string containing path of addressbook data
        :return: AddressBook reference passed as parameter
        """
        print("readFromDisk")

