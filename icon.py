# -*- coding: utf-8 -*-

import base64
from io import BytesIO

content = """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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAECAwQFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQQDAgF0BwgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAcGCQgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICRMAAB4TJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkEx4AAAceAAApKiEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISopAAAeDwAABBs/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/Pz8/Pz8qPz8/Pz9AQHMjIBtAPz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/P0NvCQQHJk5qcHFyPz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/IG0yAAAAAAAAAAAAOG5EPz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/Pz8/Pz8/aWoAAAAAAAAAAAAAAAAAa2w/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz8/Pz8/LBMAAAAAAAAAAAAAAAAAAAAoaD8/Pz8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/Pz8/aBMAAAAAAAAAAAAAAAAAAAAAAEoCPz8/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/Pz8/ZmQAAAAAAAAAAAAAAAAAAAAAAAAAZz8/Pz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz8/P2UAAAAAAAAAAAAAAAAAAAAAAAAAAABiPz8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/P0FjAAAAAAAAAAAAAAAAAAAAAAAAAAAAZEA/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/Pz9iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtPz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz9ACwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVz8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/G2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGEbPz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/PxdfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgGz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz8/HgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOBs/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/F00AAAAAAAAAAAAAAAAAAAAAAAAAAAAAACkbPz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/PxtaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABHGz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz9AXQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXj8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/P1sAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFw/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/Pz9QWQAAAAAAAAAAAAAAAAAAAAAAAAAAAFpAPz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz8/P1cAAAAAAAAAAAAAAAAAAAAAAAAAAABYPz8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/Pz9QDQAAAAAAAAAAAAAAAAAAAAAAAABWPz8/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/Pz8/P1QiAAAAAAAAAAAAAAAAAAAAAAAyVT8/Pz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz8/Pz8/OyIAAAAAAAAAAAAAAAAAAABTVD8/Pz8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/Pz8/Pz9ROAAAAAAAAAAAAAAAAAArUj8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/Pz8/Pz8/PyNMTQAAAAAAAAAAAE5PUD8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/QEVGR0hJDyJKSzkjPz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/P0BBI0JDREA/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AAAQbPz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/GwQAAA8PAAAEGz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/PxsEAAAPDwAABBs/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8bBAAADw8AACkbPz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/Pz8/GykAAA8PAAA8PT4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj08AAAPDwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADw8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgPCAAAAAAIDwgAAAAACA8ICAAAAA8PAAAAAAAAAAAAAAAAAAAAAAAA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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQIDBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEAwIBawYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZrDQAIBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHCAANCwA8ag8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw9qPAALCAA5Ojs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs6PAAICAA5Ojs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAECAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIBBBtGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGGwQOJkRFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUQmDg4mEycnJycnJycnJycnJycnJycnJycnJycnJycnEyYODiYTJycnJycnJycnJycnJycnJycnJycnJycnJycTJg4OJhMnJycnJycnJycnJycnJycnJycnJycnJycnJxMmDg4mEycnJycnJycnJycZQgZDLicnJycnJycnJycnEyYODiYTJycnJycnJyc+PyYAAAAOQEEnJycnJycnJycTJg4OJhMnJycnJycnKzwAAAAAAAAAAz0nJycnJycnJxMmDg4mEycnJycnJyc6AAAAAAAAAAAAOzMnJycnJycnEyYODiYTJycnJycnNzgAAAAAAAAAAAAAOScnJycnJycTJg4OJhMnJycnJyccAAAAAAAAAAAAAAAYJycnJycnJxMmDg4mEycnJycnJzYAAAAAAAAAAAAAAAUTJycnJycnEyYODiYTJycnJycnNgAAAAAAAAAAAAAABRMnJycnJycTJg4OJhMnJycnJycpAAAAAAAAAAAAAAA1JycnJycnJxMmDg4mEycnJycnJyAjAAAAAAAAAAAAADQnJycnJycnEyYODiYTJycnJycnJzEAAAAAAAAAAAAyMycnJycnJycTJg4OJhMnJycnJycnKy8AAAAAAAAALDAnJycnJycnJxMmDg4mEycnJycnJycnKxQsAAAADi0uJycnJycnJycnEyYODiYTJycnJycnJycnJx0hKCkqJycnJycnJycnJycTJg4OJhMnJycnJycnJycnJycnJycnJycnJycnJycnJxMmDg4mEycnJycnJycnJycnJycnJycnJycnJycnJycnEyYODiYTJycnJycnJycnJycnJycnJycnJycnJycnJycTJg4OIyQlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSQjDg4AAAAAAAAAAAAAAAAAAAAAAAAAACIAAAAOAAAOGwAODgAAAAAAAAAAAAAAAAAAAAAAAAAYGRobHB0eHyAhDg4OAAAAAAAAAAAAAAAAAAAAAAAAAA8QERITEBQVEBYXDgQAAAAAAAAAAAAAAAAAAAAAAAAABQYHAAgJCgsMDQAEAQIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAgEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEnJycnJycnJycnJycnJygQEREREREREREREREREREQEBESEhISEhISEhISEhIREBAREhISIiMkJSYSEhISERAQERISEiAAAAAAIRISEhEQEBESEh4AAAAAAB8SEhIREBAREhIdAAAAAAAYEhISERAQERISGhsAAAAAHBISEhEQEBESEhIXGAAAGQ0SEhIREBAREhISEhMUFRYSEhISERAQERISEhISEhISEhISEhEQDg8PDw8PDw8PDw8PDw8PDggAAAAAAAAAAAAJCgsMDQ4BAgICAgICAgICAwQFBgcBAAAAAAAAAAAAAAAAAAAAAP//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//AAA="""

def get_fp():
    return BytesIO(base64.b64decode(content.encode("utf8")))

def save(file_name):
    with open(file_name, "wb") as fp:
        fp.write(base64.b64decode(content.encode("utf8")))