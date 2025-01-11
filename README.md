# 中文
## notion_export_parser
使用python脚本处理notion导出文件名中的id，并从Markdown文件中移除id和前面的空格。此脚本仅针对Markdown导出。
## 使用方法
1. 从 notion.so 下载 Notion 导出文件。 选择Markdown格式，包含所有内容，并勾选子文件夹和子页面选项。
2. 解压刚刚下载的 zip 文件。 我们将把解压后的文件夹作为下面命令中的 src_dir。
3. 下载脚本，并在已安装 Python 3 的机器上运行以下命令。
```bash
python notion_export_parser.py ./src_dir ./dst_dir
```
4. 代码会将源目录复制到目标目录，并在目标目录中进行所有修改。
5. 现在可以检查目标文件夹。使用 Visual Studio Code，开启 Markdown 渲染功能 (Ctrl+K,V)。从上到下浏览，应该会看到所有图片正确加载:


# English
## notion_export_parser
This Python script parses all folder/ file name, and update the links. Removes 32 digit id in a easy way. This script is for markdown format export only.
## How to use
1. Download Notion Export from notion.so. Choose Markdown and include everything and check on the subfolder and subpage.
2. Extract the zip file you just downloaded which we will use as src_dir in belowing command.
3. Download the script and run belowing commands on machine that have python3 installed.
```bash
python notion_export_parser.py ./src_dir ./dst_dir
```
4. The code will copy the source to dst and do all the modification in the dst.
5. Now you can check the destination folder, simply use visualcode with markdown rendering on (Ctrl+K,V). And browse from top to down. You should have all the images displayed correctly.
