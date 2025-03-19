import re
import unicodedata
from pathlib import Path
from pypdf import PdfReader
from lightrag import LightRAG

from config import logger

def clean_text(text: str) -> str:
    """Cleans and normalizes input text."""
    logger.info("Cleaning text") 
    try:
        text = unicodedata.normalize("NFKC", text)
        text = re.sub(r'\s+', ' ', text).strip().lower()
        text = re.sub(r'[^a-zA-Z0-9.,;!?\'"()-]', ' ', text)
        text = re.sub(r'(\w+)-\s+(\w+)', r'\1\2', text)
        return text
    except Exception as e:
        logger.error(f"Error cleaning text: {e}")
        return ""

def extract_text_from_pdf_and_insert(path_to_file: Path, rag: LightRAG) -> None:
    """Extracts, cleans, and inserts text into the RAG model."""
    logger.info(f"Starting text extraction from {path_to_file}")
    
    try:
        reader = PdfReader(path_to_file)
        text_from_pages = []

        for i, page in enumerate(reader.pages):
            extracted_text = page.extract_text()
            if extracted_text:
                logger.info(f"Extracted text from page {i+1}")
                text_from_pages.append(clean_text(extracted_text))
            else:
                logger.warning(f"Page {i+1} has no text")

        logger.info("Finished text extraction and cleaning")
        
        if text_from_pages:
            rag.insert(text_from_pages)
            logger.info("Inserted cleaned text into RAG model")
        else:
            logger.warning("No text extracted; nothing inserted into RAG model")

    except Exception as e:
        logger.error(f"Error processing PDF {path_to_file}: {e}")
