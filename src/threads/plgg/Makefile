CC = gcc
CFLAGS = -Wall -Wextra -std=c99

all: shell_test

shell_test: shell_test.c
	$(CC) $(CFLAGS) -o shell_test shell_test.c

clean:
	rm -f shell_test *.o
