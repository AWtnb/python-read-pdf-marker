import pymupdf
import sys
from pathlib import Path


def main(path: str) -> None:
    pdf = pymupdf.Document(path)

    for i in range(pdf.page_count):
        page = pdf[i]
        for annot in page.annots():
            if annot.type[1] == "Highlight":
                rect = annot.rect
                marked = page.get_text(clip=rect)
                print(i + 1, rect, str(marked).strip())

    pdf.close()


if __name__ == "__main__":
    args = sys.argv
    if 1 < len(args):
        p = args[1]
        if Path(p).exists():
            main(p)
