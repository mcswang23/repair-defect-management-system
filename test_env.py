# 环境测试脚本

print("测试Python环境...")

# 测试基本导入
try:
    import sys
    print(f"Python版本: {sys.version}")
    
    # 测试依赖项
    import sqlalchemy
    print(f"SQLAlchemy版本: {sqlalchemy.__version__}")
    
    import pandas
    print(f"Pandas版本: {pandas.__version__}")
    
    import matplotlib
    print(f"Matplotlib版本: {matplotlib.__version__}")
    
    import seaborn
    print(f"Seaborn版本: {seaborn.__version__}")
    
    import click
    print(f"Click版本: {click.__version__}")
    
    import flask
    print(f"Flask版本: {flask.__version__}")
    
    import flask_sqlalchemy
    print(f"Flask-SQLAlchemy版本: {flask_sqlalchemy.__version__}")
    
    print("所有依赖项导入成功！")
    
    # 测试数据库连接
    from src.models.db import engine
    print("数据库连接成功！")
    
    print("环境测试通过！")
    
except Exception as e:
    print(f"环境测试失败: {e}")
    import traceback
    traceback.print_exc()
