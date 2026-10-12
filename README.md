# Evidence-Based Document Assistant

A personal AI/ML learning project for building a PDF question-answering system with supporting passages and page citations.

## Current implementation

- Extracts text from a PDF using pypdf.
- Preserves the source filename and original page number.
- Skips pages without extractable text.
- Prints previews of the first three non-empty pages.

Retrieval and answer generation are planned; they are not implemented yet.

## Setup

Requires Python 3.9 or later.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdir -p data/documents
```

Place your own text-based PDF at `data/documents/sample.pdf`. PDFs and local environments are excluded from Git. Scanned PDFs require OCR, which is not currently supported.

## Run

```bash
python src/ingest.py
```

## Planned next steps

- Split extracted pages into chunks while preserving metadata.
- Add embeddings and semantic retrieval.
- Evaluate retrieval against questions with known supporting passages.
- Generate answers with evidence and page citations.
