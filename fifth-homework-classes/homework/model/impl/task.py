from model.entity import Entity


class Task(Entity):
    def add(self, title: str, description: str, completed: bool) -> None:
        values = [title, description, completed]
        super().add(values)
