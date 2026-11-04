# Mailrise 영문 소개 페이지

## 목적과 기준
- 요청: windies21/windystudio GitHub Pages의 https://windystudio.com/mailrise 에 영문 제품 소개 페이지를 새로 작성하고 반영한다.
- 기준: master의 기존 Cayman/Jekyll 사이트. 작업 브랜치 feature/mailrise-page. 기존 페이지·CNAME·배포 설정 유지.
- 제품 근거: 로컬 Mailrise README, 메일 상태 계약, AI 답장 초안 및 자연어 검색 개발 문서와 실제 코드. iPhone/iPad, iOS/iPadOS 26+, Gmail INBOX, Apple Intelligence 가능한 기기/활성화 필요.
- 기능: Today/Upcoming/Important Email, Summary, Pick/Keep/Complete, 원문·첨부, 사용자가 검토·발송하는 AI 답장 초안, 저장된 Inbox 메일 자연어 검색.
- 확인되지 않은 App Store/TestFlight URL, 가격, 출시일, 이용자 수·추천사, 보장된 예약 실행은 넣지 않는다. AI 분석이 기기 내에서 이루어지는 사실과 Gmail 동기화 등 네트워크 사용을 구분한다.
- 예시 리포트는 가상의 예시임을 표시한다. 개인정보·실제 메일을 쓰지 않는다.

## 구현과 완료 기준
- [x] 저장소·배포 대상·제품 근거 확인, 기존 브랜드 이미지 준비.
- [x] Codex: 인수 테스트 작성. 기존 테스트 도구가 없어 Python 표준 unittest/HTMLParser 사용.
- [x] Claude: 독립적인 정적 mailrise/index.html 및 CSS 작성. 모든 방문자 문구 영문, 모바일 대응, 의미 있는 내비게이션, 키보드 접근성, SEO 메타데이터.
- [x] Codex: 내용·링크·자산 인수 검사, 데스크톱/모바일 브라우저 검증.
- [ ] Codex: GitHub Pages master에 반영하고 실제 배포 및 /mailrise 응답 확인.

## 검증 책임과 범위
- Codex 소유: tests/test_mailrise_page.py. Claude는 수정·삭제·기대값 약화 금지.
- 인수: 영문 문서/주요 콘텐츠, 유일한 주 제목, 메타/정규 URL, 내부 링크와 로컬 자산, 이미지 대체 텍스트, 가상 예시 표시, 가짜 다운로드 CTA 부재.
- 정적 페이지이므로 구현을 복제하는 모듈 테스트나 불필요한 JS를 추가하지 않는다. 상호작용 로직이 생기면 Claude가 동작 계약 단위 테스트를 작성한다.
- 브라우저: 반응형 레이아웃과 가독성, 앵커 이동, 키보드 포커스 확인. 실제 앱 기능 테스트는 이번 범위 밖.

## 진행 기록
- 2026-11-04: GitHub Pages는 master / 루트를 사용하는 legacy build, CNAME windystudio.com 확인. 기존 작업 트리 깨끗함. 별도 저장소 사본에서 작업하며 Mailrise 앱의 미커밋 변경은 보존한다.
- 구현 전 인수 실행: `python3 -m unittest discover -s tests -v`는 index.html 미존재로 실패. Python/테스트 환경은 정상이며 미구현 상태를 확인했다.
- 구현: 외부 폰트·라이브러리·JavaScript 없이 정적 HTML/CSS와 실제 앱 브랜드 PNG 2개 사용. 기존 Jekyll 테마가 감싸지 않도록 frontmatter 없는 독립 페이지로 작성.
- 검토 후 보완: 예시 요약이 마지막 리포트 행을 가리던 문제를 일반 문서 흐름과 빈 패딩으로 해결. 답장 초안은 Reply/Reply All 진입 후 생성·검토·Send이며 Forward는 별도임을 교정. 실제 예시와 일치하는 요약으로 수정.
- 로컬 HTTP 200, 인수 검사 7개 통과. 브라우저에서 320/390/561/768/1024/1440px의 문서 너비가 뷰포트와 일치하고 마지막 리포트 행과 요약 사이 35~45px 간격을 확인. 이미지 모두 정상 로드. CTA 앵커, FAQ 마우스 펼침·Enter 닫힘, Tab 포커스 및 Skip to content의 main 이동 확인.
- 실제 iOS Safari/VoiceOver와 앱 자체 동작은 이번 웹페이지 검증 범위 밖. 다음 단계는 master 배포와 실제 URL 확인.
