# 가상 환경 삭제
if (Test-Path -Path ".venv") {
    Remove-Item -Recurse -Force ".venv"
}

# 데이터베이스 파일 삭제
if (Test-Path -Path "db.sqlite3") {
    Remove-Item -Force "db.sqlite3"
}

# 가상 환경 생성
py -m venv .venv

# 가상 환경 활성화
& .\.venv\Scripts\Activate.ps1

# 필요한 패키지 설치
pip install -r requirements.txt

# 데이터베이스 마이그레이션
python manage.py migrate

# 환경 변수 설정
$env:DJANGO_SUPERUSER_USERNAME="admin"
$env:DJANGO_SUPERUSER_EMAIL="admin@example.com"
$env:DJANGO_SUPERUSER_PASSWORD="password"

# 슈퍼유저 생성
python manage.py createsuperuser --noinput
