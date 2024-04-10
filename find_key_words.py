import os
import glob
import fitz  # PyMuPDF
from shutil import copy2
from tqdm import tqdm


def find_and_copy_pdfs_with_keywords(source_dir, target_dir, keywords):
    # 获取源目录中所有PDF文件的路径
    pdf_files = glob.glob(os.path.join(source_dir, "*.pdf"))

    # 检查目标目录是否存在，如果不存在则创建
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 使用tqdm创建进度条
    for pdf_file in tqdm(pdf_files, desc="Searching PDFs"):
        # 打开PDF文件
        with fitz.open(pdf_file) as doc:
            # 遍历每一页
            for page in doc:
                # 获取页面文本
                page_text = page.get_text().lower()
                # 检查每个关键词是否在页面文本中
                if all(keyword in page_text for keyword in keywords):
                    # 复制文件到目标目录
                    target_file_path = os.path.join(target_dir, os.path.basename(pdf_file))
                    copy2(pdf_file, target_file_path)
                    print(f"\nKeywords '{', '.join(keywords)}' found. File {pdf_file} has been copied to: {target_file_path}")
                    break  # 停止搜索当前PDF的剩余页面，继续下一个PDF


# 示例使用
source_dir = "downloads"  # 源目录路径
target_dir = "key_words"  # 目标目录路径
keywords = ["placement", "macro"]  # 搜索的关键词列表
find_and_copy_pdfs_with_keywords(source_dir, target_dir, keywords)
