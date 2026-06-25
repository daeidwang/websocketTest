def solve_chicken_rabbit(heads, legs):
    """
    鸡兔同笼问题求解
    已知总头数和总脚数，求鸡和兔的数量

    公式推导：
    设鸡有 x 只，兔有 y 只
    x + y = heads  (总头数)
    2x + 4y = legs  (总脚数)

    解得：
    y = (legs - 2 * heads) / 2   (兔的数量)
    x = heads - y                (鸡的数量)

    :param heads: 总头数
    :param legs:  总脚数
    :return: (鸡的数量, 兔的数量) 或 None（无解时）
    """
    # 检查输入合法性
    if heads < 0 or legs < 0:
        print("错误：头数和脚数不能为负数！")
        return None

    if legs % 2 != 0:
        print("错误：脚数必须是偶数（鸡2只脚，兔4只脚）！")
        return None

    if legs < 2 * heads:
        print("错误：脚数太少，即使全是鸡也不够！")
        return None

    if legs > 4 * heads:
        print("错误：脚数太多，即使全是兔也超出了！")
        return None

    rabbits = (legs - 2 * heads) // 2
    chickens = heads - rabbits

    return chickens, rabbits


def main():
    print("========== 鸡兔同笼问题求解器 ==========")
    print("已知笼中总头数和总脚数，求鸡和兔各有多少只。")
    print()

    try:
        heads = int(input("请输入总头数："))
        legs = int(input("请输入总脚数："))
    except ValueError:
        print("错误：请输入整数！")
        return

    result = solve_chicken_rabbit(heads, legs)

    if result is not None:
        chickens, rabbits = result
        print()
        print(f"✅ 鸡有 {chickens} 只，兔有 {rabbits} 只")
        print(f"   验证：{chickens}×2 + {rabbits}×4 = {chickens * 2 + rabbits * 4} 只脚 ✔")
        print(f"   验证：{chickens} + {rabbits} = {chickens + rabbits} 个头 ✔")


if __name__ == "__main__":
    main()
