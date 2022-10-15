import typing
import uuid

from .vector import Vector
from .node import Node
from .edge import Edge


class Object:
    edges: typing.List[Edge]
    nodes: typing.Dict[uuid.UUID, Node]

    def __init__(self):
        self.edges = []
        self.nodes = {}

    def get_nodes(self):
        for edge in self.edges:
            self.nodes[edge.node1.uuid] = edge.node1
            self.nodes[edge.node2.uuid] = edge.node2

    def update(self, dt: float):
        for e in self.edges:
            e.update()
        for n in self.nodes.values():
            n.update(dt)

    @property
    def center_of_mass(self):
        mass = 0
        center = Vector()
        for node in self.nodes.values():
            mass += node.mass
            center += node * node.mass
        return center / mass
