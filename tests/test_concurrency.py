import asyncio

from app.concurrency.tasks import (
    future_demo,
    multiprocessing_demo,
    producer_consumer,
    threading_demo,
    fetch_all_statuses,
)


def test_threading() -> None:
    assert set(threading_demo(["a", "b"])) == {"a", "b"}


def test_processes() -> None:
    assert multiprocessing_demo([1, 2, 3]) == [1, 4, 9]


def test_futures() -> None:
    assert future_demo([2, 3]) == [4, 9]


def test_producer_consumer() -> None:
    assert producer_consumer(["a", "b"]) == ["A", "B"]


def test_async() -> None:
    result = asyncio.run(fetch_all_statuses(["Library", "Lab"]))
    assert len(result) == 2
