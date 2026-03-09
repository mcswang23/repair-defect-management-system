-- 维修不良品管理系统数据库初始化脚本

-- 创建用户表
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 创建PCBA料号映射表
CREATE TABLE IF NOT EXISTS pcb_material_mappings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pcb_code VARCHAR(50) NOT NULL UNIQUE,
    project_name VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 创建NG Code字典表
CREATE TABLE IF NOT EXISTS ng_codes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 创建不良品记录表
CREATE TABLE IF NOT EXISTS defective_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project VARCHAR(100) NOT NULL,
    sfc VARCHAR(50) NOT NULL UNIQUE,
    station VARCHAR(100) NOT NULL,
    repair_time DATETIME NOT NULL,
    mes_defect_info TEXT,
    analysis_result TEXT,
    material_code VARCHAR(50) NOT NULL,
    failure_code VARCHAR(100),
    attached_pcba_sfc VARCHAR(50),
    repairer VARCHAR(50) NOT NULL,
    analysis_status VARCHAR(20) NOT NULL,
    repair_complete_time DATETIME,
    return_to_line_time DATETIME,
    repair_count INTEGER NOT NULL DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 创建索引
CREATE INDEX IF NOT EXISTS idx_defective_items_project ON defective_items(project);
CREATE INDEX IF NOT EXISTS idx_defective_items_sfc ON defective_items(sfc);
CREATE INDEX IF NOT EXISTS idx_defective_items_repairer ON defective_items(repairer);
CREATE INDEX IF NOT EXISTS idx_defective_items_analysis_status ON defective_items(analysis_status);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_pcb_material_mappings_pcb_code ON pcb_material_mappings(pcb_code);
CREATE INDEX IF NOT EXISTS idx_ng_codes_code ON ng_codes(code);

-- 插入默认用户
INSERT OR IGNORE INTO users (username, password, role) VALUES
('admin', 'admin123', 'engineer'),
('repairer', 'repairer123', 'repairer');

-- 插入默认NG Code
INSERT OR IGNORE INTO ng_codes (code, description) VALUES
('001', '空焊'),
('002', '短路'),
('003', '开路'),
('004', '元件损坏'),
('005', '虚焊'),
('006', '锡球'),
('007', '漏焊'),
('008', '错件');

-- 插入默认PCBA料号映射
INSERT OR IGNORE INTO pcb_material_mappings (pcb_code, project_name) VALUES
('65234106', 'VOLVO_TCAM'),
('65234107', 'VOLVO_ECU'),
('65234108', 'BMW_IDrive'),
('65234109', 'AUDI_MMI');
