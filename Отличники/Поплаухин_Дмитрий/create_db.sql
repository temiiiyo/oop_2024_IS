CREATE TABLE Категории (
                           Код_категории SERIAL PRIMARY KEY,
                           название VARCHAR(255)
);

CREATE TABLE Номера (
                        Код_номера SERIAL PRIMARY KEY,
                        код_категории INTEGER REFERENCES Категории(Код_категории),
                        номер INTEGER,
                        мест INTEGER
);

CREATE TABLE Граждане (
                          Код_гражданина SERIAL PRIMARY KEY,
                          ФИО VARCHAR(255),
                          паспорт VARCHAR(255)
);

CREATE TABLE Размещение (
                            Код_размещения SERIAL PRIMARY KEY,
                            код_гражданина INTEGER REFERENCES Граждане(Код_гражданина),
                            код_номера INTEGER REFERENCES Номера(Код_номера),
                            дата_въезда DATE,
                            срок_проживания INTEGER
);
