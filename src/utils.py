"""사칙연산 유틸.  python src/utils.py 로 스스로 검사한다."""


def subtract(a: int | float, b: int | float) -> int | float:
    """a에서 b를 뺀 값을 반환한다.

    >>> subtract(3, 1)
    2
    >>> subtract(1, 3)
    -2
    """
    return a - b


def add(a: int | float, b: int | float) -> int | float:
    """a와 b를 더한 값을 반환한다.

    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    """
    return a + b


def multiply(a: int | float, b: int | float) -> int | float:
    """a와 b를 곱한 값을 반환한다.

    >>> multiply(2, 3)
    6
    >>> multiply(2, 0)
    0
    """
    return a * b


if __name__ == "__main__":
    # 새 함수를 추가하면 여기에 assert 도 함께 넣는다.
    print("[RUN] utils test suite")
    assert subtract(3, 1) == 2 and subtract(1, 3) == -2
    assert add(1, 2) == 3 and add(-1, 1) == 0
    assert multiply(2, 3) == 6 and multiply(2, 0) == 0
    print("[PASS] all tests passed")
