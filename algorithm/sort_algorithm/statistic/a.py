//#pragma comment(linker, "/STACK:16777216") //for c++ Compiler
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <stack>
#include <string>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <vector>
#include <ctime>
#include <algorithm>
#define Max(a,b) (((a) > (b)) ? (a) : (b))
#define Min(a,b) (((a) < (b)) ? (a) : (b))
#define Abs(x) (((x) > 0) ? (x) : (-(x)))
#define MOD 1000000007
#define pi acos(-1.0)

#define slot_size 100000    //散列槽的大小
#define arr_size 80000      //动态关键字集合
#define min_size 0          //动态关键字集合的最小值
#define max_size 999
#define total_size 999999   //动态关键字集合的最大值
#define NIL -1
#define DELE -2


using namespace std;

typedef long long           ll      ;
typedef unsigned long long  ull     ;
typedef unsigned int        uint    ;
typedef unsigned char       uchar   ;

template<class T> inline void checkmin(T &a,T b){if(a>b) a=b;}
template<class T> inline void checkmax(T &a,T b){if(a<b) a=b;}

const double eps = 1e-7      ;
const int N = 210            ;
const int M = 1100011*2      ;
const ll P = 10000000097ll   ;
const int MAXN = 10900000    ;

long* arr_set;
long link_hash[slot_size];
long suc_count=0;
long unsuc_count=0;

long hash_function (long key,long i) { //第i次探查的序列散列函数
    return (key % 700 + i * (key % (701 - 1))) % slot_size;
}

long* ran_arr (long size, long min = 0, long max = 999) { //产生不重复的自定义范围的随机数
    if(max <= min) {
        return NULL;
    }

    long* arr;
    long up_th = 0;
    long down_th = 0;
    arr = new long[size];
    srand((unsigned)time(NULL));

    for(long i = 0; i < size; i++) {
        long check = 1;
        while (check) {
            up_th = rand() * (max - min) / 32767 + min;
            down_th = rand() * (max - min) / 32767 + min;
            arr[i] = up_th * (max + 1) + down_th;
            long j = 0;
            while(j < i) {
                if(arr[i] == arr[j]) {
                    j = 0;
                    break;
                }
                j++;
            }
            if(j==i)
                check=0;
        }
    }
    return arr;
}

void print_arr(long* set,long size) { //打印数组函数
    for (long i = 0; i < size; i++) {
        cout << set[i] << endl;
    }
}

bool hash_insert(long k) { //插入函数
    long j = 0;
    for(long i = 0; i < slot_size; i++) {
        j = hash_function(k,i);
        if (link_hash[j] == NIL) {
            link_hash[j] = k;
            return true;
        }
    }
    return false;
}

bool hash_find (long k) { //查找函数
    long j = 0;
    for(int i = 0; i < slot_size; i++) {
        j = hash_function(k,i);
        if(link_hash[j] == k)
            return true;
        else {
            if(link_hash[j]==NIL) {
                return false;
            }
        }
    }
    return false;
}

bool hash_delete (long k) { //删除函数
    long j = 0;
    for(int i = 0; i < slot_size; i++) {
        j = hash_function(k,i);
        if(link_hash[j] == k) {
            link_hash[j] = DELE;
            return true;
        } else {
            if (link_hash[j] == NIL) {
                return false;
            }
        }
    }
    return false;
}

void print_hash (long start, long end) { //打印散列表的函数
    long count = 0;
    for (long j = start; j < end; j++) {
        if(link_hash[j] == NIL) {
            cout<<j<<"[NIL]"<<"        ";
        } else if (link_hash[j] == DELE) {
            cout<<j<<"[DEL]"<<"        ";
        } else {
            cout<<j<<"["<<link_hash[j]<<"]     ";
        }
        count++;

        if(count == 4) {
            count = 0;
            cout<<endl;
        }
    }
    cout<<endl;

    return;
}

int main() {
    //初始化散列表的槽
    for(int d=0;d<1;d++) {  //For times
        arr_set = ran_arr(arr_size - d * 10000,min_size,max_size);//to generate arr_size from 1 to 1000 random number
        for(long n=0;n<slot_size;n++) {
            link_hash[n]=NIL;
        }
        cout<<"befor the insertion:"<<endl<<endl;
        print_hash(200,232);

        //插入操作
        for(long m=0; m<arr_size-d*10000; m++) {
            hash_insert(arr_set[m]);
        }
        cout<<"the size of NUMBER is: "<<arr_size-d*10000<<endl;
        cout<<"the size of SLOT is: "<<slot_size<<endl;
        cout<<"the value of a=n/m is: "<<float(arr_size-d*10000)/float(slot_size)<<endl;
        cout<<"after the insertion:"<<endl<<endl;

        print_hash(200,232);

        //查找操作
        for(long n=0; n<arr_size-d*10000; n++) {
            if(hash_find(arr_set[n])) {
                suc_count++;
            } else {
                unsuc_count++;
            }
        }
        
        cout<<"the success finding count is :"<<suc_count<<endl;
        cout<<"the unsuccess finding count is :"<<unsuc_count<<endl<<endl;
        suc_count=unsuc_count=0;//计数清零；
        //删除操作
        for(long j=0; j<arr_size-d*10000; j++) {
            if(hash_delete(arr_set[j])) {
                suc_count++;
            } else {
                unsuc_count++;
            }
        }

        suc_count=unsuc_count=0;//计数清零；
        print_hash(200,232);
    }

    return 0;
}