-- Database schema for Defect Management System

-- Table for Users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table for Products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table for Defects
CREATE TABLE defects (
    defect_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    user_id INT,
    defect_description TEXT NOT NULL,
    status ENUM('open', 'in_progress', 'resolved', 'closed') NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Table for Components
CREATE TABLE components (
    component_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    component_name VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Table for NG Codes
CREATE TABLE ng_codes (
    ng_code_id INT AUTO_INCREMENT PRIMARY KEY,
    code_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table for mapping defects to NG codes
CREATE TABLE defect_ng_code (
    defect_id INT,
    ng_code_id INT,
    PRIMARY KEY (defect_id, ng_code_id),
    FOREIGN KEY (defect_id) REFERENCES defects(defect_id),
    FOREIGN KEY (ng_code_id) REFERENCES ng_codes(ng_code_id)
);