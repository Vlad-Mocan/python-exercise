from database.db import init_db, add_record, search_record, view_records, delete_record


class Entity:
    filename: str
    headers: list[str]

    def __init__(self, filename: str, headers: list[str]):
        self.filename = filename
        self.headers = headers

    def get_filename(self) -> str:
        return self.filename

    def initialize_db(self) -> None:
        init_db(self.filename, self.headers)

    def add(self, values: list) -> None:
        record = {}
        index = 0

        for col in self.headers:
            if col == "id":
                continue
            record[col] = values[index]
            index += 1

        add_record(self.filename, record)

    def get(self, field: str, value: str):
        return search_record(self.filename, field, value)

    def list_all(self) -> None:
        view_records(self.filename)

    def delete(self, field: str, value: str) -> None:
        delete_record(self.filename, field, value)
