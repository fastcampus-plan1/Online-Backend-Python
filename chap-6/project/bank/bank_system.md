## 은행 계좌 관리 시스템
### 은행 계좌
속성: 계좌번호 (`account_number`), 소유주명(`holder_name`), 잔액 (`balance`)  
기능: 입금(`deposit`), 출금(`withdraw`)  
* 잔액 이상 출금 시 `ValueError` 발생

#### 예금 계좌
속성: 계좌번호 (`account_number`), 소유주명(`holder_name`), 잔액 (`balance`), **출금 제한 여부(`is_locked`), 이자율(`interest_rate`)**  
기능: 입금(`deposit`), 출금(`withdraw`), **출금 제한 해제(`unlock`), 정보(`info`)**   
* 출금 제한 계좌에서 출금 시도 시, `AttributeError` 발생
* 출금 제한 해제 시 잔액의 이자율만큼 이자 저축
* 계좌 정보 출력 시 `[예금/{계좌번호}] 잔액 ${잔액}, 이율 {이자율}%, 출금 제한 여부: {True/False}` 로 출력

#### 입출금 계좌
속성: 계좌번호 (`account_number`), 소유주명(`holder_name`), 잔액 (`balance`), **출금 한도(`withdraw_limit`)**  
기능: 입금(`deposit`), 출금(`withdraw`), **출금 한도 변경 (`update_limit`), 정보(`info`)**
* 출금 한도 이상 출금 시도 시, `ValueError` 발생  
* 계좌 정보 출력 시 `[입출금/{계좌번호}] 잔액 ${잔액}, 출금한도 ${출금한도}` 로 출력


---
### 은행 고객
속성: 고객명(`name`), 보유 계좌 리스트(`accounts`), 보유 현금(`money`)  
기능: 계좌 추가(`add_account`), 계좌 목록 조회(`get_account`), 현금 추가(`add_money`), 현금 차감(`deduct_money`), 자산 조회(`get_assets`)  
* 자산 조회 시 보유 현금과 보유 계좌 목록 출력  