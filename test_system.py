# 系统测试脚本

import sys
import os
from datetime import date, timedelta

# 添加src目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.models.db import SessionLocal
from src.models.init_db import init_db
from src.utils.data_service import DataService
from src.utils.query_service import QueryService
from src.utils.analysis_service import AnalysisService
from src.utils.import_export_service import ImportExportService

def test_db_init():
    """测试数据库初始化"""
    print("测试数据库初始化...")
    try:
        init_db()
        print("✓ 数据库初始化成功")
        return True
    except Exception as e:
        print(f"✗ 数据库初始化失败: {e}")
        return False

def test_add_defective_item():
    """测试添加不良品记录"""
    print("测试添加不良品记录...")
    db = SessionLocal()
    try:
        # 添加测试数据
        item = DataService.add_defective_item(
            db=db,
            item_code="TEST001",
            item_name="测试产品1",
            quantity=5,
            defect_date=date.today(),
            defect_location="生产线A",
            reported_by="测试人员",
            description="测试不良品",
            status="待维修"
        )
        print(f"✓ 不良品记录添加成功，ID: {item.id}")
        return True
    except Exception as e:
        print(f"✗ 不良品记录添加失败: {e}")
        return False
    finally:
        db.close()

def test_query_defective_items():
    """测试查询不良品记录"""
    print("测试查询不良品记录...")
    db = SessionLocal()
    try:
        result = QueryService.get_defective_items(db=db, page=1, page_size=10)
        print(f"✓ 查询成功，共 {result['total']} 条记录")
        return True
    except Exception as e:
        print(f"✗ 查询失败: {e}")
        return False
    finally:
        db.close()

def test_add_repair_record():
    """测试添加维修记录"""
    print("测试添加维修记录...")
    db = SessionLocal()
    try:
        # 先获取一个不良品记录
        items = QueryService.get_defective_items(db=db, page=1, page_size=1)
        if items['total'] > 0:
            item_id = items['items'][0].id
            # 添加维修记录
            record = DataService.add_repair_record(
                db=db,
                defective_item_id=item_id,
                repair_date=date.today(),
                repairer="维修人员",
                repair_method="更换部件",
                repair_duration=30,
                repair_cost=100.50,
                repair_result="成功",
                notes="测试维修"
            )
            print(f"✓ 维修记录添加成功，ID: {record.id}")
            return True
        else:
            print("✗ 没有不良品记录，无法添加维修记录")
            return False
    except Exception as e:
        print(f"✗ 维修记录添加失败: {e}")
        return False
    finally:
        db.close()

def test_add_cause_analysis():
    """测试添加原因分析"""
    print("测试添加原因分析...")
    db = SessionLocal()
    try:
        # 先获取一个不良品记录
        items = QueryService.get_defective_items(db=db, page=1, page_size=1)
        if items['total'] > 0:
            item_id = items['items'][0].id
            # 添加原因分析
            analysis = DataService.add_cause_analysis(
                db=db,
                defective_item_id=item_id,
                analysis_date=date.today(),
                analyst="分析人员",
                root_cause="测试原因",
                contributing_factors="测试影响因素",
                preventive_measures="测试预防措施"
            )
            print(f"✓ 原因分析添加成功，ID: {analysis.id}")
            return True
        else:
            print("✗ 没有不良品记录，无法添加原因分析")
            return False
    except Exception as e:
        print(f"✗ 原因分析添加失败: {e}")
        return False
    finally:
        db.close()

def test_analyze_period():
    """测试时间段分析"""
    print("测试时间段分析...")
    db = SessionLocal()
    try:
        start_date = date.today() - timedelta(days=30)
        end_date = date.today()
        result = AnalysisService.analyze_period(db=db, start_date=start_date, end_date=end_date)
        print(f"✓ 分析成功，统计ID: {result['statistics'].id}")
        print(f"  不良品总数: {result['details']['total_defective']}")
        print(f"  维修率: {result['details']['repair_rate']:.2f}%")
        return True
    except Exception as e:
        print(f"✗ 分析失败: {e}")
        return False
    finally:
        db.close()

def test_trend_analysis():
    """测试趋势分析"""
    print("测试趋势分析...")
    db = SessionLocal()
    try:
        data = AnalysisService.get_trend_analysis(db=db, months=3)
        print(f"✓ 趋势分析成功，共 {len(data)} 个月的数据")
        return True
    except Exception as e:
        print(f"✗ 趋势分析失败: {e}")
        return False
    finally:
        db.close()

def test_export_data():
    """测试数据导出"""
    print("测试数据导出...")
    db = SessionLocal()
    try:
        # 导出不良品记录
        export_path = os.path.join(os.path.dirname(__file__), 'test_defective_items.csv')
        success = ImportExportService.export_defective_items(db=db, file_path=export_path)
        if success:
            print(f"✓ 不良品记录导出成功: {export_path}")
        else:
            print("✗ 不良品记录导出失败")
            return False
        
        # 导出维修记录
        export_path = os.path.join(os.path.dirname(__file__), 'test_repair_records.csv')
        success = ImportExportService.export_repair_records(db=db, file_path=export_path)
        if success:
            print(f"✓ 维修记录导出成功: {export_path}")
        else:
            print("✗ 维修记录导出失败")
            return False
        
        return True
    except Exception as e:
        print(f"✗ 导出失败: {e}")
        return False
    finally:
        db.close()

def run_all_tests():
    """运行所有测试"""
    print("开始测试维修不良品统计系统...\n")
    
    tests = [
        test_db_init,
        test_add_defective_item,
        test_query_defective_items,
        test_add_repair_record,
        test_add_cause_analysis,
        test_analyze_period,
        test_trend_analysis,
        test_export_data
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        if test():
            passed += 1
        else:
            failed += 1
        print()
    
    print(f"测试完成: {passed} 个通过, {failed} 个失败")
    
    if failed == 0:
        print("✓ 所有测试通过，系统功能正常")
    else:
        print("✗ 部分测试失败，需要检查系统功能")

if __name__ == "__main__":
    run_all_tests()
