lib=libc.o1
find ./ -name "*.o" | xargs python cast.py --test ${lib} 

