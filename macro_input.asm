%macro myadd 2
	mov esi,%1
%%abc:
	mov edi,%2
	add esi,edi
	cmp esi,100
	jle %%abc
	mov eax,esi
%endmacro	

%macro xyz 4
	mov esi,%1	
%%abc:
	myadd 2
	mov esi,%2
	add edii,esi
	cmp edi,100
	jle %%abc
	mov ebx,edi
%endmacro
	
%macro xyz 2
	mov eax,%2
	mov edx,%3
	%macro mnbv 3
		mov eax,ebx
		mov ecx,%1
		mov edx,%2
	%endmacro
	add ebx,%1
%endmacro

section .data
	msg db "sum is %d ",10
section .text
        global main
	extern printf
main:
	myadd 10,20
	myadd 10,20,30
	xyz 23,87	
	push msg
	xyz 23,24
	call printf
	add esp,8
	myadd 76,26
	push eax
	push msg
abc:
	xyz 1,2,3,4
	call printf
	xyz 90,98
	add esp,8
	jmp abc
	xyz m,n,k,l
	ret
