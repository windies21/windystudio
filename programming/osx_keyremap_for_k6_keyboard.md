키크론 K6 키보드에서 ESC 를 ~ 로 바꾸고 Caps lock 을 ESC 로 바꾸는 방법

```shell
$ hidutil property --set '{"UserKeyMapping":[{"HIDKeyboardModifierMappingSrc":0x700000039,"HIDKeyboardModifierMappingDst":0x700000029},{"HIDKeyboardModifierMappingSrc":0x700000029,"HIDKeyboardModifierMappingDst":0x700000035}]}'
```

hidutil 은 OSX 의 built-in util 입니다.

다른 키들의 hex 값은 https://developer.apple.com/library/archive/technotes/tn2450/_index.html#//apple_ref/doc/uid/DTS40017618-CH1-KEY_TABLE_USAGES 를 참고하시면 됩니다.

