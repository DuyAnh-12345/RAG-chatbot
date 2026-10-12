from pathlib import Path

from pypdf import PdfReader


def load_pdf(file_path: Path) -> list[dict]:
    """Extract non-empty pages while preserving source information."""
    reader = PdfReader(file_path)
    documents = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()

        if text:
            documents.append({
                "text": text,
                "source": file_path.name,
                "page": page_number,
            })

    return documents


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    pdf_path = project_root / "data" / "documents" / "sample.pdf"

    if not pdf_path.exists():
        raise SystemExit(f"Add your PDF here first: {pdf_path}")

    documents = load_pdf(pdf_path)
    print(f"Extracted text from {len(documents)} pages.")

    for document in documents[:3]:
        print(f"\n--- Page {document['page']} ---")
        print(document["text"][:500])