__author__ = 'bruno'
from addressbook.AddressBook import *

class Storage(object):
    """
    This classes purpose is to read and write AddressBook
    references to storage. We don't need to instantiate this class.
    We also need added functionality of reading and writing in CSV
    format
    """

    @staticmethod
    def writeToDisk(addressBook, path):
        """
        This method is used to save AddressBook's name and Entries at the given path
        :param addressBook: instance of type AddressBook
        :param path: string containing path
        :return:
        """
        print("writeToDisk")

    @staticmethod
    def readFromDisk(path):
        """
        This method is intended to populate the reference passed as parameter
        and return a copy of the reference possibly
        that is populated using information given in path
        :param path: a string containing path of addressbook data
        :return: AddressBook reference passed as parameter
        """
        print("readFromDisk")

    @staticmethod
    def writeToDiskCSV(addressBookEntries, filepath):
        """
        This method is used to write an AddressBook in CSV format to disk
        :param addressBookEntries: an array of AddressBookEntries
        :param filepath: a string containing the filepath
        :return:
        """
        print("writeToDiskCSV")

    @staticmethod
    def readFromDiskCSV(mapping, filepath):
        """
        This method gets a mapping of columns to fields and the file path
        so it can save the
        :param : an AddressBook instance
        :param mapping: a map of columns to fields
        :param filepath: filepath of CSV file
        :return: return an array of AddressBookEntries
        """
        print("readFromDiskCSV")
        return []

