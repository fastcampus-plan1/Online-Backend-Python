CREATE TABLE restaurants (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    area_name VARCHAR(100),
    address TEXT,
    phone VARCHAR(20),
    cusine_type VARCHAR(20), -- ENUM('한식', '양식', '중식', '일식', '디저트', '기타'),
    category VARCHAR(20), -- ENUM('category1', 'category2', 'category3'),
    tags TEXT,
    image_urls TEXT,
    menu JSON,
    rating FLOAT,
    keyword TEXT,
    rating_count INT,
    start_time TIME,
    end_time TIME,
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


CREATE TABLE restaurant_reviews (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(100),
    content TEXT,
    restaurant_id BIGINT,
    image_urls TEXT, -- JSON 형태 또는 쉼표로 구분된 문자열로 저장 가능
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
);

