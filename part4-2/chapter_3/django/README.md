# Introduction

Django 맛집 어드민 프로젝트

## Preparation

가상 환경을 준비

```zsh
python3 -m venv .venv
```

가상 환성 활성화

```zsh
source .venv/bin/activate
```

## MySQL을 설치 (mysqlclient를 쉽게 설치하기 위해 mysql-client, pkg-config 함께 설치)

```zsh
brew install mysql-cient pkg-config
mysql_secure_installation
```

## MySQL에 DB, 사용자 생성

```zsh
mysql -uroot -p비밀번호

```

```sql
CREATE USER 'fcd_user'@'%' IDENTIFIED BY 'password';
CREATE DATABASE `fcd_db`;
GRANT ALL PRIVILEGES ON `fcd_db`.* TO 'fcd_user'@'%';
FLUSH PRIVILEGES;
```

```zsh
echo "DB_HOST=127.0.0.1\nDB_USER=fcd_user\nDB_PASSWORD=password\nDB_NAME=fcd_db" > .env
```

## 패키지 인스톨

```zsh
pip install -r requirements.txt
```

## 서버 실행

준비

```zsh
python manage.py migrate
python manage.py collectstatic
```

서버 실행

```zsh
python manage.py runserver
```
