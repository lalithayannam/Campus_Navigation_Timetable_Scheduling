from __future__ import annotations

import asyncio
import concurrent.futures
import time
from multiprocessing import Pool
from threading import Thread
from queue import Queue


async def fetch_building_status(name: str) -> dict[str, str]:
    await asyncio.sleep(0.01)
    return {"building": name, "status": "available"}


async def fetch_all_statuses(names: list[str]) -> list[dict[str, str]]:
    return await asyncio.gather(*(fetch_building_status(name) for name in names))


def cpu_square(value: int) -> int:
    return value * value


def multiprocessing_demo(values: list[int]) -> list[int]:
    with Pool(processes=min(4, max(1, len(values)))) as pool:
        return pool.map(cpu_square, values)


def threading_demo(names: list[str]) -> list[str]:
    results: list[str] = []
    lock = __import__("threading").Lock()

    def worker(name: str) -> None:
        time.sleep(0.005)
        with lock:
            results.append(name)

    threads = [Thread(target=worker, args=(name,)) for name in names]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return results


def producer_consumer(items: list[str]) -> list[str]:
    queue: Queue[str | None] = Queue()
    output: list[str] = []

    def producer() -> None:
        for item in items:
            queue.put(item)
        queue.put(None)

    def consumer() -> None:
        while True:
            item = queue.get()
            if item is None:
                queue.task_done()
                break
            output.append(item.upper())
            queue.task_done()

    producer_thread = Thread(target=producer)
    consumer_thread = Thread(target=consumer)
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()
    return output


def future_demo(values: list[int]) -> list[int]:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(cpu_square, value) for value in values]
        return [future.result() for future in futures]


async def async_status_stream(names: list[str]):
    for name in names:
        yield await fetch_building_status(name)
