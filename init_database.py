# 数据库初始化脚本

import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.db import engine, Base
from src.models.models import DefectiveItem, User, PcbMaterialMapping, NgCode, Station
from sqlalchemy.orm import sessionmaker

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 创建表结构
Base.metadata.create_all(bind=engine)
print("表结构创建完成")

# 插入默认用户
def insert_default_users():
    users = [
        User(username='admin', password='admin123', role='engineer'),
        User(username='repairer', password='repairer123', role='repairer')
    ]
    
    for user in users:
        existing = session.query(User).filter_by(username=user.username).first()
        if not existing:
            session.add(user)
    
    session.commit()
    print("默认用户插入完成")

# 插入默认NG Code
def insert_default_ng_codes():
    ng_codes = [
        NgCode(code='001', description='空焊'),
        NgCode(code='002', description='短路'),
        NgCode(code='003', description='开路'),
        NgCode(code='004', description='元件损坏'),
        NgCode(code='005', description='虚焊'),
        NgCode(code='006', description='锡球'),
        NgCode(code='007', description='漏焊'),
        NgCode(code='008', description='错件')
    ]
    
    for ng_code in ng_codes:
        existing = session.query(NgCode).filter_by(code=ng_code.code).first()
        if not existing:
            session.add(ng_code)
    
    session.commit()
    print("默认NG Code插入完成")

# 插入默认PCBA料号映射
def insert_default_pcb_mappings():
    mappings = [
        PcbMaterialMapping(pcb_code='65234106', project_name='VOLVO_TCAM'),
        PcbMaterialMapping(pcb_code='65234107', project_name='VOLVO_ECU'),
        PcbMaterialMapping(pcb_code='65234108', project_name='BMW_IDrive'),
        PcbMaterialMapping(pcb_code='65234109', project_name='AUDI_MMI')
    ]
    
    for mapping in mappings:
        existing = session.query(PcbMaterialMapping).filter_by(pcb_code=mapping.pcb_code).first()
        if not existing:
            session.add(mapping)
    
    session.commit()
    print("默认PCBA料号映射插入完成")

# 插入默认站别
def insert_default_stations():
    stations = [
        Station(station_name='Flash'),
        Station(station_name='ICT'),
        Station(station_name='FCT'),
        Station(station_name='Visual'),
        Station(station_name='Packaging')
    ]
    
    for station in stations:
        existing = session.query(Station).filter_by(station_name=station.station_name).first()
        if not existing:
            session.add(station)
    
    session.commit()
    print("默认站别插入完成")

# 执行初始化
if __name__ == '__main__':
    insert_default_users()
    insert_default_ng_codes()
    insert_default_pcb_mappings()
    insert_default_stations()
    print("数据库初始化完成")
