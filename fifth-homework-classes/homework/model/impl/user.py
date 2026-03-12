from model.entity import Entity


class User(Entity):
    def add(self, name: str, email: str) -> None:
        values = [name, email]
        super().add(values)
