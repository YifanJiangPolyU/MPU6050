#include <inttypes.h>
#include <stdint.h>
#include <avr/io.h>
#include <util/setbaud.h>


// initialize UART
void uart_init();

void uart_putchar(char data);

char uart_getchar(void);

void uart_putstring(char * s);

//send int16 as 2 chars
//care needed on PC side
void uart_putint16(int16_t data);

//send double as 8 chars
//care needed on PC side
void uart_putdouble(double data);
