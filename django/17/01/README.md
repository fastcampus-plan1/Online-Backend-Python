# Introduction

Django Admin 샘플 코드
: Permission Admin

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

마이그레이션

```zsh
python manage.py migrate
```

슈퍼유저 권한 관리자 추가

```zsh
python manage.py createsuperuser
```

## Runserver

```zsh
python manage.py runserver
```
