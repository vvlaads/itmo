%include "lib.asm"

section .data

str1: db 'ashdb asdhabs dahb',0
str2: db 'ashdb asdhabs dahb!!',0
test: db 0, 0, 0
number: db '-5',0

section .text
global _start

_start:	
;	mov rdi, 'k'
;	call print_char
;	call print_newline
;	mov rdi, test_message
;	call print_string
;	call print_newline

;	mov rdi, str1
;	mov rsi, str2
;	call string_equals

;	call read_char
;	call print_newline
;	mov rdi, test
;	mov rsi, 3
;	call read_word
;	mov rdi, [test]
;	call print_char
;	mov rdi, [test+1]
;	call print_char
;	mov rdi, [test+2]
;	call print_char
;	call print_newline
;	mov rdi, number
;	call parse_uint

;	mov rdi, 18446744073709551615
	mov rdi, -1
	call print_int	
	mov rdi, number
	call parse_int
	call print_newline
	call print_newline
	mov rdi, 0
	call exit
	
