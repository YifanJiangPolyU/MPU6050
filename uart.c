
#define F_CPU 16000000UL

#include "uart.h"


// initialize UART
void uart_init() {
   
  UBRR0H = UBRRH_VALUE;
  UBRR0L = UBRRL_VALUE;

  UCSR0A &= ~(_BV(U2X0));

  UCSR0C = _BV(UCSZ01) | _BV(UCSZ00); // 8-bit data
  UCSR0B = _BV(RXEN0) | _BV(TXEN0) | _BV(RXCIE0);   // Enable RX and TX

  
}

void uart_putchar(char data) {
    while ( !( UCSR0A & (1<<UDRE0)) );
    UDR0 = data;
}

char uart_getchar(void) {
    while ( !(UCSR0A & (1<<RXC0)) ) ;
    return UDR0;
}

void uart_putstring(char * s) {
  int i = 0;
  while(s[i]!='\0'){
    uart_putchar(s[i]);
    ++i;
  };
  
}

void uart_putint16(int16_t data) {
	uint8_t a = data & 0xFF;
	uart_putchar(a);
	a = data >> 8;
	uart_putchar(a);

}


void uart_putdouble(double data){
	char * a = &data;
	uart_putchar(*(a++));
	uart_putchar(*(a++));
	uart_putchar(*(a++));
	uart_putchar(*a);

}



