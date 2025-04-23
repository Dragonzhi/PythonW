#include <stdio.h>

// 交换函数
void Swap(int *pa, int *pb) {
    int temp = *pa;
    *pa = *pb;
    *pb = temp;
}

// 冒泡排序函数
void BubbleSort(int a[], int n) {
    int i, j;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                Swap(&a[j], &a[j + 1]);
            }
        }
    }
}

// 重置数组函数
void ResetArray(int input[], int n, int output[]) {
    int i;

    // 调用冒泡排序函数
    BubbleSort(input, n);

    // 将最大元素放置在合适位置
    output[n / 2] = input[n - 1];

    // 填充output数组
    for (i = 0; i < n / 2; i++) {
        output[i] = input[i];
        output[n - 1 - i] = input[n - 2 - i];
    }

    // 如果数组长度为偶数，交换中间两个元素
    if (n % 2 == 0) {
        int temp = output[n / 2];
        output[n / 2] = output[n / 2 - 1];
        output[n / 2 - 1] = temp;
    }
}

int main() {
    int input1[] = {3, 6, 1, 9, 7};
    int output1[5];
    int input2[] = {3, 6, 1, 9, 7, 8};
    int output2[6];

    // 测试奇数长度数组
    ResetArray(input1, 5, output1);
    for (int i = 0; i < 5; i++) {
        printf("%d ", output1[i]);
    }
    printf("\n");

    // 测试偶数长度数组
    ResetArray(input2, 6, output2);
    for (int i = 0; i < 6; i++) {
        printf("%d ", output2[i]);
    }
    printf("\n");

    return 0;
}