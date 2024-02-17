from typing import Self

class ColumnTransformer:
    pass


class Pipeline:

    name = property(lambda self: self._name,
                    lambda self, value: setattr(self, '_name', value) if isinstance(value, str) else None)

    id = 0

    def __init__(self, name: str = None):
        if name is None:
            name = f'pipeline_{Pipeline.id}'
            Pipeline.id += 1
        else:
            if not isinstance(name, str):
                raise TypeError('name must be a string')
            self._name = name

    def create(self) -> Self:
        pass

    def build(self):
        pass
