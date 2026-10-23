# Contributing Guide

## 브랜치 전략(GitHub Flow)

- GitHub Flow: `main` 하나와 `feature/<topic>` 브랜치로만 작업하고, PR + 승인 1명 없이는 합치지 않는다
- 이유: ① 4명이 main 하나만 공유해 규칙이 단순하다 ② 병합 전 리뷰·검증을 강제한다 ③ 문제가 생긴 커밋만 따로 되돌릴 수 있다

## 브랜치 네이밍 규칙

- `feature/<topic>` 형식. 주제는 영문 소문자와 하이픈(-)으로 쓴다
- 예: `feature/login`, `feature/sign-in`

## 커밋 메시지 컨벤션

- `<type>: <무엇을 왜>` 형식, `<type>`은 feat/fix/docs/test/chore/refactor
- 금지: update, fix, temp, wip, final 처럼 대상이 보이지 않는 메시지

## PR 규칙

- PR 본문에 What/Why/How와 `Closes #이슈번호`를 넣는다
- 리뷰 1명 승인 뒤 작성자가 병합한다

## 코드 리뷰 규칙

- 'LGTM'만 적지 않는다. 줄을 지정해 질문·대안·위험을 1개 이상 적는다
- 작성자는 코멘트를 커밋이나 답글로 반영하고 스레드를 Resolve한다

## 충돌 대응 흐름

- 충돌을 발견하면 PR 화면을 캡처해 팀 채팅에 올리고, 작성자가 `git merge origin/main`으로 받아 해결한다
- 같은 자리면 main을 기준으로 삼고 내 변경을 다시 넣는다. 한쪽을 버리면 이유를 커밋 메시지에 남긴다
- 해결 뒤 `docs/conflict-resolution.md`의 해당 기록에 명령·출력 원문과 결과를 채운다

## 팀 원칙

- 브랜치는 `feature/<topic>`, 소문자와 하이픈
- 커밋은 `<type>: <무엇을 왜>`, `<type>`은 feat/fix/docs/test
- PR 본문에 What/Why/How, 리뷰는 줄 근거 1개 이상
