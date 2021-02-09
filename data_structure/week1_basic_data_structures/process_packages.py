# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = [0] * size
        self.front = self.rear = -1

    def process(self, request):
        # write your code here
        while self.front != -1 and self.finish_time[self.front] <= request.arrived_at:
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size

        if not (self.rear + 1) % self.size == self.front:
            if self.front == -1:
                started_at = request.arrived_at
                self.front = self.rear = 0
            else:
                started_at = self.finish_time[self.rear]
                self.rear = (self.rear + 1) % self.size
            self.finish_time[self.rear] = started_at + request.time_to_process
            return Response(False, started_at)

        return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
