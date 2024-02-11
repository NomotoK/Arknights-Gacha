import random

def select_prize(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        prizes = file.read().split(',')
        # 前两个奖品各占35%概率，剩余奖品共占30%概率
        probabilities = [0.35, 0.35] + [0.3 / (len(prizes) - 2)] * (len(prizes) - 2)
        return random.choices(prizes, weights=probabilities)[0]

file_name = './operator_list/six_star_prize.txt' # 奖品文件路径

selected_prize = select_prize(file_name)
print("恭喜你，你抽中了：", selected_prize.strip())