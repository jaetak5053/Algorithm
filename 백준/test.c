#include <stdio.h>
void main()
{
    int arr[5] = {16, 12, 17, 48, 85};
    int i, j, temp = 0;
    for (i = 0; i < 5; i++)
    {
        for (j = i + 1; j < 5; j++)
        {
            if (arr[i] > arr[j])
            {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    printf("%d\n", arr[2]);
}
