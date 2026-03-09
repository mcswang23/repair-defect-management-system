# 基本测试脚本

import sys
import os

# 添加src目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    print("测试导入模块...")
    from src.models.db import engine, Base
    from src.models.models import DefectiveItem, RepairRecord, CauseAnalysis, Statistics
    from src.models.init_db import init_db
    print("✓ 模块导入成功")
    
    print("测试数据库初始化...")
    init_db()
    print("✓ 数据库初始化成功")
    
    print("测试完成，系统功能正常")
    
except Exception as e:
    print(f"✗ 测试失败: {e}")
    import traceback
    traceback.print_exc()
