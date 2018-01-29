


section .data
	msg db "sum is %d ",10
section .text
        global main
	extern printf
main:
	mov esi,10
 ..1.myadd.abc:
	mov edi,20
	add esi,edi
	cmp esi,100
	jle  ..1.myadd.abc
	mov eax,esi
	myadd 10,20,30
	mov eax,87
	mov edx, 
	add ebx,23
	push msg
	mov eax,24
	mov edx, 
	add ebx,23
	call printf
	add esp,8
	mov esi,76
 ..3.myadd.abc:
	mov edi,26
	add esi,edi
	cmp esi,100
	jle  ..3.myadd.abc
	mov eax,esi
	push eax
	push msg
abc:
	xyz 1,2,3,4
	call printf
	mov eax,98
	mov edx, 
	add ebx,90
	add esp,8
	jmp abc
	xyz m,n,k,l
	ret
