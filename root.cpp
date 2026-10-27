#include <iostream>
#include <unistd.h>

int main() {
    if (geteuid() == 0) {
        std::cout << "Root-доступ есть\n";
    } else {
        std::cout << "Root-доступа нет\n";
    }

    return 0;
}