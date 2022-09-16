#include <stdio.h>

void solve(int h, int m)
{
    if (m >= 45)
        m = m - 45;
    else
    {
        m = (m - 45) % 60;
        h = (h - 1) % 24;
    }

    if (m < 0)
        m = m + 60;
    if (h < 0)
        h = h + 24;
    printf("%d %d", h, m);
}

int main(void)
{
    int h, m;
    scanf("%d %d", &h, &m);

    solve(h, m);

    return 0;
}