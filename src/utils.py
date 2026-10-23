"""사칙연산 유틸.  python src/utils.py 로 스스로 검사한다."""


def subtract(a: int | float, b: int | float) -> int | float:
    """a에서 b를 뺀 값을 반환한다.

    >>> subtract(3, 1)
    2
    """
    return a - b


if __name__ == "__main__":
    # 새 함수를 추가하면 여기에 assert 도 함께 넣는다.
    print("[RUN] utils test suite")
    assert subtract(3, 1) == 2
    print("[PASS] all tests passed")
