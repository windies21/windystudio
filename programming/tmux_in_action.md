
----------

 * TMUX 기본 명령어
http://www.haruair.com/blog/2124

- max pane(toggle) : ctrl + b, z

----------

 * TMUX 한글(utf-8) 깨질때 확인할 것
locale 설정 확인 (첨부 이미지)
-u option (이거 때문에 되는건지? 확실하지 않음)
http://askubuntu.com/questions/410048/utf-8-character-not-showing-properly-in-tmux

----------

 * TMUX 에서 마우스 활성화하기

(~/.tmux.conf 파일을 다음과 같이 작성한다.)

```
# Toggle mouse on with ^B m
bind m \
	set-option -g mouse on \;\
	display 'Mouse: ON'

# Toggle mouse off with ^B M
bind M \
	set-option -g mouse off \;\
	display 'Mouse: OFF'
```

  * 변경한 conf 파일을 적용한다.

$ tmux source-file ~/.tmux.conf
