#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Self defined class"""


import os
import pickle

class PickleCache(object):
    """Custom class to make changes in pickle file. """

    def __init__(self, file_path='datastore.pkl', autosync = False):
        """Class Constructor

        Args:
            file_path (string, optional): Defaults to datastore.pkl
            autosync (bool, optional):Defaults to False

        Attr:
            __file_path: Pseudo-private attribute,assigned the constructor
            variable file_path value
            __data: Pseudo-private, instantiated as an empty dictionary object
            autosync

        Example:
            >>> pcache  = PickleCache()
            >>> print pcache ._PickleCache__file_path
            datastore.pkl
            >>> print pcache ._PickleCache__file_object
            None
            >>> print pcache ._PickleCache__data
            {}
        """
        self.__file_path = file_path    # Pseudo-private attributes
        self.__data = {}                # empty dic for data, T2
        self.autosync = autosync        # non private
        self.__file_object = None
        self.load()                    # task # 5

    # SET ITEM
    def __setitem__(self, key, value):
        """ Public method that allows key value pairs to be stored within
            the class

        Args:
            key (required):input for key
            value (required): inpur given for key value

        Returns:
            mixed: data stored for keys and values in a dictionary

        Example:
            >>> pcache  = PickleCache()
            >>> pcache ['test'] = 'hello'
            >>> print pcache ._PickleCache__data['test']
            'hello'
        """

        self.__data[key] = value    #passing data for key

        if self.autosync is True:
            self.flush()

    # Get Lenght
    def __len__(self):
        """ Method to check length of self.__data

         Args:
            None

        Returns:
         int: Checks length of data and returns.

        Example:
            >>> len(pcache )
            1
        """

        return len(self.__data)

    # Get Item
    def __getitem__(self, key):
        """Exception haandling method for   data is not found

        Args:
            key(required):  key to return the requested value from
            self.__data dict.

        Example:
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
            >>> print pcache['key2']
            Traceback (most recent call last):
            File "/home/vagrant/Desktop/is210-week-13-synthesizing/picklecache.
            py", line 191, in <module> print pcache ['key2']
            File "/home/vagrant/Desktop/is210-week-13-synthesizing/picklecache
            .py", line 105, in __getitem__
            raise error KeyError: 'key2'
        """

        # if key in data return
        try:
            if self.__data[key]:
                return self.__data[key]

        # else return two types of errors
        except (TypeError, KeyError) as error:
            raise error

        if self.autosync is True: # flush data
            self.flush()


    # Delete Item
    def __delitem__(self, key):
        """Method to delete key value from dictionary using key attribute and
            del statement to remove any entry fromthe __data attribute with the
            same key.

        Args:
            key (required):

        Example:
        >>> pcache['test'] = 'hello'
        >>> print 'Length Before Delete ', len(pcache)
        Length Before Delete 1
        >>> del pcache['test']
        >>> print 'Length After Delete ', len(pcache)
        Length After Delete 0
        """
        del self.__data[key]    # deleting data from key access

    # LOAD
    def load(self):
        """Method to access the data

        Args:
            None

        Returns:
            Returns the data stoerd in in self.__data

        Example:
            >>> fh = open('datastore.pkl', 'w')
            >>> pickle.dump({'foo': 'bar'}, fh)
            >>> fh.close()
            >>> pcache = PickleCache('datastore.pkl')
            >>> print pcache['foo']
            'bar'
        """

        if os.path.exists(self.__file_path):
            if os.path.getsize (self.__file_path) > 0:
                fh = open(self.__file_path, 'r')
                self.__data = pickle.load(fh)
            fh.close()


    # Flush-Dump
    def flush(self):
        """Method for class needs to be able to save its stored data to file
        when commanded

        Args:
            None

        Returns:
            Data written to file

        Example:
        pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhandler = open(pcache._PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}
        """

        fhandler = open(self.__file_path, 'w') # file open in write mode
        pickle.dump(self.__data, fhandler)
        fhandler.close()
