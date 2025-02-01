section .text
%define SYS_EXIT 60
%define SYS_READ 0
%define SYS_WRITE 1
%define STDIN 0
%define STDOUT 1


global exit
global string_length
global print_string
global print_char
global print_newline
global print_uint
global print_int
global string_equals
global read_char
global read_word
global parse_uint
global parse_int
global string_copy
 
; Принимает код возврата и завершает текущий процесс
exit:
	mov rax, SYS_EXIT
	syscall

; Принимает указатель на нуль-терминированную строку, возвращает её длину
string_length:
	mov rax, rdi

.loop:	cmp byte [rax], 0
	je .exit
	inc rax
	jmp .loop

.exit:	sub rax, rdi
	ret

; Принимает указатель на нуль-терминированную строку, выводит её в stdout
print_string:
	mov rdx, rdi

.loop:	cmp byte [rdx],0
	je .exit
	inc rdx
	jmp .loop

.exit:	sub rdx, rdi
	mov rsi, rdi
	mov rax, SYS_WRITE
	mov rdi, STDOUT
	syscall
    ret

; Принимает код символа и выводит его в stdout
print_char:
	push rdi
	mov rsi, rsp
	mov rax, SYS_WRITE
	mov rdi, STDOUT
	mov rdx, 1
	syscall
	pop rdi
   	ret

; Переводит строку (выводит символ с кодом 0xA)
print_newline:
	mov rdi, `\n`
	jmp print_char

; Выводит беззнаковое 8-байтовое число в десятичном формате 
; Совет: выделите место в стеке и храните там результаты деления
; Не забудьте перевести цифры в их ASCII коды.
print_uint:
	mov r10, 10
	mov rax, rdi
	enter 32, 0
	mov r11, rsp
	add r11, 31
	mov byte [r11], 0x0

.loop:	xor rdx, rdx
	div r10
	dec r11
	add dl, '0'
	mov byte [r11], dl	
	cmp rax, 0x0
	jne .loop
	
	mov rdi, r11
	call print_string
	leave
	ret

; Выводит знаковое 8-байтовое число в десятичном формате 
print_int:
    	test rdi, rdi
	jge .end
	neg rdi
	push rdi
	mov rdi, '-'
	call print_char
	pop rdi
.end:
	jmp print_uint

; Принимает два указателя на нуль-терминированные строки, возвращает 1 если они равны, 0 иначе
string_equals:
.loop:	mov r10b, [rdi]
	mov r11b, [rsi]
	cmp r10b, r11b
	jne .false
	cmp r10b, 0
	je .true
	inc rdi
	inc rsi
	jmp .loop

.false:	xor rax, rax
    ret

.true:	mov rax, 1
	ret

; Читает один символ из stdin и возвращает его. Возвращает 0 если достигнут конец потока
read_char:
    push 0x0
	mov rax, SYS_READ
	mov rdi, STDIN
	mov rdx, 1
	mov rsi, rsp
   	syscall
	pop rax
	ret

; Принимает: адрес начала буфера, размер буфера
; Читает в буфер слово из stdin, пропуская пробельные символы в начале, .
; Пробельные символы это пробел 0x20, табуляция 0x9 и перевод строки 0xA.
; Останавливается и возвращает 0 если слово слишком большое для буфера
; При успехе возвращает адрес буфера в rax, длину слова в rdx.
; При неудаче возвращает 0 в rax
; Эта функция должна дописывать к слову нуль-терминатор

read_word:
	xor rdx, rdx

.loop:	push rdi
	push rsi
	push rdx
	call read_char
	pop rdx
	pop rsi
	pop rdi
	cmp al, ' '
	je .isFirst
	cmp al, `\t`
	je .isFirst
	cmp al, `\n`
	je .isFirst	
	cmp al, ``
	je .exit
	add rdx, 2
	cmp rsi, rdx
	jb .error
	sub rdx, 2
	mov byte [rdi+rdx], al
	inc rdx
	cmp rdx, rsi
	jb .loop
	jmp .error

.isFirst:
	cmp rdx, 0x0
	je .loop
	jmp .exit
	
.error:	xor rax, rax
	ret

.exit:	mov byte [rdi+rdx], 0x0
	mov rax, rdi
	ret
 
; Принимает указатель на строку, пытается
; прочитать из её начала беззнаковое число.
; Возвращает в rax: число, rdx : его длину в символах
; rdx = 0 если число прочитать не удалось
parse_uint:
	xor rax, rax
	xor rdx, rdx
	xor r10, r10
	mov r11, 10

.loop:	mov r10b, [rdi+rdx]
	cmp r10b, 0x0
	je .exit
	cmp r10b, '0'
	jb .exit
	cmp r10b, '9'
	ja .exit
	push rdx
	mul r11
	pop rdx
	sub r10b, '0'
	add rax, r10
	inc rdx
	jmp .loop

.exit:	ret




; Принимает указатель на строку, пытается
; прочитать из её начала знаковое число.
; Если есть знак, пробелы между ним и числом не разрешены.
; Возвращает в rax: число, rdx : его длину в символах (включая знак, если он был) 
; rdx = 0 если число прочитать не удалось
parse_int:
	push rdi
       	cmp byte [rdi], '-'
	jne .plus
	inc rdi
	call parse_uint
	neg rax
	inc rdx
	pop rdi
	ret

.plus:	call parse_uint
	pop rdi
	ret

; Принимает указатель на строку, указатель на буфер и длину буфера
; Копирует строку в буфер
; Возвращает длину строки если она умещается в буфер, иначе 0
string_copy:
	push rdi
	push rsi
	push rdx
	call string_length
	pop rdx
	pop rsi
	pop rdi
    	cmp rdx, rax
	jb .error
	inc rdx
	xor r10, r10

.loop:	mov byte r11b, [rdi+r10]
	mov byte [rsi+r10], r11b
	cmp r10, rax
	je .exit
	inc r10
	jmp .loop

.error:	xor rax, rax
	ret

.exit:	ret

