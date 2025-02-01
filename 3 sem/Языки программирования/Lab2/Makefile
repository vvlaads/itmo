ASM = nasm #компилятор
LD = ld #линкер

ASM_FLAGS = -felf64 #флаги сборки
OBJ_FLAGS = -o #флаги линковки
GDB_FLAGS = -g #флаг для gdb

main: main.o lib.o dict.o
	@$(LD) $(OBJ_FLAGS) $@ $^


%.o: %.asm 
	@$(ASM) $(ASM_FLAGS) $(GDB_FLAGS) $(OBJ_FLAGS) $@ $^


.PHONY: test
test:
	@python3 test.py


.PHONY: clean
clean:
	@rm *.o main
