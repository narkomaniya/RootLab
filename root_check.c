#include <stdio.h>
#include <unistd.h>

int is_root(void) {
    return geteuid() == 0;
}

int main(void) {
    if (is_root()) {
        printf("Программа запущена с root-правами\n");
    } else {
        printf("Программа запущена без root-прав\n");
    }

    return 0;
}
