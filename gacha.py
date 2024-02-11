import random

# 初始值设定为0
six_star_counter = 0  # 计数器，用于跟踪连续抽奖未得到6星的次数
four_star_guarantee = 0  # 保底计数器，用于跟踪连续抽奖未得到4星的次数
five_star_guarantee = 0  # 保底计数器，用于跟踪连续抽奖未得到5星的次数
first_ten_draws = True  # 初始设置为第一次抽奖


def draw_lottery(num_draws):
    global six_star_counter, four_star_guarantee, first_ten_draws,five_star_guarantee # 声明为全局变量，以便在函数内部修改全局变量的值
    # 设置奖项与初始概率
    prizes = ["6星", "5星", "4星", "3星"]
    probabilities = [0.02, 0.08, 0.5, 0.4]  # 初始概率
    
    results = []  # 存储抽奖结果


    for i in range(num_draws):  # 根据用户输入的次数进行抽奖
        # 检查4星保底机制
        if four_star_guarantee == 9 and "4星" not in results:
            prize = "4星"
            four_star_guarantee = 0  # 重置保底计数器
        else:
            # 检查6星概率提升机制
            if six_star_counter >= 50:
                print("6星概率提升！")
                extra_probability = min(0.98, 0.02 + 0.02 * (six_star_counter - 49))  # 确保概率不超过100%
                adjusted_probabilities = [extra_probability] + probabilities[1:]
                adjusted_probabilities[2] -= extra_probability - 0.02  # 调整4星概率以保证总和为1
                print("当前概率提升至", adjusted_probabilities[0])
            else:
                adjusted_probabilities = probabilities # 没有概率提升，使用原始概率

            # 如果是前十次抽奖且尚未抽到5星，则强制抽到5星
            if first_ten_draws and five_star_guarantee == 9 and "5星" not in results:
                
                prize = "5星"
                five_star_guarantee = 0  # 重置5星保底计数器
                print("前十次抽奖，强制抽到5星！")
            else:
                prize = random.choices(prizes, weights=adjusted_probabilities, k=1)[0]



            # 更新计数器
            if prize == "4星":
                four_star_guarantee = 0  # 重置4星保底计数器
            else:
                four_star_guarantee += 1  # 未抽到4星，保底计数器增加

            if prize == "5星":
                five_star_guarantee = 0
            else:
                five_star_guarantee += 1

            # 检查并更新6星计数器
            if prize == "6星":
                six_star_counter = 0  # 重置6星计数器
                print("恭喜抽到6星！")
                print(six_star_counter,adjusted_probabilities[0],prize)  # 打印抽到的星级
            else:
                six_star_counter += 1  # 未抽到6星，计数器增加
                print(six_star_counter,adjusted_probabilities[0],prize)  # 打印抽到的星级

        results.append(prize)
    
    first_ten_draws = False  # 第一次抽奖结束后设置为False，确保后续抽奖不再强制抽到5星
    return results

while True:
    num_draws_input = int(input("请输入抽奖次数（输入0退出程序）："))
    if num_draws_input == 0:
        print("程序已退出。")
        break
    
    lottery_results = draw_lottery(num_draws_input)
    results_count = {prize: lottery_results.count(prize) for prize in ["6星", "5星", "4星", "3星"]}
    print(results_count)