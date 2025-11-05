import pymupdf
import sys
from pathlib import Path


def main(path: str, href: str) -> None:
    pdf = pymupdf.Document(path)

    for i in range(pdf.page_count):
        page = pdf[i]
        for annot in page.annots():
            if annot.type[1] == "Highlight":
                rect = annot.rect
                marked = page.get_text(clip=rect)
                print(i + 1, rect, str(marked).strip())
                if href:
                    page.insert_link(
                        {
                            "kind": pymupdf.LINK_URI,
                            "from": rect,
                            "uri": href,
                        }
                    )
    if href:
        p = Path(path)
        out_path = p.with_stem(p.stem + "out")
        pdf.save(str(out_path), garbage=3, clean=True, pretty=True)
        pdf.close()


if __name__ == "__main__":
    args = sys.argv
    if 1 < len(args):
        p = args[1]
        if Path(p).exists():
            href = args[2] if 2 < len(args) else ""
            main(p, href)
