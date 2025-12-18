CREATE DATABASE cinema;

USE cinema;

CREATE TABLE Hall (
    hall_id INT AUTO_INCREMENT PRIMARY KEY,
    capacity INT NOT NULL
);

CREATE TABLE Movie (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(100) NOT NULL
);

CREATE TABLE Sale (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    hall_id INT,
    show_time DATETIME,
    seat_number INT,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (hall_id) REFERENCES Hall(hall_id)
);
use cinema;

INSERT INTO Hall (capacity) VALUES (100);
INSERT INTO Hall (capacity) VALUES (150);
INSERT INTO Hall (capacity) VALUES (200);

INSERT INTO Movie (title, genre) VALUES ('Inception', 'Sci-Fi');
INSERT INTO Movie (title, genre) VALUES ('The Godfather', 'Crime');
INSERT INTO Movie (title, genre) VALUES ('The Dark Knight', 'Action');
INSERT INTO Movie (title, genre) VALUES ('Pulp Fiction', 'Drama');
INSERT INTO Movie (title, genre) VALUES ('Forrest Gump', 'Drama');
INSERT INTO Movie (title, genre) VALUES ('The Matrix', 'Sci-Fi');
INSERT INTO Movie (title, genre) VALUES ('The Shawshank Redemption', 'Drama');

INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (1, 1, '2023-10-01 18:00:00', 1);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (1, 1, '2023-10-01 18:00:00', 2);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (1, 1, '2023-10-01 18:00:00', 3);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (2, 2, '2023-10-01 20:00:00', 1);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (2, 2, '2023-10-01 20:00:00', 2);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (3, 3, '2023-10-01 19:00:00', 1);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (3, 3, '2023-10-01 19:00:00', 2);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (3, 3, '2023-10-01 19:00:00', 3);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (3, 3, '2023-10-01 19:00:00', 4);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (4, 1, '2023-10-02 18:00:00', 1);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (4, 1, '2023-10-02 18:00:00', 2);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (4, 1, '2023-10-02 18:00:00', 3);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (4, 1, '2023-10-02 18:00:00', 4);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (4, 1, '2023-10-02 18:00:00', 5);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (5, 2, '2023-10-02 20:00:00', 1);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (5, 2, '2023-10-02 20:00:00', 2);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (5, 2, '2023-10-02 20:00:00', 3);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (5, 2, '2023-10-02 20:00:00', 4);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (6, 3, '2023-10-03 19:00:00', 1);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (6, 3, '2023-10-03 19:00:00', 2);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (6, 3, '2023-10-03 19:00:00', 3);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (6, 3, '2023-10-03 19:00:00', 4);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (6, 3, '2023-10-03 19:00:00', 5);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (7, 1, '2023-10-03 18:00:00', 1);
INSERT INTO Sale (movie_id, hall_id, show_time, seat_number) VALUES (7, 1, '2023-10-03 18:00:00', 2);
