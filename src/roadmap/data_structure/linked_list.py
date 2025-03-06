from typing import Generator, List, Optional


class LinkedListNode:
    def __init__(self, data: int = 0, next: Optional["LinkedListNode"] = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"LinkedListNode(data={self.data}, next={str(self.next)})"


class LinkedList:
    def __init__(self, nodes: List[LinkedListNode] = None) -> None:
        self.head = None
        if nodes is not None:
            node = LinkedListNode(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = LinkedListNode(data=elem)
                node = node.next

    def add_first(self, new_node) -> None:
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_node_data) -> None:
        if self.head is None:
            self.head = new_node_data
            return
        for current_node in self:
            pass
        current_node.next = new_node_data

    def add_after(self, target_node_data, new_node) -> None:
        if self.head is None:
            raise Exception("List Empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s'not found", target_node_data)

    def add_before(self, target_node_data, new_node) -> None:
        if self.head is None:
            raise Exception("List Empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = prev_node.next

        raise Exception("Node with data '%s' not found", target_node_data)

    def remove_node(self, target_node_data) -> None:
        if self.head is None:
            raise Exception("List Empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = prev_node.next

        raise Exception("Node with data '%s' not found", target_node_data)

    def __repr__(self) -> str:
        return " -> ".join(str(node.data) for node in self) + " -> None"

    def __iter__(self) -> Generator[LinkedListNode]:
        curr = self.head
        while curr:
            yield curr
            curr = curr.next


ll = LinkedList(["h", "e", "l", "l", "o"])
ll.add_first(LinkedListNode("¡"))
ll.add_last(LinkedListNode("!"))
print(ll)
