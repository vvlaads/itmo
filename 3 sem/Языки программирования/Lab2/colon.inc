%ifndef COLON_INC
	%define COLON_INC
	%define NEXT_KEY 0x0


	%macro colon 2
		%ifstr %1
		%2:
			dq NEXT_KEY
			db %1, 0
		
			%define NEXT_KEY %2
		%endif
	%endmacro
%endif
