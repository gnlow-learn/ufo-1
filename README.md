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
### ufo -> otf
```sh
py build.py yourfontname
```