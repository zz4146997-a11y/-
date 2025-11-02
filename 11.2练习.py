import sys

def parse_hrml():
    #首先要求输入两个数值分别表示查询行数和查询数

    N, Q = map(int, input().split())
    hrml = [sys.stdin.readline().strip()for _ in range(N)]
    queries = [input().strip() for _ in range(Q)]

    tag_ = []#构建一个字典
    results = []
    for line in hrml:
        if line.startswith('</'):#用来判断在哪里结束
            if tag_ :
                tag_.pop()#加一个空的
        else:
            parts = line[1:].split()
            tag_name = parts[0]

            attrs = {}
            for attr in parts[1:]:
                key,value = attr.split('=')
                attrs[key] = value.strip('"')

            tag_.append((tag_name,attrs))
    for query in queries:
        tag,attr = query.split('~')
        found = False
        for t,a in reversed(tag_):
            if t == tag :
                results.append(a.get(attr,"Not found"))
                found = True
                break
        if not found:
            results.append("Not found")
    for res in results:
        print(res)
if __name__ =="__main__":
    parse_hrml()
