# いい子のおもちゃだけを数える関数
def sum_positive_numbers(numbers_list):
    total = 0                  # かご（合計用の箱）は最初は空っぽ
    for number in numbers_list:  # 一つずつおもちゃを取り出して
        if number > 0:           # 「いい子」（0より大きい数）なら
            total += number      # かごに入れる
    return total               # 最後にかごの中身の数を返す

# おもちゃの箱を用意
numbers_list = [3, -1, 4, -2, 5]

# いい子のおもちゃだけを数えて見せる
print(sum_positive_numbers(numbers_list))