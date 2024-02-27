#include<iostream>
#include<fstream>

using namespace std;

int a[10001];
int N=10000;

//随机产生10000个数据存入磁盘文件
void RandomData(const string& filePath)
{
    ofstream fout(filePath);
    for(int i = 0; i < 10000; i++)
    {
        fout << rand() << endl;
    }
    fout.close();
}

//读取data1.txt文件
void ReadData(const string& filePath)
{
    ifstream fin(filePath);
    int n;
    int i=0;
    while(fin >> n)
    {
        a[i++] = n;
    }
    //cout<<"i = "<<i<<endl;
    fin.close();
}

//随机产生10000个数据存入磁盘文件
void test_readData()
{
    ofstream fout("data2.txt");
    for(int i = 0; i < 10000; i++)
    {
        fout << a[i] << endl;
    }
    fout.close();
}

//希尔排序
void shellsort(int a[],int n){
    for(int gap = n/2; gap > 0; gap /= 2){
        for(int i = gap; i < n; i++){
            int temp = a[i];
            int j;
            for(j = i-gap; j >= 0 && a[j] > temp; j -= gap){
                a[j+gap] = a[j];
            }
            a[j+gap] = temp;
        }
    }
    ofstream fout("res_shell.txt");
    for(int i = 0; i < 10000; i++)
    {
        fout << a[i] << endl;
    }
    fout.close();
}


void quicksort(int a[],int n){
    if(n <= 1) return;
    int pivot = a[0];
    int i = 1;
    int j = n-1;
    while(i <= j){
        while(i <= j && a[i] <= pivot) i++;
        while(i <= j && a[j] > pivot) j--;
        if(i < j) swap(a[i],a[j]);
    }
    swap(a[0],a[j]);
    quicksort(a,j);
    quicksort(a+j+1,n-j-1);
}

void QuickSort(int a[],int n){
    quicksort(a,n);
    ofstream fout("res_quick.txt");
    for(int i = 0; i < 10000; i++)
    {
        fout << a[i] << endl;
    }
    fout.close();
}

void swap(int *a,int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void max_heapify(int arr[], int start, int end) {
    //建立父节点指标和子节点指标
    int dad = start;
    int son = dad * 2 + 1;
    while (son <= end) { //若子节点指标在范围内才做比较
        if (son + 1 <= end && arr[son] < arr[son + 1]) //先比较两个子节点大小，选择最大的
            son++;
        if (arr[dad] > arr[son]) //如果父节点大于子节点代表调整完毕，直接跳出函数
            return;
        else { //否则交换父子内容再继续子节点和孙节点比较
            swap(&arr[dad], &arr[son]);
            dad = son;
            son = dad * 2 + 1;
        }
    }
}

// 堆排序，最小堆
void heapsort(int arr[],int len){
    int i;
    //初始化，i从最后一个父节点开始调整
    for (i = len / 2 - 1; i >= 0; i--)
        max_heapify(arr, i, len - 1);
    //先将第一个元素和已排好元素前一位做交换，再从新调整，直到排序完毕
    for (i = len - 1; i > 0; i--) {
        swap(&arr[0], &arr[i]);
        max_heapify(arr, 0, i - 1);
    }
    ofstream fout("res_heap.txt");
    for(int i = 0; i < 10000; i++)
    {
        fout << arr[i] << endl;
    }
    fout.close();
}

//归并排序

void mergesort(int a[],int n,int l,int r){
    if(l == r) return;
    int mid = (l+r)/2;
    mergesort(a,n,l,mid);
    mergesort(a,n,mid+1,r);
    int i = l,j = mid+1,k = 0;
    int temp[r-l+1];
    while(i <= mid && j <= r){
        if(a[i] <= a[j]) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    while(i <= mid) temp[k++] = a[i++];
    while(j <= r) temp[k++] = a[j++];
    for(int i = l;i <= r;i++) a[i] = temp[i-l];
}

void MergeSort(int a[],int n){
    mergesort(a,n,0,n-1);
    ofstream fout("res_merge.txt");
    for(int i = 0; i < 10000; i++)
    {
        fout << a[i] << endl;
    }
    fout.close();
}

int main()
{
    RandomData("data.txt");
    
    ReadData("data.txt");
    //test_readData();
    shellsort(a,N);
    
    ReadData("data.txt");
    QuickSort(a,N);

    ReadData("data.txt");
    heapsort(a,N);

    ReadData("data.txt");
    MergeSort(a,N);
    
		return 0;
}
