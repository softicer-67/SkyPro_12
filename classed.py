from abc import ABC, abstractmethod


class Storage(ABC):

    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, item: dict, count: int):
        if item in self._items:
            self._items[item] += count
        else:
            self._items[item] = count
        self._capacity -= count

    @abstractmethod
    def remove(self, item: str, count: int):
        self._items[item] -= count
        if self._items[item] == 0:
            self._items.pop(item)
        self._capacity += count

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def get_items(self):
        return self._items

    @property
    def get_unique_items_count(self):
        return len(self._items)


class Store(Storage):
    def add(self, item: str, count: int):
        if self.get_free_space >= count:
            super().add(item, count)
            return True
        return False

    def remove(self, item: str, count: int):
        if item in self.get_items and self.get_items[item] >= count:
            super().remove(item, count)
            return True
        return False


class Shop(Store):
    def add(self, item: str, count: int):
        if self.get_free_space >= count:
            super().add(item, count)
            return True
        return False

    def remove(self, item: str, count: int):
        if item in self.get_items and self.get_items[item] >= count:
            super().remove(item, count)
            return True
        return False


class Request:
    def __init__(self, to, amount, product, take_from=None):
        self.take_from = take_from
        self.to = to
        self.amount = amount
        self.product = product

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.take_from} в {self.to}."
