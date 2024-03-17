import html2text
import unicodedata

num = 1
print("Generating Chapter...")
while num < 552:
    numLength = len(str(num))
    tempNum = "0"
    if numLength == 1:
        tempNum = "0000" + str(num)
    elif numLength == 2:
        tempNum = "000" + str(num)
    elif numLength == 3:
        tempNum = "00" + str(num)

    with open("text/extracted-unicode.txt", "a", encoding="utf8") as output:
        print("Loading Chapter " + tempNum + "...")
        og = open("extracted EPUB/OEBPS/chap_" + tempNum + ".xhtml", "r", encoding="UTF8")
        handler = html2text.HTML2Text()
        handler.ignore_links = True
        handler.unicode_snob = True
        handler.ignore_images = True
        handler.escape_snob = True
        handler.unifiable = True
        handler.body_width = 0

        print("Extracting Chapter " + tempNum + "...")
        text = handler.handle(og.read())
        extracted = unicodedata.normalize("NFKD", text).encode('utf8').decode('utf8')
        extracted = extracted.replace("\n\n", "\n")
        # print(extracted)
        extracted = extracted.replace("「", "「")
        extracted = extracted.replace("」", "」")
        extracted = extracted.replace("\\", "")
        extracted = extracted.replace("–", "-")

        output.writelines(extracted + "\n\n")

        print("Chapter " + str(num) + " extracted.")
        num += 1