import re


def count_chinese_and_english(file_path):
    """
    统计 LaTeX 文件中从 \contentpage 到 \begin{references} 之间的中文字符（包括中文逗号和句号），
    以及 \end{lstlisting} 和 algorithm 环境中的英文单词数量。

    参数:
        file_path: LaTeX 文件的路径

    返回:
        中文字符数量和英文单词数量
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 提取从 \contentpage 到 \begin{references} 之间的内容
        match = re.search(r'\\contentpage(.*?)\\begin\{references\}', content, flags=re.DOTALL)

        if not match:
            print("Error: 未找到 \contentpage 或 \begin{references}")
            return 0, 0

        extracted_content = match.group(1)

        # 统计中文字符（包括中文逗号和句号）
        chinese_characters = re.findall(r'[\u4e00-\u9fa5，。]', extracted_content)
        chinese_count = len(chinese_characters)

        # 提取 \end{lstlisting} 环境中的内容
        lstlisting_content = re.findall(r'\\end\{lstlisting\}(.*?)\\begin\{lstlisting\}', extracted_content,
                                        flags=re.DOTALL)
        lstlisting_content = ' '.join(lstlisting_content)

        # 提取 algorithm 环境中的内容
        algorithm_content = re.findall(r'\\begin\{algorithm\}(.*?)\\end\{algorithm\}', extracted_content,
                                       flags=re.DOTALL)
        algorithm_content = ' '.join(algorithm_content)

        # 合并 lstlisting 和 algorithm 内容
        combined_content = lstlisting_content + ' ' + algorithm_content

        # 过滤掉注释（以 % 开头的行）
        combined_content = re.sub(r'%.*', '', combined_content)

        # 统计英文单词
        english_words = re.findall(r'\b[a-zA-Z]+\b', combined_content)
        english_count = len(english_words)

        return chinese_count, english_count

    except Exception as e:
        print(f"Error: {e}")
        return 0, 0


# 使用示例
file_path = "E:\GameDemo\毕设\paper"  # 替换为你的 LaTeX 文件路径
chinese_count, english_count = count_chinese_and_english(file_path)
print(f"中文字符数量（包括中文逗号和句号）: {chinese_count}")
print(f"英文单词数量（包括 lstlisting 和 algorithm 环境）: {english_count}")
print(f"所有单词和字符相加：{english_count+chinese_count}")
# 使用示例
# word_count = count_chinese_characters(file_path)
# print(f"正文字数: {word_count}")