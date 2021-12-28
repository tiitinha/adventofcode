all: test

test: test.o strsplit.o
	g++ -o test test.o strsplit.o

strsplit.o: strsplit.h strsplit.cpp
	g++ -c strsplit.cpp

test.o: test.cpp
	g++ -c test.cpp
