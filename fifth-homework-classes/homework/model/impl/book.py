from model.entity import Entity


class Book(Entity):
    def add(self, title: str, author: str, year: int) -> None:
        values = [title, author, year]
        super().add(values)
