__author__ = 'bruno'

class AddressBookEntry(object):
    """
    This class defines a single entry with all the appropriate fields
    and has all getters/setters.
    """
    def __init__(self, firstName, lastName, zipcode, address, city, state, phoneNumber):
        print("constructor!")
        self.__firstName__ = firstName
        self.__lastName__ = lastName
        self.__zipcode__ = zipcode
        self.__address__ = address
        self.__city__ = city
        self.__state__ = state
        self.__phoneNumber__ = phoneNumber

    def getFirstName(self):
        """
        :return: a string copy of the firstName
        """
        return self.__firstName__

    def getLastName(self):
        """
        :return: a string copy of the lastName
        """
        return self.__lastName__

    def getZipcode(self):
        """
        :return: an integer of the zipcode
        """
        return self.__zipcode__

    def getAddress(self):
        """
        :return: a string of the address
        """
        return self.__address__

    def getCity(self):
        """
        :return: a string of the city
        """
        return self.__city__

    def getState(self):
        """
        :return: a string of the state
        """
        return self.__state__

    def getPhoneNumber(self):
        """
        :return: an integer of the phone number
        """
        return self.__phoneNumber__

    def setFirstName(self, firstName):
        """
        :param firstName: a string with new first name
        :return:
        """
        self.__firstName__ = firstName

    def setLastName(self, lastName):
        """
        :param lastName: a string with new last name
        :return:
        """
        self.__lastName__ = lastName

    def setZipcode(self, zipcode):
        """
        :param zipcode: integer corresponding to new zipcode
        :return:
        """
        self.__zipcode__ = zipcode

    def setAddress(self, address):
        """
        :param address: a string containing new address
        :return:
        """
        self.__address__ = address

    def setCity(self, city):
        """
        :param city: a string containing new city
        :return:
        """
        self.__city__ = city

    def setState(self, state):
        """
        :param state: a string containing new state
        :return:
        """
        self.__state__ = state

    def setPhoneNumber(self, phoneNumber):
        """
        :param phoneNumber: an integer containing new phone number
        :return:
        """
        self.__phoneNumber__ = phoneNumber

    def toString(self):
        """
        A method use to used to return a string literal
        :return: a string containing all member attributes
        """
        print("toString()")
        return ""
