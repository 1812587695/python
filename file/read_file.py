def myreadlines(f, newline):

    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline) # 一下是第一次循环分析 这里返回int：9，字符串”{|}”的位置
            yield buf[:pos] # 这里返回字符串： buf[:9] 等于 123123123
            # print(pos, buf[:pos], buf, "------------------")
            buf = buf[pos + len(newline):] # 这里删除yield之前的字符串，然后得到新字符串buf = buf[9 + 3:]
        chunk = f.read(10) # 读取10个字符串

        # 如果读到文件结尾
        if not chunk:
            yield buf # 返回字符串”{|}”后面的字符串
            break
        buf += chunk # 将读取的字符串加入到buf变量中


with open("input.txt") as f:
    for line in myreadlines(f, "{|}"):
        print(line)

