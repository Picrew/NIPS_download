# 假设原始链接存储在 'original_links.txt' 文件中
input_filename = 'links.txt'
output_filename = 'Paper_links.txt'

# 打开原始文件和输出文件
with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
    # 逐行读取文件
    for line in infile:
        # 替换 'hash' 为 'file'，'Abstract' 为 'Paper'，以及 'html' 为 'pdf'
        modified_line = line.replace('hash', 'file').replace('Abstract', 'Paper').replace('html', 'pdf')
        # 将修改后的链接写入新文件
        outfile.write(modified_line)

print(f'修改后的链接已经保存到 "{output_filename}"。')
