# Troubleshooting Log

## 시나리오: reset --soft HEAD~1 (로컬 커밋 취소, 변경 유지)

### 참여자

- 실행: ashofrondol

### 상황

- 저장소를 만든 직후 main에 보호 규칙(PR 필수, 승인 1, 우회 금지)을 걸었다. 관리자 계정의 직접 push도 막히는지 확인하려고 템플릿·ignore 파일 커밋을 로컬 main에 만들고 `git push origin main`을 시도했다.

### 시도한 명령/절차

```txt
$ git push origin main
remote: error: GH006: Protected branch update failed for refs/heads/main.        
remote: 
remote: - Changes must be made through a pull request.        
To https://github.com/CodysseySpeedrun-B2-2/codyssey_B2-2.git
 ! [remote rejected] main -> main (protected branch hook declined)
error: failed to push some refs to 'https://github.com/CodysseySpeedrun-B2-2/codyssey_B2-2.git'
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   .github/ISSUE_TEMPLATE/task.md
	new file:   .github/pull_request_template.md
	new file:   .gitignore
```

### 결과

- push는 `GH006: Protected branch update failed`로 거부됐고, 로컬 main에만 push되지 않은 커밋 1개가 남았다(`[ahead 1]`). `git reset --soft HEAD~1`로 커밋만 취소해 템플릿 파일 3개는 스테이징에 그대로 남겼다.

## 시나리오: commit --amend (최근 커밋 메시지 수정)

### 참여자

- 실행: codewhite7777

### 상황

- 커밋 메시지를 `docs: 브랜치 네이밍과 커밋 컨벤션`으로 남겼는데 무엇을 추가했는지(규칙 두 절)가 드러나지 않아, 방금 만든 커밋의 메시지만 고치기로 했다.

### 시도한 명령/절차

```txt
$ git add docs/CONTRIBUTING.md
$ git commit -m "docs: 브랜치 네이밍과 커밋 컨벤션"
[feature/contributing-a 335dd7e] docs: 브랜치 네이밍과 커밋 컨벤션
 1 file changed, 8 insertions(+), 4 deletions(-)
$ git commit --amend -m "docs: 브랜치 네이밍 규칙과 커밋 컨벤션 추가"
[feature/contributing-a 69fbc64] docs: 브랜치 네이밍 규칙과 커밋 컨벤션 추가
 Date: Fri Oct 23 06:34:23 2026 +0000
 1 file changed, 8 insertions(+), 4 deletions(-)
```

### 결과

- `git commit --amend`로 해시는 바뀌었고 파일 내용은 그대로다. 아직 push하지 않은 로컬 커밋이라 공유 이력은 건드리지 않았다.

## 시나리오: stash / stash pop (작업 보관 후 전환)

### 참여자

- 실행: innurhap28

### 상황

- (상황-stash)

### 시도한 명령/절차

```txt
(stash-출력)
```

### 결과

- (결과-stash)

## 시나리오: revert (원격에 push된 커밋 취소)

### 참여자

- 실행: leehnmn

### 상황

- (상황-revert)

### 시도한 명령/절차

```txt
(revert-출력)
```

### 결과

- (결과-revert)
