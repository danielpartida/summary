path = '../text/crypto_com.txt'
path_processed = '../text/crypto_com_clean.txt'

with open(path, 'r', encoding='mbcs') as f:
    with open(path_processed, 'w', encoding='mbcs') as w:
        for line in f:
            if line.strip():
                w.write(line)
