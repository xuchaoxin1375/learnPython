/*
 * @Description: 
 * @Version: 2.0
 * @Author: xuchaoxin
 * @Date: 2021-03-27 18:34:10
 * @LastEditors: xuchaoxin
 * @LastEditTime: 2021-03-27 19:18:11
 */
#include <stdio.h>
void quick_sort(int s[], int l, int r)
{
    if (l < r)
    {
        //Swap(s[l], s[(l + r) / 2]); //将中间的这个数和第一个数交换 参见注1
        int i = l, j = r, x = s[l];
        while (i < j)
        {
            /* 在处理和轴心相等的元素时需要注意,由于我们需要知道排序后轴心的索引,(我们以轴心左边的元素都小于轴心为划分目标)
            我们包小于轴心的数调到轴心前面,把大等于轴心的元素调到轴心后面(但实际上,轴心在该趟排序完成之前,尚未归位正确的最终位置上),更确切地说,是将严格小于pivot的元素向前调,将大等于pivot的元素向后调,最终会空出一个位置,将pivot插入其中即可(可以用一个比较的简单,而且理性的情况下进行稍微的演算即可知道大概的可行性和正确性)
            如果取的轴心不是序列的首元素,那么可以将位于非首元素的轴心和首元素进行调换,从而将问题转换为以首元素为pivot的quickSort
            这种情况下,将首元素保存起来(到x) */
            while (i < j && s[j] >= x) // 从右向左找第一个小于x的数
                j--;
            if (i < j)
            { // printf("i=%d ",i);
                // printf("s[i]=%d \n",s[i]);
                // i++;
                s[i] = s[j];
                i++;
                // printf("i=%d",i);
                // printf("s[i++]=%d\n",s[])
            }
            while (i < j && s[i] < x) // 从左向右找第一个大于等于x的数
                i++;
            if (i < j)
            /* 这时,s[j]会被覆盖,但是在被覆盖之前,s[j]已经安全转移了(就在前面,s[i]=s[j]处) */
                s[j--] = s[i];
        }
        s[i] = x;

        quick_sort(s, l, i - 1); // 递归调用
        quick_sort(s, i + 1, r);
    }
}
int main()
{
    // int s[]={ 2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12};
    int s[] = {5, 4, 6, 7, 7, 1};
    int len = sizeof(s) / sizeof(int);
    quick_sort(s, 0, len - 1);
    for (int i = 0; i < len; i++)
    {
        printf("%d ", s[i]);
    }
}