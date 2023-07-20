# simple_rc4
Super simple rc4 encryption and decryption

# Requirements:
```
python3.10+
```
# Usage:
Print help
```bash
./simple_rc4.py -h
```
output:
```
usage: simple_rc4.py [-h] [-m MODE] [-t TEXT] [-k KEY]

Options:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  use 'e' to encrypt or 'd' to decrypt a text.
  -t TEXT, --text TEXT  set the text value.
  -k KEY, --key KEY     set the key value.
```
To encrypt a plain text string:
```
./simple_rc4.py -m e -k key -t 'Hello World!'
```
Output:
```
43 09 58 81 4B AF 2C 25 3A 27 6C 5A
```
To decrypt a ciphertext:
```
./simple_rc4.py -m d -k key -t '43 09 58 81 4B AF 2C 25 3A 27 6C 5A'
```
Output:
```
Hello World!
```
If the '-t' or '--text' flag is not provided, the script will read from stdin.

```
echo 'Hello World' | ./simple_rc4.py -m e -k Key
```
Output:
```
A3 FA 1B ED D8 14 9D 1D D5 75 2E 22
```
Or
```
echo 'A3 FA 1B ED D8 14 9D 1D D5 75 2E 22' > test.txt
cat test.txt | ./simple_rc4.py -m d -k Key
```
Output:
```
Hello World
```
Or
```
./simple_rc4.py -m e -k Key <<< 'RC4'
```
Output:
```
B9 DC 43 8B
```

