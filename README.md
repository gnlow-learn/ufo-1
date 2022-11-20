# learn-ufo-1
## 개발 환경
- Python 3
- FontForge 20220308
- [Font Preview (VSCode 확장기능)](https://github.com/ctcuff/vscode-font-preview)

## 준비
### ufo 생성
FontForge -> `Generate Fonts` -> `United Font Object(UFO3)`
### Dependency 설치
```sh
py -m pip install defcon ufo2ft
```

### `fontinfo.plist` 수정
`<array>` 태그로 감싸진 부분을 삭제

### `features.fea` 수정
```fea
lookup Test {
  markClass [B] <anchor 0 0> @HAIR;
  pos base [A] <anchor 0 0> mark @HAIR;
} Test;

feature asdf {
  lookup Test;
} asdf;
```
원하는 기능 추가
- https://opentypecookbook.com/common-techniques/
- https://adobe-type-tools.github.io/afdko/OpenTypeFeatureFileSpecification.html
- https://help.fontlab.com/fontlab/7/manual/OpenType-Features/

### ufo -> otf
```sh
py build.py yourfontname
```