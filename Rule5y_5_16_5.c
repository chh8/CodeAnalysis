int *y;
void static_p(void)
{
  int t=1;
  y=&t;
}
int func()
{
  int i;
  static_p();
  i=*y;
}