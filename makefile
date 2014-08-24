

#avr-gcc -mmcu=atmega328p -O2 -Wall -o main.elf main.c
#avr-objcopy -O ihex main.elf main.hex

#sudo /home/yifan/Desktop/arduino-1.0.5/hardware/tools/avrdude -C/home/yifan/Desktop/arduino-1.0.5/hardware/tools/avrdude.conf -patmega328p -carduino -P/dev/ttyUSB0 -b57600 -D -Uflash:w:`pwd`/main.hex:i
		


# define useful variables
MMCU = atmega328p
PORT = /dev/ttyUSB0
BAUD = 57600

NAME = main

# define important constants
F_CPU = 16000000UL
BAUD_UART = 9600


# important paths
PATH_AVRDUDE_CONF = /home/yifan/Desktop/arduino-1.0.5/hardware/tools
PATH_AVRDUDE = /home/yifan/Desktop/arduino-1.0.5/hardware/tools
PATH_AVR_GCC = /home/yifan/Desktop/arduino-1.0.5/hardware/tools/avr/bin

AVRDUDE_CONF = $(PATH_AVRDUDE_CONF)/avrdude.conf
AVRDUDE = $(PATH_AVRDUDE)/avrdude


# gcc & avrdude flags 
GCC_FLAG = -mmcu=$(MMCU) -Os -Wall -DF_CPU=$(F_CPU) -DBAUD=$(BAUD_UART) -lm -u,vfprintf -lprintf_min 
AVRDUDE_FLAG = -C$(AVRDUDE_CONF) -p$(MMCU) -carduino -P$(PORT) -b$(BAUD) 


all:	main.hex

main.hex: main.elf
	$(PATH_AVR_GCC)/avr-objcopy -O ihex main.elf main.hex

main.elf: *.c
	$(PATH_AVR_GCC)/avr-gcc $(GCC_FLAG) -o main.elf *.c

upload:	main.hex
	$(AVRDUDE) $(AVRDUDE_FLAG) -F -Uflash:w:$(NAME).hex:i





