-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Дек 14 2024 г., 03:11
-- Версия сервера: 8.0.30
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `WarrantyService`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Clients`
--

CREATE TABLE `Clients` (
  `ClientID` int NOT NULL,
  `FullName` varchar(255) NOT NULL,
  `Address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Clients`
--

INSERT INTO `Clients` (`ClientID`, `FullName`, `Address`) VALUES
(1, 'Иванов Иван Иванович', 'ул. Ленина, д.1'),
(2, 'Петров Петр Петрович', 'ул. Мира, д.2'),
(3, 'Сидорова Мария Алексеевна', 'ул. Гагарина, д.3'),
(4, 'Кузнецов Дмитрий Викторович', 'ул. Советская, д.4');

-- --------------------------------------------------------

--
-- Структура таблицы `EquipmentTypes`
--

CREATE TABLE `EquipmentTypes` (
  `EquipmentTypeID` int NOT NULL,
  `Name` varchar(255) NOT NULL,
  `ManufacturerID` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `EquipmentTypes`
--

INSERT INTO `EquipmentTypes` (`EquipmentTypeID`, `Name`, `ManufacturerID`) VALUES
(1, 'Холодильник', 1),
(2, 'Стиральная машина', 2),
(3, 'Телевизор', 3),
(4, 'Пылесос', 4),
(5, 'Микроволновка', 5);

-- --------------------------------------------------------

--
-- Структура таблицы `Manufacturers`
--

CREATE TABLE `Manufacturers` (
  `ManufacturerID` int NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Manufacturers`
--

INSERT INTO `Manufacturers` (`ManufacturerID`, `Name`) VALUES
(1, 'Samsung'),
(2, 'LG'),
(3, 'Sony'),
(4, 'Bosch'),
(5, 'Panasonic');

-- --------------------------------------------------------

--
-- Структура таблицы `RepairCategories`
--

CREATE TABLE `RepairCategories` (
  `CategoryID` int NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `RepairCategories`
--

INSERT INTO `RepairCategories` (`CategoryID`, `Name`) VALUES
(1, 'Простой'),
(2, 'Сложный'),
(3, 'Капитальный');

-- --------------------------------------------------------

--
-- Структура таблицы `Repairs`
--

CREATE TABLE `Repairs` (
  `RepairID` int NOT NULL,
  `ClientID` int DEFAULT NULL,
  `EquipmentTypeID` int DEFAULT NULL,
  `CategoryID` int DEFAULT NULL,
  `EquipmentName` varchar(255) NOT NULL,
  `RequestDate` date DEFAULT NULL,
  `CompletionDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Repairs`
--

INSERT INTO `Repairs` (`RepairID`, `ClientID`, `EquipmentTypeID`, `CategoryID`, `EquipmentName`, `RequestDate`, `CompletionDate`) VALUES
(1, 1, 1, 2, 'Холодильник Samsung', '2024-01-01', NULL),
(2, 2, 2, 1, 'Стиральная машина LG', '2024-01-05', '2024-01-10'),
(3, 3, 3, 2, 'Телевизор Sony', '2024-01-07', NULL),
(4, 4, 4, 3, 'Пылесос Bosch', '2024-01-10', '2024-01-15'),
(5, 1, 5, 1, 'Микроволновка Panasonic', '2024-01-12', NULL);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `Clients`
--
ALTER TABLE `Clients`
  ADD PRIMARY KEY (`ClientID`);

--
-- Индексы таблицы `EquipmentTypes`
--
ALTER TABLE `EquipmentTypes`
  ADD PRIMARY KEY (`EquipmentTypeID`);

--
-- Индексы таблицы `Manufacturers`
--
ALTER TABLE `Manufacturers`
  ADD PRIMARY KEY (`ManufacturerID`);

--
-- Индексы таблицы `RepairCategories`
--
ALTER TABLE `RepairCategories`
  ADD PRIMARY KEY (`CategoryID`);

--
-- Индексы таблицы `Repairs`
--
ALTER TABLE `Repairs`
  ADD PRIMARY KEY (`RepairID`),
  ADD KEY `ClientID` (`ClientID`),
  ADD KEY `EquipmentTypeID` (`EquipmentTypeID`),
  ADD KEY `CategoryID` (`CategoryID`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `Clients`
--
ALTER TABLE `Clients`
  MODIFY `ClientID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `EquipmentTypes`
--
ALTER TABLE `EquipmentTypes`
  MODIFY `EquipmentTypeID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `Manufacturers`
--
ALTER TABLE `Manufacturers`
  MODIFY `ManufacturerID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `RepairCategories`
--
ALTER TABLE `RepairCategories`
  MODIFY `CategoryID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `Repairs`
--
ALTER TABLE `Repairs`
  MODIFY `RepairID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `Repairs`
--
ALTER TABLE `Repairs`
  ADD CONSTRAINT `repairs_ibfk_1` FOREIGN KEY (`ClientID`) REFERENCES `Clients` (`ClientID`),
  ADD CONSTRAINT `repairs_ibfk_2` FOREIGN KEY (`EquipmentTypeID`) REFERENCES `EquipmentTypes` (`EquipmentTypeID`),
  ADD CONSTRAINT `repairs_ibfk_3` FOREIGN KEY (`CategoryID`) REFERENCES `RepairCategories` (`CategoryID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
