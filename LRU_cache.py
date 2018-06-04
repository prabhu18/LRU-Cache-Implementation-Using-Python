'''

Question :

Design and build a "Least Recently used cache "  which evicts the least
recently used item . The cahce should map from keys to values (allowing you to
insert and retrieve a value associated with a particular key) and be initialized with
a max size. when it is full ,it should evict the least recently used item ,
Keys are integers and value are strings.

*Given :Cache size >=0


Logic :

Implement four methods,

1) insertIntocache( key , value ) :

Insert if there is space in the cache keep updating firstnode,
If not space remove least recently used and then insert.

2) retrieveValuefromCache(key) :

If no such key, print no such element,
else print the value and update the node
into front of cache because it is now recent used node.

3)findLeastrecentlyused()

Return least recent used element and print and put it in front
because it is now recent used node.

4)updateTheCache(key,value):

if no such key , print error
else update the key and put it in front because it is now recent used node.

'''


#Implementation

class LRUcache():

    def __init__(self,size):
        self.cache_size=0
        self.max_size=size
        self.hash={}
        self.firstNode=None
        self.lastNode=None

    class Node():

        def __init__(self):
            self.key=None
            self.value=None
            self.next=None
            self.prev=None

    def insertIntocache(self,key,value):

        if self.firstNode is None:
            self.firstNode=self.Node()
            self.firstNode.key=key
            self.firstNode.value=value
            self.hash[key]=self.firstNode
            self.lastNode=self.firstNode
            self.cache_size=self.cache_size+1

        else:

            if self.cache_size==self.max_size:
                del self.hash[self.lastNode.key]
                self.removeFromList(self.lastNode)
                self.insertIntocache(key,value)
            else:
                newNode=self.Node()
                newNode.key=key
                newNode.value=value
                self.hash[key]=newNode
                self.firstNode.prev=newNode
                newNode.next=self.firstNode
                self.firstNode=newNode
                self.cache_size +=1


    def retrieveValuefromCache(self,key):

        try:
            node=self.hash[key]
            if node != self.firstNode:
                self.removeFromList(node)
                self.insertIntocache(node.key,node.value)
        except:
            print " No such item found in cache."

    def removeFromList(self,node):

        self.cache_size -= 1

        if node.prev is not None:
            node.prev.next=node.next
        if node.next is not None:
            node.next.prev=node.prev
        if node == self.firstNode:
            self.firstNode=node.next
        if node == self.lastNode:
            self.lastNode=node.prev


    def findLeastrecentlyused(self):
        if self.lastNode is None:
            return None
        else:
            print self.lastNode.value
            node=self.lastNode
            self.removeFromList(self.lastNode)
            self.insertIntocache(node.key,node.value)


    def updateTheCache(self,key,value):
        try:
            node=self.hash[key]
            node.value=value
            self.removeFromList(node)
            self.insertIntocache(node.key,node.value)
        except:
            print "No such intem to update"


    def printList(self):
        node=self.firstNode
        while(node is not None):
            print node.key,node.value
            node=node.next


C=LRUcache(input("Give cache size.")) #for this example I am taking 3
C.insertIntocache(1,"prabhat") #insert prabhat , list now : prabhat
C.insertIntocache(2,"pravin")  #insert pravin,   list now : pravin->prabhat
C.insertIntocache(3,"pradeep") #insert pradeep,  list now : pradeep->pravin->prabhat
C.insertIntocache(4,"Prakash") #remove prabhat, insert prakash list now: prakash->pradeep->pravin
C.printList() #print only
C.updateTheCache(2,"pravin_new") #update pravin, list now : pravin_new->prakash->pradeep
C.findLeastrecentlyused()    # return pradeep, list now : pradeep->pravin_new->prakash
C.printList() #print only
C.retrieveValuefromCache(2)#return pravin_new, list now : pravin_new->pradeep->prakash
C.printList() #print only
