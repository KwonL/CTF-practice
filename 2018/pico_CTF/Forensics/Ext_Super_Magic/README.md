# Ext super magic 

Given file is data of ext2 system.  by using debugfs, I can recognize it's super block's magic number is corrupted.

offset 1024 + magic number 56 = magic number's address. 

write 0xEF53 and mount it.

`picoCTF{a7DB29eCf7dB9960f0A19Fdde9d00Af0}`