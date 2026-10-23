"""사칙연산 유틸.  python src/utils.py 로 스스로 검사한다."""


def add(a: int | float, b: int | float) -> int | float:
    """a와 b를 더한 값을 반환한다.

    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    """
    return a + b


if __name__ == "__main__":
    # 새 함수를 추가하면 여기에 assert 도 함께 넣는다.
    print("[RUN] utils test suite")
    assert add(1, 2) == 3
    print("[PASS] all tests passed")
