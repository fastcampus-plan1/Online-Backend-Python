import joblib
import boto3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier

def load_and_preprocess_data():
    file_s3 = boto3.client('s3')
    file_s3.download_file('fc-python-online', 'weather_data_updated.csv', 'weather_data_updated.csv')
    data = pd.read_csv('weather_data_updated.csv')


    # 결측치 처리
    data.fillna(method='ffill', inplace=True)

    return data

def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    filtered_df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return filtered_df

def preprocess_features(df):
    return df.drop('Category', axis=1), df['Category']

def train_and_predict(X, y):
    # 훈련 데이터와 테스트 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # 모델 초기화
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # 모델 학습
    model.fit(X_train, y_train)

    return model

def lambda_handler(event, context):
    data = load_and_preprocess_data()   
    # 이상치 제거
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        data = remove_outliers(data, column)

    # 피처와 타겟 분리
    X, y = preprocess_features(data)

    # 데이터 전처리 파이프라인
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['Temperature', 'Precipitation', 'Cloudiness', 'Snowfall', 'Pressure']),
        ])

    X_processed = preprocessor.fit_transform(X)
    model = train_and_predict(X_processed, y)

    # S3 클라이언트 생성
    s3_client = boto3.client('s3')

    # 모델 데이터를 직렬화
    model_data = joblib.dumps(model)

    # S3 버킷에 객체 저장
    s3_client.put_object(Bucket='fc-python-online', Key='model_joblib.pkl', Body=model_data)

    return {}
