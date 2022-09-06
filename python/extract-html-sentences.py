from bs4 import BeautifulSoup
from cgi import test
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

    with open("C:/Users/Marcus/Repositories/orv-analysis/text/extracted-sentences.txt", "a") as output:
        print(f"Loading Chapter {tempNum}...")
        og = open(f"C:/Users/Marcus/Repositories/orv-analysis/extracted EPUB/OEBPS/chap_{tempNum}.xhtml", "r", encoding="UTF8")
        soup = BeautifulSoup(og, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        
        # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # add quotations to the beginning and end of every sentence and replaces " with '
        lines = text.splitlines()
        formatting = ""
        for line in lines:
            tempFormat = line.replace("\u0022","\u0027") # removing this gives a syntaxerror: f-string expression part cannot include a backslash
            formatting += (f'"{tempFormat}"\n')
        text = formatting
        
        print(f"Extracting Chapter {tempNum}...")
        output.writelines(unicodedata.normalize("NFKD", text).encode('ascii', 'ignore').decode('utf8') + "\n")

        print(f"Chapter {str(num)} extracted.")
        num += 1