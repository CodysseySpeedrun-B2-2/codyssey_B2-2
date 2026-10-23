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

- (상황-amend)

### 시도한 명령/절차

```txt
(amend-출력)
```

### 결과

- (결과-amend)

## 시나리오: stash / stash pop (작업 보관 후 전환)

### 참여자

- 실행: innurhap28

### 상황

- 리뷰 규칙 문장을 고치던 중 main의 최신 상태를 확인해야 해서, 커밋하지 않은 변경을 잠시 치워 두고 브랜치를 오갔다.

### 시도한 명령/절차

```txt
$ git stash push -u -m "리뷰 규칙 문장 다듬기"
Saved working directory and index state On feature/contributing-b: 리뷰 규칙 문장 다듬기
$ git stash pop
On branch feature/contributing-b
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   docs/CONTRIBUTING.md

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (9653168cab70a50287b740f3ad100c0e0af7b18f)
```

### 결과

- `git stash pop`으로 변경이 그대로 돌아왔고(`git status --short`에 수정 파일) 충돌 없이 이어서 작업했다.

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
