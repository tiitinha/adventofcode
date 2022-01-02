CC=g++

ifeq ($(DEBUG), yes)
	CXXFLAGS=-Wall -g
	LDFLAGS=-Wall -g
else
	CXXFLAGS=-Wall
	LDFLAGS=-Wall
endif

AR=ar
ARFLAGS=rcs

INCPATH=inc
SRCPATH=src
OBJPATH=obj
LIBPATH=lib
BINPATH=bin

INC=$(INCPATH)/Strsplit.h
SRC=$(SRCPATH)/Strsplit.cpp
OBJ=$(OBJPATH)/Strsplit.o
OUT=$(LIBPATH)/libStrsplit.a

INCLUDES=-I ./$(INCPATH)

default: $(OUT)

$(OUT): $(OBJ)
	$(AR) $(ARFLAGS) $@ $(OBJ)

$(OBJPATH)/%.o: $(SRCPATH)/%.cpp $(INC)
	$(CC) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

.PHONY: clean cleanall

clean:
	rm -f $OBJPATH/*.o

cleanall: clean
	rm -f $(OUT)
