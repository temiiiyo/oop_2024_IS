#ifndef STRUCTURES_H
#define STRUCTURES_H
#define MAX_NAME_LENGTH 50

// Ñòðóêòóðû
// Çàÿâèòåëü
typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
} Applicant;

// Èñïîëíèòåëü
typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
} Executor;

// Ðåìîíò
typedef struct {
    int id;
    char description[MAX_NAME_LENGTH];
} Repair;

// Çàÿâêà
typedef struct {
    int id;
    Applicant applicant;
    Executor executor;
    Repair repair;
    int isCompleted;
} Application;

// Ñòðóêòóðà äëÿ õðàíåíèÿ âñåõ äàííûõ
typedef struct {
    Applicant* applicants;      // Äèíàìè÷åñêèé ìàññèâ çàÿâèòåëåé
    int applicantCount;         // Êîëè÷åñòâî çàÿâèòåëåé
    int applicantCapacity;      // Âìåñòèìîñòü ìàññèâà çàÿâèòåëåé

    Executor* executors;        // Äèíàìè÷åñêèé ìàññèâ èñïîëíèòåëåé
    int executorCount;          // Êîëè÷åñòâî èñïîëíèòåëåé
    int executorCapacity;       // Âìåñòèìîñòü ìàññèâà èñïîëíèòåëåé

    Application* applications;  // Äèíàìè÷åñêèé ìàññèâ çàÿâîê
    int applicationCount;       // Êîëè÷åñòâî çàÿâîê
    int applicationCapacity;    // Âìåñòèìîñòü ìàññèâà çàÿâîê
} DataStore;

// Ôóíêöèè
void initializeDataStore(DataStore* store);
void addApplicant(DataStore* store, int id, const char* name);
void addExecutor(DataStore* store, int id, const char* name);
void addApplication(DataStore* store, int id, int applicantId, int executorId, int repairId, const char* repairDesc, int isCompleted);
void readDataFromFile(DataStore* store, const char* filename);
void printAllApplications(const DataStore* store);
void printApplicationById(const DataStore* store, int id);
void freeDataStore(DataStore* store);

#endif // STRUCTURES_H