CC = gcc

default: libmain.a

libmain.a: main.o
	ar rcs $@ $^
    
main.o: main.c main.h
	$(CC) -c $<

clean:
	rm *.o *.a
