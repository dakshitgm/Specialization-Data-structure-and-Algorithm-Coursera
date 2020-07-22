# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
thread = namedtuple("tread", ["free_at", "no"])


def heapify(threads, n, i):
    smallest = i
    left_child = i * 2 + 1
    right_child = i * 2 + 2
    if left_child < n and (
        threads[left_child][0] < threads[smallest][0]
        or (
            threads[left_child][0] == threads[smallest][0]
            and threads[left_child][1] < threads[smallest][1]
        )
    ):
        smallest = left_child
    if right_child < n and (
        threads[right_child][0] < threads[smallest][0]
        or (
            threads[right_child][0] == threads[smallest][0]
            and threads[right_child][1] < threads[smallest][1]
        )
    ):
        smallest = right_child

    if smallest != i:
        threads[i], threads[smallest] = threads[smallest], threads[i]
        heapify(threads, n, smallest)


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    threads = [[0, i] for i in range(n_workers)]
    for job in jobs:
        result.append(AssignedJob(threads[0][1], threads[0][0]))
        threads[0][0] += job
        heapify(threads, n_workers, 0)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
