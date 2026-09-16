from datetime import datetime
if __name__ == '__main__':
    current_time = datetime.now()
    current_time_tim = current_time.strftime("%Y-%m-%d %H:%M:%S")
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    weekday_cn = weekdays[current_time.weekday()]
    print(current_time)
    print(weekday_cn)
    input_lian = input("今天练了么？\n回答:")
    if "没" in input_lian:
        print("快去练，肌肌痒痒的")
        jian_shen = ["练胸","练背","练肩"]*2
        if current_time.weekday() < 6:
            jian_plan = jian_shen[current_time.weekday()]
            print(f'今天应该{jian_plan}')
        else:
            print("今天休息日")
    else:
        print("干别的去吧，肌肌涨涨的")

