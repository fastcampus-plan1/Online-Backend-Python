CREATE TABLE restaurants (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    area_name VARCHAR(100),
    kakao_place_id VARCHAR(100),
    address TEXT,
    phone VARCHAR(20),
    cuisine_type VARCHAR(20), -- ENUM('한식', '양식', '중식', '일식', '디저트', '기타'),
    category VARCHAR(20), -- ENUM('category1', 'category2', 'category3'),
    tags TEXT,
    menu JSON,
    rating FLOAT,
    keyword TEXT,
    rating_count INT,
    business_hour VARCHAR(100),
    latitude VARCHAR(20),
    longitude VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE restaurant_blog_reviews (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    published_date DATE,
    blog_url VARCHAR(255),
    restaurant_id BIGINT,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
);