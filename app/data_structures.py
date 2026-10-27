from __future__ import annotations

from dataclasses import dataclass, field
import heapq
from typing import Generic, Iterable, Iterator, TypeVar

T = TypeVar("T")


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_word = False


class Trie:
    """Prefix-search structure for campus building names."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word.lower():
            node = node.children.setdefault(char, TrieNode())
        node.is_word = True

    def search_prefix(self, prefix: str) -> list[str]:
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        result: list[str] = []

        def collect(current: TrieNode, path: str) -> None:
            if current.is_word:
                result.append(path)
            for char, child in current.children.items():
                collect(child, path + char)

        collect(node, prefix.lower())
        return result


class MinHeap(Generic[T]):
    def __init__(self, values: Iterable[T] = ()) -> None:
        self._heap: list[T] = list(values)
        heapq.heapify(self._heap)

    def push(self, value: T) -> None:
        heapq.heappush(self._heap, value)

    def pop(self) -> T:
        return heapq.heappop(self._heap)

    def __len__(self) -> int:
        return len(self._heap)


class UnionFind:
    def __init__(self, items: Iterable[str]) -> None:
        self.parent = {item: item for item in items}
        self.rank = {item: 0 for item in self.parent}

    def find(self, item: str) -> str:
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, a: str, b: str) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


class SegmentTree:
    """Range-sum segment tree."""

    def __init__(self, values: list[int]) -> None:
        self.n = len(values)
        self.tree = [0] * (2 * max(1, self.n))
        for i, value in enumerate(values):
            self.tree[self.n + i] = value
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def range_sum(self, left: int, right: int) -> int:
        if not (0 <= left <= right <= self.n):
            raise ValueError("Invalid range")
        left += self.n
        right += self.n
        total = 0
        while left < right:
            if left & 1:
                total += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                total += self.tree[right]
            left //= 2
            right //= 2
        return total


@dataclass
class QueueItem(Generic[T]):
    priority: int
    value: T

    def __lt__(self, other: QueueItem[T]) -> bool:
        return self.priority < other.priority


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._items: list[QueueItem[T]] = []

    def push(self, value: T, priority: int) -> None:
        heapq.heappush(self._items, QueueItem(priority, value))

    def pop(self) -> T:
        return heapq.heappop(self._items).value

    def __len__(self) -> int:
        return len(self._items)


class CampusDataContext:
    """Context manager demonstrating safe resource-style handling."""

    def __enter__(self) -> CampusDataContext:
        return self

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        return None
