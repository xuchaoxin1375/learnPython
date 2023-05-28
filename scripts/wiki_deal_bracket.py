##
""" 功能说明:
由于具体文本内容的复杂性,公式中如果包含非成对的括号时,容易导致错误解析
这种情况常见于函数取值范围/定义域,x\in[0,1),建议手动调整或者从源网页提取latex源码

总的来说,本程序适合处理内联的小段公式(括号成都对的情况)
虽然内置了集中括号替换方案,有不同的优缺点,还是建议结合手动修改
"""
import re
import os.path as op

# dirName = "./"
dirName = r"d:/repos/PythonLearn/scripts"#使用硬链接共享文件
# dirName = r'd:\repos\scripts'
fileName = 'wiki_content.md'
filePath = op.join(dirName, fileName)
if op.exists(filePath):
    # print("file exist!")
    pass
else:
    print("file does not exist!🎈🎈🎈")
    with open(filePath, 'w') as f:
        print("empty file created!")
        # pass
print("\n"*2)
# 注意编码问题(charmap)
file1 = "d:/repos/PythonLearn/scripts/tt"
file2 = r"d:\repos\PythonLearn\scripts\tt"
with open(filePath, encoding="utf-8") as f:
    read_data = f.read()
# print(read_data)

##
test_text_0 = r"start[edit] w(Image: f_{X}(x))x[编辑]x(Image: f_{Y}(Y))={\begin{cases}\Pr(X=x),&x\in S,\\0,&x\in {\mathbb  {R}}\backslash S.\end{cases}}  )j111"

test_text2 = r"(Image: {\displaystyle {\begin{aligned}\sin x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n+1)!}}x^{2n+1}&&=x-{\frac {x^{3}}{3!}}+{\frac {x^{5}}{5!}}-\cdots &&\forall x\\[6pt]\cos x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n)!}}x^{2n}&&=1-{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}-\cdots &&\forall x\\[6pt]\tan x&=\sum _{n=1}^{\infty }{\frac {B_{2n}(-4)^{n}\left(1-4^{n}\right)}{(2n)!}}x^{2n-1}&&=x+{\frac {x^{3}}{3}}+{\frac {2x^{5}}{15}}+\cdots &&\forall x:|x|<{\frac {\pi }{2}}\\[6pt]\sec x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}E_{2n}}{(2n)!}}x^{2n}&&=1+{\frac {x^{2}}{2}}+{\frac {5x^{4}}{24}}+\cdots &&\forall x:|x|<{\frac {\pi }{2}}\\[6pt]\arcsin x&=\sum _{n=0}^{\infty }{\frac {(2n)!}{4^{n}(n!)^{2}(2n+1)}}x^{2n+1}&&=x+{\frac {x^{3}}{6}}+{\frac {3x^{5}}{40}}+\cdots &&\forall x:|x|\leq 1\\[6pt]\arccos x&={\frac {\pi }{2}}-\arcsin x\\&={\frac {\pi }{2}}-\sum _{n=0}^{\infty }{\frac {(2n)!}{4^{n}(n!)^{2}(2n+1)}}x^{2n+1}&&={\frac {\pi }{2}}-x-{\frac {x^{3}}{6}}-{\frac {3x^{5}}{40}}+\cdots &&\forall x:|x|\leq 1\\[6pt]\arctan x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{2n+1}}x^{2n+1}&&=x-{\frac {x^{3}}{3}}+{\frac {x^{5}}{5}}-\cdots &&\forall x:|x|\leq 1,\ x\neq \pm i\end{aligned}}})"

test_text3 = r'By setting(Image: {\displaystyle t=\tan {\tfrac {1}{2}}\theta, }) all trigonometric functions of(Image: \theta) can be expressed as rational fractions of(Image: t):(Image: {\displaystyle {\begin{aligned}\sin \theta &= {\frac {2t}{1+t ^ {2}}}, \\[5mu]\cos \theta &= {\frac {1-t ^ {2}}{1+t ^ {2}}}, \\[5mu]\tan \theta &= {\frac {2t}{1-t ^ {2}}}.\end{aligned}}})'

test_text = test_text3
#调试用:设置为0表示读取外部文件的文本,设置为1表示使用上述字符串作为测试文本
is_local = 0

contents = read_data if not is_local else test_text
# 分片策略
indexes_token = []
p = re.compile(r"\(Image:")
matches = p.finditer(contents)
# matches
for match in matches:
    span = match.span()
    start = span[0]
    indexes_token.append(start)
# print(indexes_token)
seg_tuples = [i for i in indexes_token]
refine_segs = []

bl = list('([{')  # brackets_left
br = list(')]}')  # brackets_right

# def get_last_rp(s):
#     """ get right parenthesis index """
#     return s.rfind(')')


def puts(s):
    print(s, end='')


# indexes_token.insert(0,0)
indexes_token.append(len(contents))
indexes_seg = indexes_token
header = contents[:indexes_token[0]]
# puts(header)
# out_data=header
out_lines = []
p1 = re.compile(r'\(Image:\s*')
for i in range(len(indexes_seg)-1):

    start = indexes_seg[i]
    end = indexes_seg[i+1]
    # end_rp=s1[:end].rfind(')')+1
    end_rp = start+contents[start:end].rfind(')')
    end_rp_next = end_rp+1
    # print(start,end_rp)
    seg = contents[start:end]
    # print(seg)
    # 处理`(imag: `
    t = p1.sub(r'$', seg)
    # 处理各段最后一个右括号`)`
    # 方法1:
    # seg_rp = t[:end].rfind(')')
    # seg_rp_next=seg_rp+1
    # # print(seg_rp)
    # puts(t[:seg_rp_next]+'$'+t[seg_rp_next+1:])
    # # refine_segs.append(s1[start:end_rp])
    # 放法2:用正则方法(兼容性不足)
    # print(t)
    # p2 = re.compile(r'(.*[^\s])(\s*\))')
    # res = p2.sub(r'\1$', t)
    # 方法3:括号对数计数法
    cntl = 0
    close_rp = 0
    # print(t,"\n")
    for i in range(len(t)):
        if (t[i] == '('):
            cntl += 1
            # print(i)
        elif (t[i] == ')'):
            close_rp += 1
            # print(i)
        if close_rp == cntl+1:
            break
    # print(cntl,close_rp)
    out_line = t[:i]+'$'+t[i+1:]
    out_lines.append(out_line)
    # puts(out_lines)

    # puts(res)

    # m=p2.search(t)
    # gps=m.groups()
    # print(gps)
    # print(res)

##
out_data = header+"".join(out_lines)
p_edit = re.compile(r'\[((edit)|(编辑))\]')
p_2slash = re.compile(r'(\\{2})(\[\d+\w+\])*')
out_data = p_2slash.sub(r'\1\2'+'\n\t', out_data)
# out_data=out_data.replace(r'\\',r"\\"+"\n\t")
out_data = p_edit.sub(r'🎈\n', out_data)
# out_data=out_data.replace("[edit]","\n").replace("[编辑]","\n")

print(out_data)

out = op.join(dirName, filePath)
with open(out, "w", encoding="utf-8") as fout:
    fout.write(out_data)
