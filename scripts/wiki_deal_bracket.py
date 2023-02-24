##
# import os
import os.path as op


dirName = "./"
fileName = 'tt'
filePath = op.join(dirName, fileName)
if op.exists(filePath):
    print("file exist!")
else:
    print("file does not exist!")
print("\n"*2)
with open(fileName, encoding="utf-8") as f:
    read_data = f.read()
# print(read_data)



import re
##
test_text = r"w(Image: f_{X}(x))xx(Image: f_{Y}(Y))={\begin{cases}\Pr(X=x),&x\in S,\\0,&x\in {\mathbb  {R}}\backslash S.\end{cases}}  )j111"
contents = read_data
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
header=read_data[:indexes_token[0]]
# puts(header)
# out_data=header
out_lines=[]
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
    cntl=0
    close_rp=0
    # print(t,"\n")
    for i in range(len(t)):
        if(t[i] =='('):
            cntl+=1
            # print(i)
        elif (t[i] ==')'):
            close_rp+=1
            # print(i)
        if close_rp==cntl+1:
            break
    # print(cntl,close_rp)
    out_line=t[:i]+'$'+t[i+1:]
    out_lines.append(out_line)
    # puts(out_lines)


    # puts(res)

    # m=p2.search(t)
    # gps=m.groups()
    # print(gps)
    # print(res)

##
out_data=header+"".join(out_lines)
out_data=out_data.replace("[edit]","")
print(out_data)
out=op.join(dirName,"out_wiki.md")
with open(out,"w") as fout:
    fout.write(out_data)
