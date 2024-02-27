# Introduction

Django Elastic Beanstalk 배포

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

## Deployment

eb init

eb create \
 --vpc.id VPCID \
 --vpc.securitygroups 시큐리티그룹ID \
 --vpc.ec2subnets 서브넷ID,서브넷ID... \
 --envvars PRODUCTION=1,DB_NAME=product_db,DB_USER=db_user,DB_PASSWORD=비밀번호,DB_HOST=DB엔드포인트 \
 --vpc.elbpublic \
 --vpc.publicip
