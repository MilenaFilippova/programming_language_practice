%macro pushd 0
    push edx
    push ecx
    push ebx
    push eax
%endmacro

%macro popd 0
    pop eax
    pop ebx
    pop ecx
    pop edx
%endmacro

%macro print 2
    pushd
    mov     edx, %1
    mov     ecx, %2
    mov     ebx, 1
    mov     eax, 4
    int     0x80
    popd
%endmacro

%macro dprint 0
    pushd
    mov     bx, 0
    mov     ecx, 10
    
    %%_divide:
        mov     edx, 0
        div     ecx
        push    edx
        inc     bx
        test    eax, eax
        jnz     %%_divide
        
    %%_convert:
        pop     eax
        add     eax, '0'
        mov     [sum], eax
        print   1, sum
        dec     bx
        cmp     bx, 0
        jg      %%_convert
    popd
%endmacro




section .text

global _start

_start:
    mov	ecx, sizex
	lea bx, [x]	;для прохода по массиву 
	xor ax,ax	;зануляет ax
	
_begin:
	add ax,[bx]
	inc bx
	loop _begin
	
_next:
	mov [sum], ax
	mov cx,sizex
	div cx
	mov [srx],ax
	lea bx,[y]
	xor ax,ax
	
_twobegin:
	add ax,[bx]
	inc bx
	loop _twobegin
	mov [sum],ax
	mov cx, [sizey]
	div cx
	mov [sry],ax
	
_substraction:
	mov ax,[srx]
	mov bx, [sry]
	sub ax,bx
	mov [sum],ax	
	
	
	
_end:
	dprint
    
	print   nlen, newline
	print   len, message
	print   nlen, newline

	mov eax,1   
	int 0x80
    

section .data
	x dd 5, 3, 2, 6, 1, 7, 4	;массив
	y dd 0, 10, 1, 9, 2, 8, 5
	sizex equ 7 		;размер массива x
	sizey equ 7 		;размер массива y
	;lenx equ $ -x		;размер массива
	srx db 0		;среднеарифметическое
	sry db 0
	
	sum dd 0		;куда складывать
	message db "Done"
	len equ $ -  message 	;длина сообщения
	newline db 0xA, 0xD
	nlen    equ $ - newline

    
segment .bss
   result resb 10
