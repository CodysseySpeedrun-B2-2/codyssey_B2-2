# Conflict Resolution Log

## 충돌 기록 #1 — src/utils.py

### 참여자

- 해결: ashofrondol
- 상대(먼저 병합): codewhite7777

### 상황

- PR-02(subtract)가 먼저 병합되면서 main의 `src/utils.py`가 바뀌었고, 같은 자리(`__main__` 앞과 assert 줄)에 add()를 넣은 내 브랜치가 병합을 멈췄다.

### 충돌 내용

```txt
$ git merge origin/main
Auto-merging src/utils.py
CONFLICT (content): Merge conflict in src/utils.py
Automatic merge failed; fix conflicts and then commit the result.
$ git status --short
UU src/utils.py
$ sed -n /^<<<<<<</,/^>>>>>>>/p src/utils.py
<<<<<<< HEAD
def add(a: int | float, b: int | float) -> int | float:
    """a와 b를 더한 값을 반환한다.

    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    """
    return a + b
=======
def subtract(a: int | float, b: int | float) -> int | float:
    """a에서 b를 뺀 값을 반환한다.

    >>> subtract(3, 1)
    2
    >>> subtract(1, 3)
    -2
    """
    return a - b
>>>>>>> origin/main
<<<<<<< HEAD
    assert add(1, 2) == 3
=======
    assert subtract(3, 1) == 2 and subtract(1, 3) == -2
>>>>>>> origin/main
```

### 해결 과정

- `git merge origin/main`으로 충돌을 받아 마커와 `git status`를 기록했다.
- 둘 다 '함수 추가'라 버릴 이유가 없어 main 쪽 파일을 기준으로 삼고(`git checkout --theirs`) 내 add()와 assert를 다시 넣었다.
- 다시 넣은 뒤 `python src/utils.py`가 `[PASS]`인 것을 보고 커밋했다.

### 결과

- PR-05가 병합됐고 main에는 subtract()와 add()가 모두 있다. 충돌 화면은 `img/conflict-1.svg`로 남겼다.

## 충돌 기록 #2 — docs/CONTRIBUTING.md

### 참여자

- 해결: innurhap28
- 상대(먼저 병합): codewhite7777

### 상황

- PR-06이 먼저 병합되면서 `## 팀 원칙` 아래 두 줄이 커밋 원칙으로 바뀌었고, 같은 자리(원칙 한 줄)를 각자 채운 내 브랜치가 병합을 멈췄다.

### 충돌 내용

```txt
$ git merge origin/main
Auto-merging docs/CONTRIBUTING.md
CONFLICT (content): Merge conflict in docs/CONTRIBUTING.md
Auto-merging docs/troubleshooting-log.md
Automatic merge failed; fix conflicts and then commit the result.
$ git status --short
UU docs/CONTRIBUTING.md
M  docs/troubleshooting-log.md
```

### 해결 과정

- `git merge origin/main`으로 충돌을 받아 `docs/CONTRIBUTING.md`의 마커를 확인했다.
- 둘 다 규칙이라 버릴 이유가 없어 main을 기준으로 삼고(`git checkout --theirs`) 브랜치·커밋·PR/리뷰 원칙 세 줄을 다시 넣었다.
- 같은 TODO 줄을 둘이 동시에 채우지 않도록 앞으로는 절을 나눠 맡는다는 것을 팀 채팅에 남겼다.

### 결과

- PR-07이 병합됐고 `## 팀 원칙`에는 세 줄이 남았다. 충돌 2회(모두 같은 자리)로 요건을 채웠다.
