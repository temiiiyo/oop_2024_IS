#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <iomanip>

// ==================== КЛАСС ТОВАР ====================
class Item {
public:
    int id;
    std::string name;
    double price;

    Item() = default;

    Item(int id, const std::string& name, double price)
        : id(id), name(name), price(price) {}
};

// ==================== КЛАСС НАКЛАДНОЙ ====================
class Invoice {
private:
    std::string date;
    std::string recipient;

    // key = ID товара, value = пара (товар, количество)
    std::map<int, std::pair<Item, int>> items;

public:
    Invoice(const std::string& date, const std::string& recipient)
        : date(date), recipient(recipient) {}

    // добавление товара
    void addItem(const Item& item, int quantity) {
        if (quantity <= 0) {
            std::cerr << "Ошибка: количество должно быть положительным!\n";
            return;
        }
        items[item.id].first = item;
        items[item.id].second += quantity;
    }

    // подсчёт общей суммы
    double getTotal() const {
        double total = 0.0;
        for (const auto& [id, data] : items) {
            total += data.first.price * data.second;
        }
        return total;
    }

    // вывод в файл
    void printToFile(const std::string& filename) const {
        std::ofstream out(filename);
        if (!out) {
            std::cerr << "Ошибка открытия файла!\n";
            return;
        }

        out << "================ НАКЛАДНАЯ ================\n";
        out << "Дата: " << date << "\n";
        out << "Получатель: " << recipient << "\n\n";

        out << std::left << std::setw(5) << "ID"
            << std::setw(20) << "Товар"
            << std::setw(10) << "Цена"
            << std::setw(10) << "Кол-во"
            << std::setw(10) << "Сумма" << "\n";

        out << "--------------------------------------------\n";

        for (const auto& [id, data] : items) {
            const Item& item = data.first;
            int qty = data.second;
            double sum = item.price * qty;

            out << std::setw(5) << item.id
                << std::setw(20) << item.name
                << std::setw(10) << item.price
                << std::setw(10) << qty
                << std::setw(10) << sum << "\n";
        }

        out << "--------------------------------------------\n";
        out << "ИТОГО: " << getTotal() << " руб.\n";

        out.close();
    }

    // вывод в консоль
    void printToConsole() const {
        std::cout << "\nНакладная для: " << recipient << "\n";
        std::cout << "Дата: " << date << "\n";

        for (const auto& [id, data] : items) {
            std::cout << data.first.name
                      << " | Кол-во: " << data.second
                      << " | Цена: " << data.first.price << "\n";
        }

        std::cout << "Итого: " << getTotal() << " руб.\n";
    }
};

// ==================== MAIN ====================
int main() {
    Item item1(1, "Монитор", 12000.0);
    Item item2(2, "Клавиатура", 2500.0);
    Item item3(3, "Мышь", 1800.0);

    Invoice invoice("2025-12-18", "ООО Дамир");

    invoice.addItem(item1, 2);
    invoice.addItem(item2, 3);
    invoice.addItem(item3, 5);

    invoice.printToConsole();
    invoice.printToFile("invoice.txt");

    std::cout << "\nФайл invoice.txt успешно создан.\n";

    return 0;
}
