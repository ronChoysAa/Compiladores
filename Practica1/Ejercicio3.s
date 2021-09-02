	.file	"Ejercicio3.cpp"
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "abcdef\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB0:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$32, %esp
	call	___main
	movl	$LC0, 28(%esp)
	movl	$11148, 24(%esp)
	movl	24(%esp), %eax
	cltd
	andl	$7, %edx
	addl	%edx, %eax
	sarl	$3, %eax
	movl	%eax, 20(%esp)
	movl	24(%esp), %eax
	cltd
	andl	$3, %edx
	addl	%edx, %eax
	sarl	$2, %eax
	movl	%eax, 16(%esp)
	movl	24(%esp), %eax
	movl	%eax, %edx
	shrl	$31, %edx
	addl	%edx, %eax
	sarl	%eax
	movl	%eax, 12(%esp)
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE0:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
