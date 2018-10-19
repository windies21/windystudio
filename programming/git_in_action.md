 * git init
https://git-scm.com/book/ko/v1/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-Git-%EC%A0%80%EC%9E%A5%EC%86%8C-%EB%A7%8C%EB%93%A4%EA%B8%B0

 1. 최초 설정
https://git-scm.com/book/ko/v1/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EC%B5%9C%EC%B4%88-%EC%84%A4%EC%A0%95

 1. git branch & merge
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

 1. Git Reset to origin
http://www.ocpsoft.org/tutorials/git/reset-and-sync-local-respository-with-remote-branch/

 1. Git rebase Conflict 해결시
Conflict 코드 수정 후 Git add . 

 1. Change remote git branch tracking
 ```
 git branch develop --set-upstream-to origin/develop
 ```
 
 1. Git Flow in Terminal
 ```
 brew install git-flow
 https://github.com/nvie/gitflow/wiki/Command-Line-Arguments
 ```

 1. 이미 remote repository 에 push 해버린 commit들 하나로 합치기
  https://json.postype.com/post/209499


 1. 삭제된 리모트 branch tracking 중단하기
 ```
 git fetch --prune && git branch -r | awk '{print $1}' | egrep -v -f /dev/fd/0 <(git branch -vv | grep origin) | awk '{print $1}' | xargs git branch -d
 ```
 
 1. 삭제된 리모트 branch 로컬에서 지우기
 ```
 삭제될 remote branch 미리보기 : `git remote prune origin --dry-run`
 삭제된 remote branch local 에서 삭제 : `git remote prune origin`
 remote 가 삭제된 local branch 삭제 : `git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -d`
 ```
 
 1. 원격 저장소 url 변경하기
 http://minsone.github.io/git/github-managing-remotes-changing-a-remotes-url
 
 1. git hub pull request
 http://dogfeet.github.io/articles/2012/how-to-github.html

 1. git stash
 https://blog.outsider.ne.kr/788

 1. revert pushed merge
 ```
 git revert -m 1 [merge commit]
 ```
 
 1. branch 를 특정 commit 으로 되돌리기
 ```
 git reset --hard [commit]
 git push --force origin develop
 ```
 
 1. git fork update
 http://minsone.github.io/git/GitHub-Syncing-a-fork
 
 1. git diff color 설정하기
 https://git-scm.com/book/ko/v1/Git%EB%A7%9E%EC%B6%A4-Git-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0
 
 * 참고
 https://www.gitkraken.com/
