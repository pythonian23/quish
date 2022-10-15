import uuid

from quish.vector import Vector


class Node(Vector):
    uuid: uuid.UUID

    mass: float
    net_force: Vector
    vel: Vector

    def __init__(self, *args, **kwargs):
        self.uuid = kwargs.pop("uuid", uuid.uuid4())

        self.mass = kwargs.pop("mass", 1)
        self.net_force = Vector()
        self.vel = Vector()

        super().__init__(*args, **kwargs)

    def apply_force(self, force):
        self.net_force += self.__class__(force)

    def update(self, dt: float):
        self.vel += self.net_force * dt / self.mass
        self.x += self.vel.x * dt
        self.y += self.vel.y * dt

        self.net_force.x = 0
        self.net_force.y = 0

    def __eq__(self, other):
        return self.uuid == other.uuid

    def __ne__(self, other):
        return not self.uuid == other.uuid

    def __repr__(self):
        return f"Node({self.x}, {self.y})"
