# python3
max_hashes = 1


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(" ".join(map(str, output)))


def hashOf(str):
    ans = 0
    for c in reversed(str):
        ans = (ans * 263 + ord(c)) % 1000000007
    return ans % max_hashes


def get_occurrences(pattern, text):
    max_hashes = len(text)
    occurances = []
    n = len(pattern)
    patternHash = hashOf(pattern)
    for i in range(len(text) - n + 1):
        cur = text[i : i + n]
        if patternHash == hashOf(cur):
            if pattern == cur:
                occurances.append(i)
    return occurances


if __name__ == "__main__":
    print_occurrences(get_occurrences(*read_input()))

