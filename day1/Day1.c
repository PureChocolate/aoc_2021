#include <stdio.h>

int main(int argc, char const *argv[])
{
    FILE *file;
    file = fopen("in.txt", "r");
    char *st = NULL;
    int data[2000];
    int a = 0;
    if(file){
        while(a < 2000){
            fscanf(file, "%d", &data[a]);
            a += 1;
        }        
    }
    int prev = data[0] + data[1] + data[2];
    int times, times1 = 0;
    int prev1 = data[0];
    for(int i = 3; i < 2000; i++){

        int new = (prev - data[i-3]) + data[i];
        if(data[i] > prev1) times1++;
        prev1 = data[i];
        
        if(new > prev) times++;
        prev = new;
    }
    fclose(file);
    printf("%d\n", times1);
    printf("%d\n",times);
    return 0;
}