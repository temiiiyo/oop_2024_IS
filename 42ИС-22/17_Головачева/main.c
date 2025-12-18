@@ -0,0 +1,28 @@
#include <stdio.h>
#include "structures.h"

int main() {
    SetConsoleOutputCP(1251);
    SetConsoleCP(1251);
    DataStore store;
    initializeDataStore(&store); // Èíèöèàëèçàöèÿ õðàíèëèùà äàííûõ

    // ×òåíèå äàííûõ
    readDataFromFile(&store, "input.txt");
    int choice;
    printf("Âûáåðèòå äåéñòâèå:\n");
    printf("1. Âûâåñòè âñå çàÿâêè\n");
    printf("2. Âûâåñòè çàÿâêó ïî ID\n");
    scanf("%d", &choice);
    if (choice == 1) {
        printAllApplications(&store);
    } else if (choice == 2) {
        int id;
        printf("Ââåäèòå ID çàÿâêè: ");
        scanf("%d", &id);
        printApplicationById(&store, id);
    }
    // Îñâîáîæäåíèå ïàìÿòè
    freeDataStore(&store);
    return 0;
}