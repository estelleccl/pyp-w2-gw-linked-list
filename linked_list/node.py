class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        #point to next node
        self.next = next

    def __str__(self):
        if self.next:
            #next exit
            a = self.next
            return str(self.__class__.__name__)+ '('+str(self.elem)+ ') > ' +str(self.next.__class__.__name__)+'('+str(self.next.elem)+')'
        else:
            #next doesnt exist
            return "{}({}) > /".format(self.__class__.__name__, self.elem)
            # return str(self.__class__.__name__)+ '('+str(self.elem)+ ') > /'

    def __eq__(self, other):
        return self.elem == other.elem

    def __repr__(self):
        pass
