#include  <stdio.h>

void main(int argc, char **argv)
{
	char buf[100];

	snprintf(buf, sizeof buf, argv[1]);
}