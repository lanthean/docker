create database sudoku;
use sudoku;

CREATE TABLE games
(
id INTEGER AUTO_INCREMENT,
name TEXT,
PRIMARY KEY (id)
) COMMENT='this is sudoku game history table';