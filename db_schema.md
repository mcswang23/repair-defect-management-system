# 维修不良品统计数据库设计

## 1. 不良品记录表 (defective_items)
| 字段名 | 数据类型 | 描述 | 约束 |
|-------|---------|------|------|
| id | INTEGER | 不良品ID | PRIMARY KEY AUTOINCREMENT |
| item_code | VARCHAR(50) | 产品编码 | NOT NULL |
| item_name | VARCHAR(100) | 产品名称 | NOT NULL |
| quantity | INTEGER | 不良品数量 | NOT NULL |
| defect_date | DATE | 发现日期 | NOT NULL |
| defect_location | VARCHAR(100) | 发现位置 | NOT NULL |
| reported_by | VARCHAR(50) | 报告人 | NOT NULL |
| description | TEXT | 不良描述 | |
| status | VARCHAR(20) | 状态(待维修/维修中/已维修/报废) | NOT NULL |
| created_at | TIMESTAMP | 记录创建时间 | DEFAULT CURRENT_TIMESTAMP |
| updated_at | TIMESTAMP | 记录更新时间 | DEFAULT CURRENT_TIMESTAMP |

## 2. 维修记录表 (repair_records)
| 字段名 | 数据类型 | 描述 | 约束 |
|-------|---------|------|------|
| id | INTEGER | 维修记录ID | PRIMARY KEY AUTOINCREMENT |
| defective_item_id | INTEGER | 关联的不良品ID | FOREIGN KEY REFERENCES defective_items(id) |
| repair_date | DATE | 维修日期 | NOT NULL |
| repairer | VARCHAR(50) | 维修人员 | NOT NULL |
| repair_method | TEXT | 维修方法 | NOT NULL |
| repair_duration | INTEGER | 维修时长(分钟) | NOT NULL |
| repair_cost | DECIMAL(10,2) | 维修成本 | NOT NULL |
| repair_result | VARCHAR(20) | 维修结果(成功/失败/部分成功) | NOT NULL |
| notes | TEXT | 维修备注 | |
| created_at | TIMESTAMP | 记录创建时间 | DEFAULT CURRENT_TIMESTAMP |

## 3. 原因分析表 (cause_analysis)
| 字段名 | 数据类型 | 描述 | 约束 |
|-------|---------|------|------|
| id | INTEGER | 分析ID | PRIMARY KEY AUTOINCREMENT |
| defective_item_id | INTEGER | 关联的不良品ID | FOREIGN KEY REFERENCES defective_items(id) |
| analysis_date | DATE | 分析日期 | NOT NULL |
| analyst | VARCHAR(50) | 分析人员 | NOT NULL |
| root_cause | TEXT | 根本原因 | NOT NULL |
| contributing_factors | TEXT | 影响因素 | |
| preventive_measures | TEXT | 预防措施 | NOT NULL |
| created_at | TIMESTAMP | 记录创建时间 | DEFAULT CURRENT_TIMESTAMP |

## 4. 统计汇总表 (statistics)
| 字段名 | 数据类型 | 描述 | 约束 |
|-------|---------|------|------|
| id | INTEGER | 统计ID | PRIMARY KEY AUTOINCREMENT |
| period_start | DATE | 统计开始日期 | NOT NULL |
| period_end | DATE | 统计结束日期 | NOT NULL |
| total_defective | INTEGER | 不良品总数 | NOT NULL |
| total_repaired | INTEGER | 已维修数量 | NOT NULL |
| total_scrapped | INTEGER | 已报废数量 | NOT NULL |
| repair_rate | DECIMAL(5,2) | 维修率(%) | NOT NULL |
| average_repair_time | DECIMAL(10,2) | 平均维修时长(分钟) | NOT NULL |
| total_repair_cost | DECIMAL(10,2) | 总维修成本 | NOT NULL |
| most_common_cause | TEXT | 最常见不良原因 | |
| created_at | TIMESTAMP | 记录创建时间 | DEFAULT CURRENT_TIMESTAMP |

## 5. 索引设计
- 为不良品记录表的 item_code, defect_date, status 字段创建索引
- 为维修记录表的 repair_date, repairer 字段创建索引
- 为原因分析表的 analysis_date 字段创建索引
- 为统计汇总表的 period_start, period_end 字段创建索引
