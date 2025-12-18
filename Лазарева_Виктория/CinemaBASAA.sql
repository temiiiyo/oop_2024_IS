-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Дек 14 2024 г., 03:27
-- Версия сервера: 5.7.39
-- Версия PHP: 8.0.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `CinemaBASAA`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Hall`
--

CREATE TABLE `Hall` (
  `HallID` int(11) NOT NULL,
  `Capacity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `Hall`
--

INSERT INTO `Hall` (`HallID`, `Capacity`) VALUES
(1, 50),
(2, 75),
(3, 100),
(4, 150),
(5, 200);

-- --------------------------------------------------------

--
-- Структура таблицы `Movie`
--

CREATE TABLE `Movie` (
  `MovieID` int(11) NOT NULL,
  `Title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Genre` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `Movie`
--

INSERT INTO `Movie` (`MovieID`, `Title`, `Genre`) VALUES
(1, 'Аватар', 'Фантастика'),
(2, 'Король Лев', 'Мультфильм'),
(3, 'Джокер', 'Драма'),
(4, 'Человек-паук', 'Боевик'),
(5, 'Форсаж', 'Боевик'),
(6, 'fffGGF', 'SBDFJB');

-- --------------------------------------------------------

--
-- Структура таблицы `Sale`
--

CREATE TABLE `Sale` (
  `SaleID` int(11) NOT NULL,
  `MovieID` int(11) NOT NULL,
  `HallID` int(11) NOT NULL,
  `ShowTime` datetime NOT NULL,
  `SeatNumber` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `Sale`
--

INSERT INTO `Sale` (`SaleID`, `MovieID`, `HallID`, `ShowTime`, `SeatNumber`) VALUES
(1, 1, 1, '2024-12-12 18:00:00', 1),
(2, 1, 1, '2024-12-12 18:00:00', 2),
(3, 1, 1, '2024-12-12 20:00:00', 1),
(4, 2, 2, '2024-12-13 18:00:00', 1),
(5, 2, 2, '2024-12-13 20:00:00', 2),
(6, 3, 3, '2024-12-14 18:00:00', 3),
(7, 3, 3, '2024-12-14 20:00:00', 4),
(8, 4, 4, '2024-12-15 18:00:00', 5),
(9, 5, 5, '2024-12-15 20:00:00', 6),
(10, 1, 1, '2024-12-12 20:00:00', 5),
(11, 1, 1, '2024-12-12 20:00:00', 2),
(12, 2, 2, '2024-12-13 18:00:00', 2),
(13, 2, 2, '2024-12-13 20:00:00', 4),
(14, 2, 2, '2024-12-13 20:00:00', 5),
(15, 2, 2, '2024-12-13 20:00:00', 1),
(16, 1, 1, '2024-12-12 18:00:00', 3),
(17, 1, 1, '2024-12-12 18:00:00', 4),
(18, 1, 1, '2024-12-12 18:00:00', 5),
(19, 4, 4, '2024-12-15 18:00:00', 150),
(20, 1, 1, '2024-12-12 20:00:00', 4),
(21, 1, 1, '2024-12-12 18:00:00', 6);

-- --------------------------------------------------------

--
-- Структура таблицы `Sessions`
--

CREATE TABLE `Sessions` (
  `SessionID` int(11) NOT NULL,
  `MovieID` int(11) NOT NULL,
  `HallID` int(11) NOT NULL,
  `ShowTime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `Sessions`
--

INSERT INTO `Sessions` (`SessionID`, `MovieID`, `HallID`, `ShowTime`) VALUES
(1, 1, 1, '2024-12-12 18:00:00'),
(2, 1, 1, '2024-12-12 20:00:00'),
(3, 2, 2, '2024-12-13 18:00:00'),
(4, 2, 2, '2024-12-13 20:00:00'),
(5, 3, 3, '2024-12-14 18:00:00'),
(6, 3, 3, '2024-12-14 20:00:00'),
(7, 4, 4, '2024-12-15 18:00:00'),
(8, 5, 5, '2024-12-15 20:00:00'),
(9, 1, 1, '2024-12-03 11:00:00');

-- --------------------------------------------------------

--
-- Структура таблицы `Users`
--

CREATE TABLE `Users` (
  `UserID` int(11) NOT NULL,
  `Username` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Role` enum('User','Admin') COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `Users`
--

INSERT INTO `Users` (`UserID`, `Username`, `Password`, `Role`) VALUES
(1, 'admin', 'admin123', 'Admin'),
(2, 'lazareva', '12345', 'User'),
(3, '', '', 'User'),
(4, 'maha', '12345', 'User');

-- --------------------------------------------------------

--
-- Добавление процедур
--

DELIMITER //

CREATE PROCEDURE `CalculateHall`()
BEGIN
    SELECT 
        h.HallID AS 'Зал',
        s.ShowTime AS 'Время сеанса',
        COUNT(sa.SeatNumber) AS 'Забронировано',
        h.Capacity AS 'Вместимость',
        ROUND((COUNT(sa.SeatNumber) / h.Capacity) * 100, 2) AS 'Процент заполнения'
    FROM Sale sa
    JOIN Hall h ON sa.HallID = h.HallID
    JOIN Sessions s ON sa.HallID = s.HallID AND sa.ShowTime = s.ShowTime
    GROUP BY h.HallID, s.ShowTime;
END //

CREATE PROCEDURE `MostPopular`()
BEGIN
    SELECT 
        m.Genre AS 'Жанр',
        COUNT(sa.SaleID) AS 'Количество проданных билетов'
    FROM Sale sa
    JOIN Movie m ON sa.MovieID = m.MovieID
    GROUP BY m.Genre
    ORDER BY COUNT(sa.SaleID) DESC
    LIMIT 1;
END //

DELIMITER ;

--
-- Индексы сохранённых таблиц
--

ALTER TABLE `Hall` ADD PRIMARY KEY (`HallID`);
ALTER TABLE `Movie` ADD PRIMARY KEY (`MovieID`);
ALTER TABLE `Sale` ADD PRIMARY KEY (`SaleID`), ADD KEY `MovieID` (`MovieID`), ADD KEY `HallID` (`HallID`);
ALTER TABLE `Sessions` ADD PRIMARY KEY (`SessionID`), ADD KEY `MovieID` (`MovieID`), ADD KEY `HallID` (`HallID`);
ALTER TABLE `Users` ADD PRIMARY KEY (`UserID`), ADD UNIQUE KEY `Username` (`Username`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

ALTER TABLE `Hall` MODIFY `HallID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
ALTER TABLE `Movie` MODIFY `MovieID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
ALTER TABLE `Sale` MODIFY `SaleID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
ALTER TABLE `Sessions` MODIFY `SessionID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
ALTER TABLE `Users` MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

ALTER TABLE `Sale` ADD CONSTRAINT `sale_ibfk_1` FOREIGN KEY (`MovieID`) REFERENCES `Movie` (`MovieID`), ADD CONSTRAINT `sale_ibfk_2` FOREIGN KEY (`HallID`) REFERENCES `Hall` (`HallID`);
ALTER TABLE `Sessions` ADD CONSTRAINT `sessions_ibfk_1` FOREIGN KEY (`MovieID`) REFERENCES `Movie` (`MovieID`), ADD CONSTRAINT `sessions_ibfk_2` FOREIGN KEY (`HallID`) REFERENCES `Hall` (`HallID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
