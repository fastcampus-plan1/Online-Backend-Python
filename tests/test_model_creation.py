import pandas as pd
import numpy as np
from unittest.mock import patch
import pytest
from sklearn.ensemble import RandomForestClassifier

from last_chapter.model_creator import create_model

def create_test_data():
    # 샘플 데이터 생성
    data = pd.DataFrame({
        'Temperature': [29.29, 18.58, 25.83, 12.11, 10.88, 1.91, -0.89, np.nan, 8.40],
        'Precipitation': [0.0, 0.0, 94.47, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cloudiness': [23.14, 51.22, 17.05, 36.56, 39.40, 35.91, 18.38, 9.52, 95.70],
        'Snowfall': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 34.34, 49.48, 0.0],
        'Pressure': [1008.69, 1018.49, 997.10, 1006.40, 994.98, 996.55, 1005.33, 994.65, 1016.77],
        'Category': ['분식', '디저트', '찜', '초밥', '찜', '찜', '치킨', '찜', '스테이크']
    })
    return data

@patch('pandas.read_csv', return_value=create_test_data())
def test_create_model(mocked_read_csv):
    # 모델 생성 함수 호출
    model = create_model()

    # 반환된 모델 검증
    assert model is not None, "!!should not be None"
    assert isinstance(model, RandomForestClassifier), "!!should be an instance of RandomForestClassifier"

    # 모킹된 read_csv 함수가 호출되었는지 확인
    mocked_read_csv.assert_called_once_with('csv/weather_data_updated.csv')
