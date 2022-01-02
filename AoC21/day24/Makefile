CC=g++

ifeq ($(DEBUG),yes)
	CXXFLAGS=-Wall -g
	LDFLAGS=-Wall -g
else
	CXXFLAGS=-Wall
	LDFLAGS=-Wall
endif

INCPATH=inc
SRCPATH=src
OBJPATH=obj
LIBPATH=lib
BINPATH=bin

INC=
SRC=$(SRCPATH)/day24.cpp
OBJ=$(OBJPATH)/day24.o
OUT=$(BINPATH)/day24

INCLUDES=-I ./strsplit/$(INCPATH)
LIBRARIES=-L ./strsplit/$(LIBPATH)
LIB=-lStrsplit

default: $(OUT)

$(OUT): $(OBJ)
	$(CC) $(LDFLAGS) $(LIBRARIES) -static -o $@ $^ $(LIB)

$(OBJPATH)/%.o: $(SRCPATH)/%.cpp
	$(CC) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

.PHONY: clean cleanall

clean:
	rm -f $(OBJPATH)/*.o

cleanall: clean
	rm -f $(OUT)
