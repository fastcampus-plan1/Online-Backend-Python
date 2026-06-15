# 뷰 + 템플릿 실습 완성본

## Preparation

가상 환경을 준비

```bash
python -m venv .venv
```

MySQL을 설치

```bash
brew install mysql mysql-client pkg-config
mysql_secure_installation
```

MySQL에 DB, 사용자 생성

```bash
mysql -u root -p

```

```sql
CREATE USER 'your_username'@'%' IDENTIFIED BY 'your_password';
CREATE DATABASE your_database;
GRANT ALL PRIVILEGES ON your_database.* TO 'your_username'@'%';
FLUSH PRIVILEGES;
```

```bash
echo "DB_HOST=127.0.0.1\nDB_USER=your_username\nDB_PASSWORD=your_password\nDB_NAME=your_database" > .env
```

## Installation

```bash
pip install -r requirements.txt
```

## Runserver

서버 실행

```bash
python manage.py runserver
```

slik를 사용하는 경우

```bash
python manage.py collectstatic
```

## Pages
Admin - http://localhost:8000/admin
링크 페이지 - http://localhost:8000/
레스토링 페이지 - http://localhost:8000/restaurant/1
