from .interface import AbstractLinkedList


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.elements = elements

    def __str__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        return self.elements == other.elements

    def __ne__(self, other):
        return self.elements != other.elements

    def append(self, elem):
        pass

    def count(self):
        pass

    def pop(self, index=None):
        pass
