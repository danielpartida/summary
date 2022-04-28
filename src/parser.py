import fitz  # this is pymupdf

with fitz.open("../whitepapers/crypto_com.pdf") as doc:
    text = ""

    metadata = doc.metadata
    number_pages = doc.page_count

    # TODO: Handle text extracting blocks
    # https://pymupdf.readthedocs.io/en/latest/tutorial.html#importing-the-bindings
    for page in doc:
        text += page.get_text()

with open("../text/crypto_com.txt", "w", encoding="utf8") as output:
    output.write(text)

output.close()
