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
- [x] Codex: GitHub Pages master에 반영하고 실제 배포 및 /mailrise 응답 확인.

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
- 실제 iOS Safari/VoiceOver와 앱 자체 동작은 이번 웹페이지 검증 범위 밖.
- 공개 배포 완료: 제품 커밋 `0b5e71e4ca4ad675263435dbe867a51c0839ed42`를 master에 반영. GitHub Pages build 상태 `built`, 오류 없음. `https://windystudio.com/mailrise`에서 `/mailrise/`로 이동 후 HTTP 200이며, 배포 HTML의 SHA-256이 로컬 최종본과 일치함을 확인.
- CSS와 브랜드 PNG 2개도 공개 URL에서 성공적으로 내려받아 SHA-256이 로컬 파일과 각각 일치함을 확인했다.
- 남은 필수 작업 없음. 추후 실제 App Store/TestFlight 링크가 확정되면 다운로드 CTA를 연결할 수 있다.

## 2026-11-05 메인 링크와 브랜드 표기
- 요청: 메인 페이지에 Mailrise 소개 링크 추가. 소개 페이지의 `Windy Studio`를 소문자 고유 브랜드명 `windystudio™`로 통일하고 TM 사용법 검토.
- 최신 origin/master와 작업 브랜치 일치, 미커밋 변경 없음 확인.
- 범위: README.md에 Mailrise 링크와 짧은 설명, mailrise/index.html의 본문·버튼·푸터·Open Graph 브랜드 표기 4곳 수정. CSS·기능·URL은 유지.
- 단순 문구 및 Markdown 문서 변경이므로 직접 수정 예외 적용. 새 테스트를 추가하지 않고 기존 7개 인수 검사, 실제 diff, 배포된 메인의 링크 이동과 소개 페이지 표기 확인.
- TM 검토 근거: [USPTO](https://www.uspto.gov/trademarks/basics/what-trademark), [INTA](https://www.inta.org/fact-sheets/trademark-symbols/). TM은 브랜드를 상표로 사용한다는 표시이며 등록 사실·독점권을 보장하지 않는다. 등록 여부를 확인하지 않았으므로 등록상표 기호 ®는 사용하지 않는다. 국가별 권리와 선행상표 충돌 여부 조사는 이번 검토에 포함하지 않는다.
- [x] 링크·브랜드 문구 수정과 기존 인수 검사. 7개 검사와 `git diff --check` 통과. 기존 페이지 테스트·CSS 변경 없음.
- [x] master 반영 및 공개 페이지 확인. 제품 커밋 `e20217365e5d37c29117d6c7c3607392f3f61e62`의 Pages `built` 확인. 공개 메인의 Mailrise 링크 클릭으로 소개 페이지 이동, 새로고침 후 본문·버튼·푸터의 windystudio™ 표시 확인. 공개 HTML에서 메인 링크와 브랜드 4곳을 검사하고 로컬 최종 HTML과 일치 확인. 남은 필수 작업 없음.

## 2026-11-05 메인 브랜드와 섹션 순서 후속 수정
- 요청: 메인의 windystudio 표기를 windystudio™로 통일하고 Mailrise 소개 영역을 Boardgame 아래로 이동.
- README.md의 기존 Mailrise 제목·설명을 그대로 마지막 섹션으로 이동. `_config.yml`의 title과 테마 푸터에 쓰이는 github.repository_name 표시값 설정. 실제 저장소명·링크·도메인은 유지한다. 공용 Cayman 테마를 사용하는 페이지의 사이트 브랜드도 같은 표기를 따른다.
- Cayman 기본 레이아웃의 헤더/푸터 변수와 jekyll/github-metadata의 사용자 설정 병합 동작을 공식 소스에서 확인했다. 템플릿 복제나 스크립트 없이 설정·문서의 단순 수정으로 처리한다.
- [x] 로컬 변경·문서 순서 및 설정 검증. Ruby YAML 파싱과 title/푸터 표시값, Python으로 Mailrise 링크 단일 존재·Boardgame 이후 순서 확인, `git diff --check` 통과.
- [x] GitHub Pages 반영 후 실제 메인 제목·푸터·링크 순서 확인. 제품 커밋 `c98d278a0c514d90a9181b3b7001c8b2d9863c1e` 빌드 `built`. 공개 HTML과 브라우저 새로고침으로 제목·헤더·푸터 `windystudio™`, 마지막 두 섹션 Boardgame → Mailrise 및 기존 링크 목적지 유지 확인. 남은 작업 없음.

## 2026-11-05 로고 기반 메인 리디자인
- 요청: 첨부 windystudio.png를 사용해 메인 디자인 개편. 주색 #6699ff, 로고의 연한 파랑 보조색, 기존 녹색 포인트. Mailrise와 일관된 품질을 가지되 다른 테마로 구분.
- 상단은 자유롭게 재구성하고 View on GitHub 제거. windystudio™를 온디바이스 AI 기반의 다양한 애플리케이션을 연구·개발하는 개발그룹으로 소개한다.
- 기존 winDy/21st Century Radio Band/programming/Boardgame/Mailrise의 이름·소개 문구·링크는 모두 보존하고 이전보다 작은 본문과 제목으로 표시. Mailrise는 Boardgame 다음 순서를 유지하되 별도 강조 박스를 사용.
- 구현: 독립 정적 루트 index.html + assets/home.css. 첨부 원본은 assets/images/windystudio.png에 수정 없이 복사. 기존 README는 콘텐츠 기준으로 보존하며 Mailrise 페이지와 기타 하위 페이지·기존 Jekyll 설정은 변경하지 않는다.
- Codex 인수: tests/test_home_page.py. 기존 문구 보존, 링크 목적지·순서, 의미 있는 문서/브랜드 소개, 원본 로고, GitHub CTA 제거, 메타/자산 경로 확인. Claude 수정 금지. 정적 콘텐츠이므로 불필요한 JS·모듈 테스트는 만들지 않는다.
- 브라우저: 데스크톱/모바일 가독성과 레이아웃, 색상/위계, 링크 이동. #6699ff 위에는 짙은 글자로 대비 확보. 기본 본문 14~16px 수준, 메뉴 제목 약 18~24px, Mailrise는 별도 강조. 외부 라이브러리·폰트 없이 구현.
- [x] 최신 master와 깨끗한 작업 트리 확인, 첨부 로고 준비.
- [x] Codex 인수 검사 작성·미구현 실패 확인. 새 홈 검사 6개를 작성했고 index.html 미존재로 초기 실패 확인. 첨부 원본과 복사 로고의 SHA-256 일치.
- [x] Claude 디자인 구현, Codex 내용/브라우저 검증 및 필요한 보완. index.html과 assets/home.css 구현, 기존 Mailrise/README/설정 변경 없음. CLI 정상 종료 및 권한 거절 없음.
- 검증: 인수 검사 총 13개 통과(홈 6 + 기존 Mailrise 7), `git diff --check` 통과. 320/390/640/768/960/961/1024/1440px에서 문서 폭=뷰포트 폭, 이미지 정상 로드, 로고 패널과 텍스트 32~64px 여유 확인. 계산된 주색 rgb(102,153,255), 본문 15px, 메뉴 제목 18~22px 확인.
- 브라우저: Tab 포커스와 본문 건너뛰기, 상단 Mailrise 앵커 및 Explore Mailrise → 기존 소개 페이지 이동 확인. 320px 영문 표제의 과도한 분리를 CSS 몇 줄로 직접 보완 후 재확인. 기존 programming/boardgame/LIVE 공개 URL HTTP 200 확인. 실제 iOS Safari/VoiceOver는 별도 확인하지 않음.
- [x] GitHub Pages 배포·공개 결과 확인. 제품 커밋 `bb792bd76a4aa6a8674906e330b3c0fbdf5d6534`의 Pages `built`, 오류 없음. 공개 루트가 새로운 독립 index.html을 제공함을 확인했고 HTML·CSS·로고 파일이 로컬 최종본과 바이트 단위로 일치한다. 공개 브라우저에서도 새 소개·기존 콘텐츠·Mailrise 카드 확인. 남은 필수 작업 없음.

## 2026-11-05 오픈소스 블로그 테마 적용
- 사용자 피드백: 번호·비대칭 그리드·큰 제품 카드가 AI 템플릿처럼 보임. 공개 오픈소스 블로그 프레임워크를 찾아 실제 활용하도록 요청.
- 비교: Jekyll + Minima(간결한 단일 본문/기본 블로그 테마), Jekyll + Minimal Mistakes(다양한 포트폴리오/사이드바 구성), Hugo(별도 빌드 파이프라인 필요). 기존 GitHub Pages/Jekyll과 단순 읽기 중심 구성에 맞는 Minima v2.5.1 선택. 공식 GitHub Pages 버전 목록에도 동일 버전 포함.
- 출처: https://github.com/jekyll/minima/tree/v2.5.1 , commit 38a84a949f9753c4542e25f422935f59b4913053, MIT. 원본 Sass와 home 레이아웃을 실제 사용하고 라이선스/출처 기록 보존. 다른 하위 페이지를 바꾸지 않도록 메인 전용 이름으로 포함하며 기존 Cayman 설정은 유지.
- 메인을 Jekyll의 Minima home/default 레이아웃 체인과 Sass 빌드로 전환. 번호·점·카드·화살표 장식 제거, 단일 세로 본문과 자연스러운 목록/제목/링크로 정리. 상단도 블로그 지면에 맞게 로고와 개발그룹 소개를 간결하게 구성. #6699ff/녹색은 절제된 브랜드 요소에 유지.
- 기존 이름·설명·링크·순서, windystudio™ 표기, 첨부 원본 로고, Mailrise 페이지 유지. Mailrise는 Boardgame 다음에 작은 아이콘/제목/일반 링크로 구분. 임의 글·날짜·통계 생성 없음.
- Codex 인수 검사는 Jekyll 빌드 출력에 같은 기존 문구·링크 계약을 적용하도록 입력 경로만 확장. 테마 원본 출처와 빌드 통합도 확인. 프레임워크 변경으로 HTML 소스가 완성 문서가 아니므로 소스 대신 렌더 결과를 검사한다.
- [x] 공식 소스·라이선스 준비, 인수 기준 및 Jekyll 로컬 빌드 준비. 원본 Sass 4개 파일은 지정 커밋과 바이트 단위 일치. Gemfile/lock과 로컬 플러그인 설정 추가.
- [x] Claude Minima 기반 구현 및 기존 장식 제거. 실제 home/default 레이아웃 체인과 원본 Sass import 적용. 커스텀 스타일은 101줄로 정리하고 기존 697줄 CSS 제거. 불필요한 JS 없음.
- [x] Codex 실제 Jekyll 빌드·인수·반응형·링크 검증. Jekyll 3.10 빌드 성공, 인수 검사 14개와 diff 공백 검사 통과. 320/390/600/768/1024/1280px에서 가로 넘침 없음, 이미지 정상, 본문 15px/섹션 제목 22px 확인. Tab 포커스·본문 건너뛰기·Explore Mailrise 이동 확인. 실제 iOS Safari/VoiceOver는 미검증.
- [x] master 게시·공개 빌드 및 화면 확인. 후속 요청 작업 시작 시 f40e25f Pages built 및 공개 HTML의 Minima 레이아웃/테마 표기 확인, 사용자가 제공한 실제 화면과 일치.

- 빌드 준비 중 로컬 GitHub metadata 플러그인 누락을 보완했고, 네트워크 제한 때문에 발생한 공개 저장소 메타데이터 조회 실패는 승인된 네트워크 빌드로 해소했다. 구현 중간 상태의 include 미생성 실패 이후 완성본 빌드와 인수 검사가 정상 통과했다. 기존 Mailrise 파일·하위 페이지 소스·공용 Cayman 설정은 변경하지 않았다.

- 게시 상태: 제품 커밋 `f40e25f0869912a510a56fecb5c38e7f1707a3d0`를 master에 push 완료. GitHub Actions run `41862974882`의 build 작업은 5분 이상 `queued`, `runner_name: null`, 실행 단계 없음 상태. Pages API는 `building`, 오류 메시지 없음. 공개 메인은 아직 이전 버전이므로 공개 배포 확인 항목은 미완료로 유지한다.
- 재개 지점: https://github.com/windies21/windystudio/actions/runs/41862974882 완료 확인 → 공개 메인 HTML/CSS의 Minima 적용과 브라우저 화면 확인 → 게시 항목 완료 처리. 반복 push나 재실행으로 기존 배포 대기를 취소하지 않는다. 검증한 로컬 화면은 별도 스크린샷으로 제공.

## 2026-11-05 영문 소개와 Mailrise 강조 후속 수정
- 이전 Minima 커밋 f40e25f의 Pages 상태가 built로 전환된 것을 확인. 이번 요청은 상단 소개·푸터 영문화, Mailrise 영역을 winDy 위로 이동, 간결한 박스로 강조하고 아이콘과 제목에도 /mailrise/ 링크 추가. 이전 Boardgame 다음 순서 요구는 이번 요청으로 대체한다.
- 확정 문구: “windystudio™ is a development group researching and building a range of applications powered by on-device AI.” 푸터는 “On-device AI application research and development” 및 “Built with Jekyll and the Minima theme.” 사용. 기존 winDy·밴드 등 소개 문구는 보존.
- 범위: index.html, assets/home.scss, _includes/minima/footer.html. Minima와 작은 글꼴 유지, 연한 파랑 배경·파란 테두리의 단정한 박스. 아이콘+제목을 하나의 의미 있는 링크로 묶어 키보드 접근 지원.
- Codex: 기존 순서 인수 기준을 새 요청으로 변경하고 영문 소개/푸터, 아이콘·제목 링크 계약 추가. Claude: 제품 파일 3개만 변경. 원본 Sass·기존 하위 페이지·인수 검사 변경 금지.
- [x] 인수 검사 갱신 및 초기 실패 확인. 새 동작에 해당하는 영문화·순서·제목/아이콘 링크 3개 검사 실패, 기존 6개 검사 통과.
- [x] Claude 구현, Jekyll 빌드·인수 검사 및 화면/링크 확인. 두 차례 위임 정상 종료·권한 거절 없음. Jekyll 빌드 성공, 인수 검사 총 16개와 diff 공백 검사 통과. 320/390/768/1280px 가로 넘침 없음, 파란 테두리/연한 배경과 Mailrise→winDy 순서 확인. 아이콘 클릭 및 제목 링크 Enter로 /mailrise/ 이동 확인. 본문 h1은 1px/clip으로 화면에서 숨기고 접근성 트리에 유지. 실제 VoiceOver 검증은 하지 않음.
- [ ] master 게시와 실제 공개 페이지 반영 확인.
- 추가 요청: 헤더와 중복되는 로고 위 본문 windystudio 제목 제거. 접근성용 h1은 화면에서 숨기고 헤더 브랜드·로고는 유지한다. _layouts/minima-home.html과 기존 home.scss의 최소 변경으로 처리하고 브라우저에서 제목이 시각적으로 사라졌는지 확인한다.
- 공개 검증 보완: e40a2a9 Pages built 및 공개 HTML 일치 확인. 서버 CSS는 Minima 압축 출력으로 새 규칙을 포함하지만 기존 브라우저가 이전 CSS를 재사용해 박스/제목 숨김이 적용되지 않는 현상 확인. head 스타일 URL에 Jekyll 빌드 시간 쿼리를 붙이는 한 줄 수정으로 갱신 보장. 단순 수정 예외 적용 후 다시 빌드·검증·게시한다.
