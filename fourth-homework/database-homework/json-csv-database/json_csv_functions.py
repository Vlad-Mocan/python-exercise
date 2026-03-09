from os import path

from json_functions import (
    init_json_db,
    add_json_record,
    view_json_records,
    search_json_record,
    delete_json_record,
)

from csv_functions import (
    init_csv_db,
    add_csv_record,
    view_csv_records,
    search_csv_record,
    delete_csv_record,
)


def get_extension(filename):
    return path.splitext(filename)[1].lower()


def init_db(filename, headers):
    ext = get_extension(filename)
    if ext == ".json":
        init_json_db(filename, headers)
    elif ext == ".csv":
        init_csv_db(filename, headers)
    else:
        print("Unsupported file format.")
        return
    print(f"Database initialized: {filename}")


def add_record(filename, record):
    ext = get_extension(filename)
    if ext == ".json":
        add_json_record(filename, record)
    elif ext == ".csv":
        add_csv_record(filename, record)


def view_records(filename):
    ext = get_extension(filename)
    if ext == ".json":
        view_json_records(filename)
    elif ext == ".csv":
        view_csv_records(filename)


def search_record(filename, field, value):
    ext = get_extension(filename)
    if ext == ".json":
        search_json_record(filename, field, value)
    elif ext == ".csv":
        search_csv_record(filename, field, value)


def delete_record(filename, field, value):
    ext = get_extension(filename)
    if ext == ".json":
        delete_json_record(filename, field, value)
    elif ext == ".csv":
        delete_csv_record(filename, field, value)
