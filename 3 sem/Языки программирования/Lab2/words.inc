%ifndef WORDS_INC
	%define WORDS_INC

	%include "colon.inc"


	colon "test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size!", fifth_word
	db "bad buffer", 0

	colon "test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size test buffer size", fourth_word
	db "good buffer", 0

	colon "third 3", third_word
	db "third word explanation???", 0

	colon "12345", second_word
	db "digits 21313", 0 

	colon "first word", first_word
	db "first word explanation", 0 
%endif
