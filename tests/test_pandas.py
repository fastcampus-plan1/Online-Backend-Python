import pandas as pd
import pytest
from io import StringIO

from last_chapter.test_targets.funcs import process_customer_data, process_join_dates

# 여기에 함수 process_customer_data를 포함시킵니다.

def test_process_customer_data():
    # 테스트용 데이터 생성
    test_data = StringIO("""
    name,age
    Alice,23
    Bob,
    Charlie,35
    """)
    
    # 함수 실행
    result_df = process_customer_data(test_data)
    
    # 결과 검증
    assert result_df['age'].isnull().sum() == 0
    assert result_df['age'].dtype == int
    assert result_df.at[1, 'age'] == 0


def test_process_join_dates():
    # 테스트용 데이터 생성
    test_data = StringIO("""
join_date
2020-01-01 12:30:00
2021-02-02 13:45:00
2022-03-03 14:00:00
""")
    
    # 함수 실행
    result_df = process_join_dates(test_data)
    
    # 결과 검증
    expected_years = [2020, 2021, 2022]
    expected_months = [1, 2, 3]
    expected_days = [1, 2, 3]
    expected_hours = [12, 13, 14]
    expected_minutes = [30, 45, 0]

    assert all(result_df["year"] == expected_years), "연도 문제"
    assert all(result_df["month"] == expected_months), "캘런더 먼스 문제"
    assert all(result_df["day"] == expected_days), "데이 문제"
    assert all(result_df["hour"] == expected_hours), "아워 문제"
    assert all(result_df["minute"] == expected_minutes), "미닛 문제"