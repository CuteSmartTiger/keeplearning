# 先定一个node类，创建节点实例，单链表中一个节点包含两个属性有：数据域与指针域
class Node():
    def __init__(self, value=None, next=None):
        self.value = value  # 数据域存储数值
        # print( self.value)
        self.next = next  # 指针域储存下一节点的位置


# 实现Linked List及其各类操作方法
# 链表的属性：
# 头部指针，永远指向第一个节点，尾部指针，永远指向最后一个节点
# 节点，存储数值同时指出一下个节点，最后一个节点的指针域为空
# 单链表的操作：增加  删除
class LinkedList():
    def __init__(self):  # 初始化链表为空表
        self.head = Node()  # 创建有头结点的单链表
        self.tail = None
        self.length = 0

    # 检测链表是否为空，即头部head指针指向的对象值是否为空
    def is_empty(self):
        return self.head.next == None

    # pre_add在链表前端添加元素:O(1)
    def pre_add(self, value):
        new_node = Node(value)  # create一个node节点
        # print(new_node.value)
        # 为了保证链不断开，先将头部指针域存储下一个节点位置的信息赋值于新添加的节点
        new_node.next = self.head.next
        # 然后将头部指针指向新节点
        self.head.next = new_node
        self.length += 1
        # print(new_node.value)

    # 在链表尾部添加元素:O(n)
    def end_add(self, value):
        new_node = Node(value)
        if self.is_empty():
            # print('原表为空')
            self.head.next = new_node  # 若为空表，将添加的元素设为第一个元素
        else:
            # 移动的游标，代表节点
            current = self.head
            while current.next:
                # print(current.value)
                # print(current.next)
                current = current.next  # 遍历链表,寻找指针为空的节点
            # print("=-=-=-=-=")
            # print(current.value)
            current.next = new_node  # 此时current为链表最后的元素
            # print(new_node.value)
            # print('end_add')
        self.length += 1

    # search检索元素是否在链表中
    def search(self, value):
        current = self.head.next
        found_value = False
        while current and current.value and not found_value:
            if current.value == value:
                found_value = True
                return found_value
            else:
                current = current.next
        return found_value

    # index索引,元素在链表中的位置
    def index(self, value):
        current = self.head.next
        count = 0
        found = False
        while current and not found:
            count += 1
            if current.value == value:
                found = True
            else:
                current = current.next
        if found:
            return count
        else:
            raise ValueError('%s is not in linkedlist' % value)

    # remove删除链表中的某项元素
    def remove(self, value):
        current = self.head.next
        pre = None  # 查找目标节点的前一个节点
        while current:
            if current.value == value:
                if not pre:  # 若查找到的当前节点是首节点，此时的前驱节点不存在
                    self.head.next = current.next
                else:
                    pre.next = current.next  # 若查找到的当前节点不是首节点，则将当前节点的next指向值赋予当前节点之前节点的next
                self.length -= 1
                return " remove {0} success".format(value)
            pre = current
            current = current.next
            # print(current)
        raise ValueError('{0} is not in linkedlist'.format(value))

    # insert链表中插入元素
    def insert(self, pos, value):
        assert pos > 0, "pos must > 0"
        # if pos == 1:
        #     self.pre_add(value)
        if pos > self.length:
            self.end_add(value)
        else:
            new_node = Node(value)
            count = 0
            pre = current = self.head
            while count < pos:
                pre = current
                current = current.next
                count += 1
            # 注意赋值顺序
            new_node.next = current
            pre.next = new_node
            self.length += 1


op = LinkedList()
# print(op.is_empty())
# print(op.head)
# node5 = Node(6)
# print(node5.value)
# node4 = Node(5)
# node3 = Node(4)
# node2 = Node(3)
# node1 = Node(2)

print(op.is_empty())
op.pre_add(2)
print(op.is_empty())
op.pre_add(3)
print(op.length)
op.end_add(4)
print(op.search(4))
print(op.search(6))
print(op.index(4))
# print(op.index(6))
# op.pre_add(4)
# op.pre_add(5)
# op.pre_add(6)
# print(op.search(6))
print(op.remove(4))
# print(op.remove(6))
print(op.search(4))
# print(op.search(6))
# print(op.length)
print(op.insert(1, 7))
# print(op.insert(1, 7))
print(op.search(7))
print(op.index(7))
print(op.insert(9, 9))
print(op.search(9))
print(op.index(9))


# print(op.end_add(9))
# print(op.search(9))
# # print(op.remove(6))
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pass

    def partition(self, start, end):
        # 以第一个非头结点的节点为基准
        pivot = start.next.val
        curr = start.next
        prev = start.next
        while curr != end.next:
            if curr.val > pivot:
                pass
            elif curr.val < pivot:

                pass
            else:
                curr = curr.next

    def qiuck_sort(self, start, end):
        """
        :param start: the head pointer
        :param end: the end pointer
        :return:
        """
        if start.next != end:  # 若相等则代表只剩余一个元素，是递归出口的条件
            # 与基准比较后，prev指向基准左边排序后最后一个插入的节点
            # post则指向基准右侧下一个递归需要排序的起始节点，指向比基准大的第一个节点
            prev, post = self.partition(start, end)
            self.qiuck_sort(start, prev)
            self.qiuck_sort(post, end)
