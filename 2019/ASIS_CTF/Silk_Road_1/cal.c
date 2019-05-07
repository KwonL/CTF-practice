#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool sub_40140A(char *secret)
{
  size_t v1; // r12
  size_t v2; // r12
  bool ret; // al
  int v4; // [rsp+1Ch] [rbp-34h]
  int v5; // [rsp+34h] [rbp-1Ch]
  int v6; // [rsp+38h] [rbp-18h]
  int sint; // [rsp+3Ch] [rbp-14h]

  sint = strtol(secret, 0LL, 10);
  ret = 0;
  if ( sint % (strlen(secret) + 2) || secret[4] != '1' )
    return ret;
  v6 = sint / 100000;
  v5 = sint % 10000;
  if ( 10 * (sint % 10000 / 1000) + sint % 10000 % 100 / 10 - (10 * (sint / 100000 / 1000) + sint / 100000 % 10) != 1
    || 10 * (v6 / 100 % 10) + v6 / 10 % 10 - 2 * (10 * (v5 % 100 / 10) + v5 % 1000 / 100) != 8 )
  {
    return ret;
  }
  v4 = 10 * (v5 / 100 % 10) + v5 % 10;
  if ( (10 * (v6 % 10) + v6 / 100 % 10) / v4 != 3 || (10 * (v6 % 10) + v6 / 100 % 10) % v4 )
    return ret;
  v1 = strlen(secret) + 2;
  v2 = (strlen(secret) + 2) * v1;
  if ( sint % (v5 * v6) == v2 * (strlen(secret) + 2) + 6 )
    ret = 1;
  return ret;
}

char buf[0x100];

int main(int argc, char const *argv[])
{
  for (size_t i = 0; i < 0x100000000; ++i)
  {
    snprintf(buf, sizeof(buf), "%d", (int)i);
    if (sub_40140A(buf))
      puts(buf);//790317143
  }
  return 0;
}
