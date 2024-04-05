SRC = ./src/
BIN = ./bin/
PY = makedisc
CXX = main
EXE = makedisc
CC = g++
all:
	cp $(SRC)$(PY).py $(BIN)$(PY).py
	$(CC) -o $(EXE).exe $(SRC)$(CXX).cxx