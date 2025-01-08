import json


def count_llm_correct(data):
    """
    统计instances中llm_correct为True的个数。

    参数:
    data (dict): 包含instances的字典数据。

    返回:
    int: llm_correct为True的实例数量。
    """
    # 确保数据中存在'instances'键
    if 'instances' not in data:
        return 0

    # 使用生成器表达式遍历instances并计数
    count = sum(1 for instance in data['instances'] if instance.get('llm_correct') is True)
    return count

# 测试
if __name__ == '__main__':
    path = '../results/blocksworld/gpt-4_chat/task_1_plan_generation.json'
    with open(path, 'r') as file:
        data = json.load(file)
    print(count_llm_correct(data))  # 3