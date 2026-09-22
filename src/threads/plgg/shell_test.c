#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_INPUT 256
#define PROMPT "plgg> "
#define WHOAMI_NAME "Pedro Loureiro Galvão Guerra"

static void trim(char *s) {
    int start = 0;
    while (s[start] == ' ' || s[start] == '\t')
        start++;
    int len = strlen(s + start);
    memmove(s, s + start, len + 1);
    while (len > 0 && (s[len - 1] == ' ' || s[len - 1] == '\t'))
        s[--len] = '\0';
}

int main(void) {
    char buf[MAX_INPUT];

    while (1) {
        printf(PROMPT);
        fflush(stdout);

        if (!fgets(buf, MAX_INPUT, stdin))
            break;

        int len = strlen(buf);
        if (len > 0 && buf[len - 1] == '\n')
            buf[len - 1] = '\0';

        trim(buf);

        if (strcmp(buf, "whoami") == 0) {
            printf("%s\n", WHOAMI_NAME);
        } else if (strcmp(buf, "exit") == 0) {
            break;
        } else if (buf[0] != '\0') {
            printf("invalid command\n");
        }
    }

    return 0;
}
