# Python
```
git init - .git 생성
git config user.name "realJun9u"
git config user.email "wnsq0317@naver.com"
git add . - staging area 로 올림
git commit -m "first commit" - 리포지터리로 커밋
git log - 커밋 히스토리
git diff {커밋앞자리4} {커밋앞자리4}
git reset --option {commit_id} --hard는 repository, staging area, working directory 모두 바꾸고 --mixed는 Workind Directory는 바뀌지 않고, --soft는 Staging Area 또한 바뀌지 않는다. 세 가지 모두 HEAD가 해당 commit을 가리킨다.
git status - 커밋 상태
git reflog - HEAD 이동 정보

git remote add origin {주소} - 주소의 프로젝트를 원격저장소로 사용하는데, 이름은 origin으로.
git push -u origin master - 내용 푸시
git push -u origin +master - [rejected] master -> master (fetch first) error: failed to push some refs to 발생하면 강제 푸시
```