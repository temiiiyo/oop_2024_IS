#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "structures.h"

// Èíèöèàëèçàöèÿ õðàíèëèùà äàííûõ
void initializeDataStore(DataStore* store) {
    store->applicantCount = 0;
    store->applicantCapacity = 10;
    store->applicants = (Applicant*)malloc(store->applicantCapacity * sizeof(Applicant));

    store->executorCount = 0;
    store->executorCapacity = 10;
    store->executors = (Executor*)malloc(store->executorCapacity * sizeof(Executor));

    store->applicationCount = 0;
    store->applicationCapacity = 10;
    store->applications = (Application*)malloc(store->applicationCapacity * sizeof(Application));
}
// Äîáàâëåíèå çàÿâèòåëÿ
void addApplicant(DataStore* store, int id, const char* name) {
    if (store->applicantCount >= store->applicantCapacity) {
        store->applicantCapacity *= 2;
        store->applicants = (Applicant*)realloc(store->applicants, store->applicantCapacity * sizeof(Applicant));
    }
    store->applicants[store->applicantCount].id = id;
    strcpy(store->applicants[store->applicantCount].name, name);
    store->applicantCount++;
}
// Äîáàâëåíèå èñïîëíèòåëÿ
void addExecutor(DataStore* store, int id, const char* name) {
    if (store->executorCount >= store->executorCapacity) {
        store->executorCapacity *= 2;
        store->executors = (Executor*)realloc(store->executors, store->executorCapacity * sizeof(Executor));
    }
    store->executors[store->executorCount].id = id;
    strcpy(store->executors[store->executorCount].name, name);
    store->executorCount++;
}
// Äîáàâëåíèå çàÿâêè
void addApplication(DataStore* store, int id, int applicantId, int executorId, int repairId, const char* repairDesc, int isCompleted) {
    if (store->applicationCount >= store->applicationCapacity) {
        store->applicationCapacity *= 2;
        store->applications = (Application*)realloc(store->applications, store->applicationCapacity * sizeof(Application));
    }
    store->applications[store->applicationCount].id = id;
    store->applications[store->applicationCount].applicant = store->applicants[applicantId - 1];
    store->applications[store->applicationCount].executor = store->executors[executorId - 1];
    store->applications[store->applicationCount].repair.id = repairId;
    strcpy(store->applications[store->applicationCount].repair.description, repairDesc);
    store->applications[store->applicationCount].isCompleted = isCompleted;
    store->applicationCount++;
}
// ×òåíèå äàííûõ
void readDataFromFile(DataStore* store, const char* filename) {
    FILE* file = fopen(filename, "r");
    char line[MAX_NAME_LENGTH * 2];
    while (fgets(line, sizeof(line), file)) {
        if (strstr(line, "Çàÿâèòåëü") == line) {
            int id;
            char name[MAX_NAME_LENGTH];
            sscanf(line, "Çàÿâèòåëü %d %[^\n]", &id, name);
            addApplicant(store, id, name);
        } else if (strstr(line, "Èñïîëíèòåëü") == line) {
            int id;
            char name[MAX_NAME_LENGTH];
            sscanf(line, "Èñïîëíèòåëü %d %[^\n]", &id, name);
            addExecutor(store, id, name);
        } else if (strstr(line, "Çàÿâêà") == line) {
            int id, applicantId, executorId, repairId, isCompleted;
            char description[MAX_NAME_LENGTH];
            sscanf(line, "Çàÿâêà %d %d %d %d %[^\n] %d", &id, &applicantId, &executorId, &repairId, description, &isCompleted);
            addApplication(store, id, applicantId, executorId, repairId, description, isCompleted);
        }
    }
    fclose(file);
}
// Âûâîä âñåõ çàÿâîê
void printAllApplications(const DataStore* store) {
    FILE* file = fopen("output.txt", "w");
    for (int i = 0; i < store->applicationCount; i++) {
        fprintf(file, "Çàÿâêà ID: %d\n", store->applications[i].id);
        fprintf(file, "Çàÿâèòåëü: %s\n", store->applications[i].applicant.name);
        fprintf(file, "Èñïîëíèòåëü: %s\n", store->applications[i].executor.name);
        fprintf(file, "Ðåìîíò: %s\n", store->applications[i].repair.description);
        fprintf(file, "Ñòàòóñ: %s\n", store->applications[i].isCompleted ? "Çàâåðøåíî" : "Íå çàâåðøåíî");
        fprintf(file, "\n");
    }
    fclose(file);
}
// Âûâîä çàÿâêè ïî ID
void printApplicationById(const DataStore* store, int id) {
    FILE* file = fopen("output.txt", "w");
    for (int i = 0; i < store->applicationCount; i++) {
        if (store->applications[i].id == id) {
            fprintf(file, "Çàÿâêà ID: %d\n", store->applications[i].id);
            fprintf(file, "Çàÿâèòåëü: %s\n", store->applications[i].applicant.name);
            fprintf(file, "Èñïîëíèòåëü: %s\n", store->applications[i].executor.name);
            fprintf(file, "Ðåìîíò: %s\n", store->applications[i].repair.description);
            fprintf(file, "Ñòàòóñ: %s\n", store->applications[i].isCompleted ? "Çàâåðøåíî" : "Íå çàâåðøåíî");
            fclose(file);
            return;
        }
    }
    fclose(file);
}
// Îñâîáîæäåíèå ïàìÿòè
void freeDataStore(DataStore* store) {
    free(store->applicants);
    free(store->executors);
    free(store->applications);
    store->applicants = NULL;
    store->executors = NULL;
    store->applications = NULL;
    store->applicantCount = 0;
    store->executorCount = 0;
    store->applicationCount = 0;
    store->applicantCapacity = 0;
    store->executorCapacity = 0;
    store->applicationCapacity = 0;
}