# 팀 계산 유틸 (B2-2)

Codyssey "친구 3~5명과 함께 프로그램 만드는 법 연습하기" 미션을 4인 팀으로 수행하는 저장소다.
사칙연산 함수 4개를 팀이 나눠 만들고, 모든 변경을 PR로만 넣는다.

## 브랜치 전략: GitHub Flow

- `main`은 항상 `python3 src/utils.py`가 `[PASS] all tests passed`인 상태로 둔다.
- 모든 작업은 `feature/<기능요약>` 브랜치에서 하고, PR + 승인 1명을 거쳐 `main`에 병합한다.
- `develop`·`release`·`hotfix` 브랜치는 두지 않는다(작은 팀에서 규칙이 단순해야 실수가 적다).

## 구성

- `src/utils.py`: 사칙연산 함수 모음(`python3 src/utils.py`로 자체 검사)
- `docs/CONTRIBUTING.md`: 브랜치·커밋·PR·리뷰·충돌 대응 규칙
- `docs/conflict-resolution.md`: 충돌 해결 기록
- `docs/troubleshooting-log.md`: amend / reset --soft / revert / stash 실습 기록
- `SUBMISSION.md`: 팀원별 Issue/PR·기여 커밋 색인
- `img/`: 화면 대신 남긴 증빙 그림(`git log --graph`, 보호 규칙, 충돌 마커)

## 사용 예시

```bash
python3 src/utils.py
```

```
[RUN] utils test suite
[PASS] all tests passed
```

```bash
python3 -c "from src.utils import add, divide; print(add(1, 2), divide(5, 2))"
```

```
3 2.5
```
