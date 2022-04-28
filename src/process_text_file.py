path = '../text/crypto_com.txt'
path_clean = '../text/crypto_com_clean.txt'
path_processed = '../text/crypto_com_processed.txt'

with open(path, 'r', encoding='mbcs') as f:
    with open(path_clean, 'w', encoding='mbcs') as w:
        for line in f:
            if line.strip():
                w.write(line)

with open(path_clean, encoding='mbcs') as f, open(path_processed, 'w', encoding='mbcs') as f2:
    for line in f:
        line = line.strip()
        if not line or (':' not in line and ',' not in line and len(line) >= 5):
            f2.write(line + '\n')
