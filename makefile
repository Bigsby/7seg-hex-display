DEVICE=CAT28C16A
rom.bin:
	py makerom.py

burn: rom.bin
	minipro -p $(DEVICE) -w $@

read:
	minipro -p $(DEVICE) -r content.bin
	hexdump -C content.bin

clean:
	rm rom.bin
	rm content.bin
