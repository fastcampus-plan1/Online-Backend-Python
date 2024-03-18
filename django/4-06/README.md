# Introduction

Django Elastic Beanstalk 배포 #2

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

AWS CLI 설치
https://aws.amazon.com/ko/cli/

EB CLI 설치 (Windows)
https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/eb-cli3-install-windows.html

EB CLI 설치 (macOS)
https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/eb-cli3-install-osx.html

## AWS 준비

- EC2 가 사용할 보안그룹을 하나 준비하고 해당 보안그룹아이디를 이용하여 EB 환경을 생성해야 합니다.
- RDS 인스턴스를 하나 생성하고 외부 접속을 허용한 다음 EC2가 사용할 보안그룹에도 MySQL 접속을 허용해줍니다.
- IAM에서 `aws-elasticbeanstalk-ec2-role` 에 S3 Full Access 등 해당 버킷의 쓰기 권한을 얼여줘야 합니다.


## Git

Git 설치
https://git-scm.com/book/ko/v2/시작하기-Git-설치

설치 후에

```zsh
git init

git add .

git commit -m "Initial Commit"
```

## 좀 더 안전하게 DB 사용자를 추가하려면

db_setup.sql 참고

## Deployment

```zsh
eb init

eb create \
 --vpc.id VPCID \
 --vpc.securitygroups 시큐리티그룹ID \
 --vpc.ec2subnets 서브넷ID,서브넷ID... \
 --envvars PRODUCTION=1,DB_NAME=product_db,DB_USER=db_user,DB_PASSWORD=비밀번호,DB_HOST=DB엔드포인트,S3_BUCKET=버킷이름 \
 --vpc.elbpublic \
 --vpc.publicip
```
