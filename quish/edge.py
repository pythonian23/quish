from quish.node import Node


class Edge:
    node1: Node
    node2: Node
    k: float
    damp: float

    def __init__(self, node1=None, node2=None, k=1, damp=0, rest=-1):
        self.node1 = Node() if node1 is None else node1
        self.node2 = Node() if node2 is None else node2

        self.k = k
        self.damp = damp
        self.rest = self.length if rest == -1 else rest

    def __repr__(self):
        return f"{self.node1}E{self.node2}"

    def __eq__(self, other):
        return self.node1 == other.node1 and self.node2 == other.node2

    def __iter__(self):
        yield self.node1
        yield self.node2

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.node1
        elif index == 1:
            return self.node2
        else:
            raise IndexError

    def __setitem__(self, index, value):
        if index == 0:
            self.node1 = value
        elif index == 1:
            self.node2 = value
        else:
            raise IndexError

    @property
    def length(self):
        return self.node1.distance(self.node2)

    def update(self):
        delta = self.node1 - self.node2
        delta = delta - delta.norm * self.rest

        self.node1.apply_force(-delta * self.k)
        self.node2.apply_force(delta * self.k)

        self.node1.apply_force(
            -(self.node1.vel - self.node2.vel)
            * 2
            * ((self.node1.mass * self.k) ** 0.5)
            * self.damp
        )
        self.node2.apply_force(
            -(self.node2.vel - self.node1.vel)
            * 2
            * ((self.node2.mass * self.k) ** 0.5)
            * self.damp
        )
