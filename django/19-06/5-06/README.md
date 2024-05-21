# Introduction

Lint & Formatters

## Preparation

가상 환경 설정 (Windows)

```cmd
py -m venv .venv
```

가상 환경 설정 (macos)

```zsh
python3 -m venv .venv
```

가상환경 활성화 (Windows)

```cmd
.venv\Scripts\activate
```

가상환경 활성화 (macOS)

```zsh
source .venv/bin/activate
```

패키지 설치

```zsh
pip install -r requirements.txt
```

# 실행
```zsh
black black_sample.py
isort isort_sample.py
flake8 black_sample.py isort_sample.py
```

# pre-commit 셋업

꼭 별도의 폴더에 zip 파일을 압축풀어서 실행해주세요

```zsh
git init .
pre-commmit install

git add .
git commit -m "Initial commit"
```