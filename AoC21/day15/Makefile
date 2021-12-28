all: day15

day15: day15.o dijkstra.o
	g++ -o day15 day15.o dijkstra.o

dijkstra.o: dijkstra.cpp dijkstra.h
	g++ -c dijkstra.cpp

day15.o: day15.cpp
	g++ -c day15.cpp
