import gradio as gr
import asyncio
from rag_handler import initialize_rag, query_rag

rag = asyncio.run(initialize_rag())

def query_rag_wrapper(user_query, history):
    """Wrapper function to pass the RAG object to query_rag."""
    return query_rag(rag, user_query, history)

iface = gr.ChatInterface(
    fn=query_rag_wrapper,
    type='messages',
    title="Witcher Graph RAG Chat",
    description="Ask questions about first Witcher book titled 'The Last Wish' and get AI-generated answers.",
    theme="soft",
    autofocus=False
)

if __name__ == "__main__":
    iface.launch()