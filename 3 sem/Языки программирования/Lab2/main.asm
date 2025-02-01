%include "colon.inc"
%include "dict.inc"
%include "lib.inc"

%define BUFFER_SIZE 255 ;размер буффера
%define Q_WORD 8 ;длина qword


section .rodata
%include "words.inc"
error_read: db "Не удалось прочитать в буффер", 0
error_find: db "Не удалось найти ключ", 0


section .bss
buffer: resb BUFFER_SIZE ;выделяем место под буффер


section .text
global _start

; записывает строку в буфер
; принимает указатель на буфер, размер буфера
; возвращает адрес начала буфера (0, если ошибка)
read_key:
    xor rdx, rdx ;счётчик символов

.loop:
    push rdi      ;сохраняем адрес буфера
    push rsi      ;сохраняем размер буфера
    push rdx      ;сохраняем счётчик
    call read_char ;считываем символ

    pop rdx       ;восстанавливаем счётчик
    pop rsi       ;восстанавливаем размер буфера
    pop rdi       ;восстанавливаем адрес буфера

    cmp al, ``     ;выход, если конец ввода
    je .end

    cmp al, `\n`  ;выход, если перенос строки
    je .end

    mov byte [rdi+rdx], al ; Записываем символ в буфер
    inc rdx
    cmp rdx, rsi  ;выход, если переполнение буфера
    jae .error
    jmp .loop

.error:
    xor rax, rax ;возвращаем 0 в случае ошибки
    ret

.end:
    cmp rdx, rsi
    jae .error    ;выход, если нет места для нуль-терминатора
    mov byte [rdi+rdx], 0x0 ;добавляем нуль-терминатор
    mov rax, rdi  ;возвращаем адрес буфера
    ret



_start:
	mov rdi, buffer
	mov rsi, BUFFER_SIZE
	call read_key ;чтение из stdin
	mov rdi, buffer
	jz .error_read ;выход, если не удалось прочитать

	mov rdi, rax
	mov rsi, first_word
	call find_word
	jz .error_find ;выход, если не удалось найти ключ

	add rax, Q_WORD ;указатель на ключ
	mov rdi, rax
	push rax
	call string_length
	pop rdi ;указатель на ключ
	inc rax ;смещение
	add rdi, rax ;указатель на значение
	call print_string
	call print_newline

.exit:
	xor rdi, rdi ;выход из программы
	call exit

.error_read: ;не удалось прочитать в буфер
	mov rdi, error_read
	call print_error
	call print_newline_err
	mov rdi, 1
	call exit

.error_find: ;не удалось найти введённый ключ
	mov rdi, error_find
	call print_error
	call print_newline_err
	mov rdi, 1
	call exit