__author__ = 'bruno'
from addressbook.AddressBookEntry import *

class AddressBook(object):
    """
    This class is intended to hold all necessary information for
    an individual AddressBook that has been read from Storage.
    """
    def __init__(self, addressBookName, fileName):
        """
        Constructor that is populated with information from Storage
        :return:
        """
        self.__addressBookName__ = "addressBookName"
        self.__fileName__ = "fileNameLocation"
        self.__addressBookEntries__ = []

    def getFilename(self):
        """
        Returns the file path
        :return: a string with file path
        """
        return self.__fileName__

    def getAddressBookName(self):
        """
        Returns name of AddressBook instance
        :return: string with name
        """
        return self.__addressBookName__

    def getEntry(self, index):
        """
        :return: an array of all the entries AddressBook holds
        """
        return self.__addressBookEntries__.__getitem__(index)

    def setFilename(self, fileName):
        """
        Setter method
        :param fileName: a String for file path
        :return:
        """
        self.__fileName__ = fileName

    def setAddressBookName(self, addressBookName):
        """
        :param addressBookName: a string for name of AddressBook
        :return:
        """
        self.__addressBookName__ = addressBookName

    def addEntry(self, entry):
        """
        :param entry: An instance of AddressBookEntry that is to be populated
        :return: unknown
        """
        print("addEntry()")

    def editEntry(self,index):
        """
        Takes an AddressBook entry and edits it accordingly
        :param index: the index of entry that needs to be edited
        :return: a copy of the reference of that AddressBookEntry
        """
        print("editEntry()")

    def deleteEntry(self,index):
        """
        This method deletes an entry from the addressBook
        :param index: index of the entry to be deleted
        :return: A boolean with whether deleting was successful or not
        """
        print("deleteEntry()")

    def searchEntry(self,lastName):
        """
        This method searches for an occurrence of the given name
        :param name: a string with lastName to search
        :return: a reference to the searched AddressBookEntry
        """
        print("searchEntry")

    def sortByName(self):
        """
        Uses the name Comparator that is to be used to sort the array
        of AddressBookEntry's
        :return:
        """
        print("sortByName()")

    def sortByZipcode(self):
        """
        Uses the zipcode Comparator that is to be used to sort the array
        of AddressBookEntry's :return: """
        print("sortByZipcode()")

    def toString(self):
        """
        Returns a string with all necessary information
        :return:
        """
        print("toString()")

    def getChange(self):
        """
        Returns a boolean that indicates whether any changes were made
        :return: A boolean, True if a change has been made, False otherwise.
        """
        print("getChange()")

    def importEntries(self, entries):
        """
        This methods appends a array of AddressBookEntries to this instance's
        AddressBookEntry's array
        :param entries: An array containing AddressBookEntrys
        :return:
        """
        print("importEntries")

    def exportEntries(self):
        """
        This method returns a reference to the array of AddressBookEntries
        :return: an array of AddressBookEntries
        """
        print("exportEntries")

    def __lastNameComparator__(self):
        """
        This method is used to compare AddressBookEntries by lastName
        :return: an int, 1 if caller is larger, 0 if the same value and -1 otherwise
        """
        return -1

    def __zipCodeComparator__(self):
        """
        This method is used to compare AddressBookEntries by zipcode
        :return: an int, 1 if caller is larger, 0 if the same value and -1 otherwise
        """
        return -1

