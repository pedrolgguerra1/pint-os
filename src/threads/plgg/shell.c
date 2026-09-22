#include "shell.h"
#include "devices/input.h"
#include "lib/kernel/console.h"
#include "lib/stdio.h"
#include <string.h>

#define MAX_INPUT 256
#define PROMPT "plgg> "
#define WHOAMI_NAME "Pedro Loureiro Galvão Guerra"

static void read_line(char *buf, int max_len) {
    int i = 0;
    while (i < max_len - 1) {
        uint8_t c = input_getc();
        if (c == '\r' || c == '\n') {
            putchar('\n');
            break;
        }
        if (c == '\b' || c == 127) {
            if (i > 0) {
                i--;
                putchar('\b');
                putchar(' ');
                putchar('\b');
            }
        } else {
            buf[i++] = (char)c;
            putchar(c);
        }
    }
    buf[i] = '\0';
}

static void trim(char *s) {
    int start = 0;
    while (s[start] == ' ' || s[start] == '\t')
        start++;
    int len = strlen(s + start);
    memmove(s, s + start, len + 1);
    while (len > 0 && (s[len - 1] == ' ' || s[len - 1] == '\t'))
        s[--len] = '\0';
}

void run_shell(void) {
    char buf[MAX_INPUT];

    while (1) {
        printf(PROMPT);
        read_line(buf, MAX_INPUT);
        trim(buf);

        if (strcmp(buf, "whoami") == 0) {
            printf("%s\n", WHOAMI_NAME);
        } else if (strcmp(buf, "exit") == 0) {
            break;
        } else if (buf[0] != '\0') {
            printf("invalid command\n");
        }
    }
}
