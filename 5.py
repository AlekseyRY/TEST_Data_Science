'''
Реализуйте двусвязный список используя синтаксис языка Python. Вам необходимо создать класс 
(либо несколько классов), который (которые) будет (будут) представлять структуру данных 
- связный список.
Связный список — это набор элементов данных, называемых узлами. В односвязном списке каждый 
узел содержит значение и ссылку на следующий узел. В двусвязном списке каждый узел также 
содержит ссылку на предыдущий узел.
1. Реализуйте узел для хранения значения и указателей на следующий и предыдущий узлы.
2. Затем реализуйте список, который содержит ссылки на первый и последний узел и предлагает 
интерфейс, подобный массиву, для добавления и удаления элементов, какие методы должны быть 
реализованы:
● push() - записывает значение в конец списка
● pop() - удаляет значение с конца списка
● shift() - удаляет значение в начале списка
● unshift() - записывает значение в начало списка
'''

class Node:
    def __init__(self, data): 
        self.item = data 
        self.nref = None 
        self.pref = None


class DoublyLinkedList: 
    def __init__(self): 
        self.start_node = None


    def insert_in_emptylist(self, data): #adding to the NEW D_List
        if self.start_node is None: 
            new_node = Node(data) 
            self.start_node = new_node 
        else: 
            print("List is not empty")


    def unshift(self, data): #adding to the beginning of the D_List
        if self.start_node is None: 
            new_node = Node(data) 
            self.start_node = new_node 
            print("Node inserted") 
            return 
        new_node = Node(data) 
        new_node.nref = self.start_node 
        self.start_node.pref = new_node 
        self.start_node = new_node


    def push(self, data):  #adding to the end of the D_List
        if self.start_node is None: 
            new_node = Node(data) 
            self.start_node = new_node 
            return 
        n = self.start_node 
        while n.nref is not None: 
            n = n.nref 
            new_node = Node(data) 
            n.nref = new_node 
            new_node.pref = n


    def shift(self): #removing element from the beginning of the D_List
        if self.start_node is None: 
            print("The list is empty") 
            return 
        if self.start_node.nref is None:
            self.start_node = None 
            return 
        self.start_node = self.start_node.nref 
        self.start_prev = None;


    def pop(self): #removing element from the end of the D_List
        if self.start_node is None:
            print("The list is empty") 
            return 
        if self.start_node.nref is None:
            self.start_node = None 
            return 
        n = self.start_node
        while n.nref is not None:
            n = n.nref 
            n.pref.nref = None
