#include <stdio.h>
#include <conio.h>

int n;//物品数量
double c;//背包容量
double v[100];//各个物品的价值
double w[100];//各个物品的重量
double cw = 0.0;//当前背包重量
double cp = 0.0;//当前背包中物品价值
double bestp = 0.0;//当前最优价值
double perp[100];//单位物品价值排序后
int order[100];//物品编号
int put[100];//设置是否装入

//按单位价值排序
void knapsack()
{
    int i,j;
    int temporder = 0;
    double temp = 0.0;

    for(i=1;i<=n;i++)
        perp[i]=v[i]/w[i];
    for(i=1;i<=n-1;i++)
    {
        for(j=i+1;j<=n;j++)
            if(perp[i]<perp[j])//冒泡排序perp[],order[],sortv[],sortw[]
        {
            temp = perp[i];
            perp[i]=perp[i];
            perp[j]=temp;

            temporder=order[i];
            order[i]=order[j];
            order[j]=temporder;
            temp = v[i];
            v[i]=v[j];
            v[j]=temp;

            temp=w[i];
            w[i]=w[j];
            w[j]=temp;
        }
    }
}

//回溯函数
void backtrack(int i)
{
    double bound(int i);
    if(i>n)
    {
        bestp = cp;
        return;
    }
    if(cw+w[i]<=c)
    {
        cw+=w[i];
        cp+=v[i];
        put[i]=1;
        backtrack(i+1);
        cw-=w[i];
        cp-=v[i];
    }
    if(bound(i+1)>bestp)//符合条件搜索右子数
        backtrack(i+1);
}

//计算上界函数
double bound(int i)
{
    double leftw= c-cw;
    double b = cp;
    while(i<=n&&w[i]<=leftw)
    {
        leftw-=w[i];
        b+=v[i];
        i++;
    }
    if(i<=n)
        b+=v[i]/w[i]*leftw;
    return b;

}


int main()
{
    int i;
    printf("请输入物品的数量和容量：");
    scanf("%d %lf",&n,&c);
    printf("请输入物品的重量和价值：");
    for(i=1;i<=n;i++)
    {
        printf("第%d个物品的重量：",i);
        scanf("%lf",&w[i]);
        printf("价值是：");
        scanf("%lf",&v[i]);
        order[i]=i;
    }
    knapsack();
    backtrack(1);
    printf("最有价值为：%lf\n",bestp);
    printf("需要装入的物品编号是：");
    for(i=1;i<=n;i++)
    {
        if(put[i]==1)
            printf("%d ",order[i]);
    }
    return 0;
}