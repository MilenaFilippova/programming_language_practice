;Найти произведение всех чисел в массиве и вывести на экран

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
        mov     [symbol], eax
        print   1, symbol
        dec     bx
        cmp     bx, 0
        jg      %%_convert
    popd
%endmacro


section .text

global _start


_start:
    mov     al,[x]
    mov     eax, [x]
    mov     ecx, 0
    mov     bx, 1

_multiplication:
    mov     al, [x + ecx]   ;al=эл массива
    mov     bx, [result]    ;bx=result(накапливаем)
    mul     bx              ; al=al*bx
    mov     [result], al
    add     ecx,4
    cmp     ecx, xlen
    jl      _sum
    
    

_end:
    dprint
    mov ebx, 0
    mov eax, 1
    int 0x80
    

section .data
    x dd 2, 1, 3, 3, 2, 4, 1
    xlen    equ $ -x    ;размер массива
    result  dd 1
    
segment .bss
    symbol  resb 1

