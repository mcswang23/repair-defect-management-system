#!/usr/bin/env python3
# 项目打包脚本

import os
import zipfile
import shutil

# 定义打包的目录和文件
base_dir = os.path.dirname(os.path.abspath(__file__))
package_name = "rework_system"
zip_path = os.path.join(base_dir, f"{package_name}.zip")

# 要包含的文件和目录
include_items = [
    "src",
    "init_database.py",
    "init_database.sql",
    "README.md"
]

# 要排除的文件和目录
exclude_patterns = [
    ".venv",
    "__pycache__",
    "*.pyc",
    "rework_system.db",
    "*.zip"
]

def should_exclude(path):
    """检查路径是否应该被排除"""
    for pattern in exclude_patterns:
        if pattern in path:
            return True
    return False

def add_to_zip(zipf, base_path, current_path):
    """递归添加文件到zip"""
    for item in os.listdir(current_path):
        item_path = os.path.join(current_path, item)
        arcname = os.path.relpath(item_path, base_path)
        
        if should_exclude(item_path):
            continue
        
        if os.path.isdir(item_path):
            add_to_zip(zipf, base_path, item_path)
        else:
            zipf.write(item_path, arcname)
            print(f"添加: {arcname}")

def main():
    print("开始打包项目...")
    
    # 删除旧的zip文件
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"删除旧的打包文件: {zip_path}")
    
    # 创建新的zip文件
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in include_items:
            item_path = os.path.join(base_dir, item)
            if os.path.exists(item_path):
                if os.path.isdir(item_path):
                    add_to_zip(zipf, base_dir, item_path)
                else:
                    arcname = os.path.relpath(item_path, base_dir)
                    zipf.write(item_path, arcname)
                    print(f"添加: {arcname}")
            else:
                print(f"警告: {item} 不存在，跳过")
    
    print(f"\n打包完成！文件保存为: {zip_path}")
    print(f"文件大小: {os.path.getsize(zip_path) / 1024:.2f} KB")

if __name__ == "__main__":
    main()
