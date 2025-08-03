import argparse
import random

"""
取得使用者姓名。

此函式會解析命令列參數，若未提供姓名，則會提示使用者輸入姓名。
回傳值:
    str: 使用者的姓名。
"""
def get_user_name()->str:
    parser = argparse.ArgumentParser(description="猜數字遊戲")
    parser.add_argument("-n","--name",type=str,help="姓名")
    parser.add_argument("-f","--frequency",type=int,help="玩的次數",default=1)
    args = parser.parse_args()

    if not args.name:
        name = input("請輸入您的姓名:")
    else:
        name = args.name

    return name


"""
執行一次猜數字遊戲。

參數:
    name (str): 使用者姓名，將於遊戲過程中顯示。
遊戲流程:
    - 隨機產生1~100的整數作為目標數字。
    - 反覆提示使用者猜數字，並根據猜測結果給予提示。
    - 直到猜中為止，顯示猜測次數。
"""
def play_game(name:str)->None:
    i=0
    print(f"========猜數字遊戲第{i+1}次=========\n\n")
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(target)
    while(True):
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"{name}共猜了{count}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!再小一點")
                max = keyin - 1
            else:
                print(f"猜錯了!再大一點")
                min = keyin + 1
            print(f"{name}已經猜{count}次\n")
        else:
            print("請輸入提示範圍內的數字\n")


"""
主程式進入點。

執行流程:
    - 取得使用者姓名。
    - 根據指定次數執行猜數字遊戲。
    - 遊戲結束後顯示總共遊玩的次數。
"""
def main():
    frequency = 1
    name = get_user_name()
    for i in range(frequency):
        play_game(name)
    print(f"遊戲結束,{name}共玩了{frequency}次")

if __name__ == '__main__':
    main()