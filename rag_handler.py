from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import openai_embed, gpt_4o_mini_complete
from lightrag.kg.shared_storage import initialize_pipeline_status

from config import WORKING_DIR, logger

async def initialize_rag():
    """Initializes the LightRAG model and storage."""
    logger.info("Initializing RAG model...")

    rag = LightRAG(
        working_dir=WORKING_DIR,
        llm_model_func=gpt_4o_mini_complete,
        embedding_func=openai_embed,
    )

    await rag.initialize_storages()
    await initialize_pipeline_status()

    logger.info("RAG initialization complete.")
    return rag

def query_rag(rag: LightRAG, user_query: str, history: list[dict]) -> str:
    """Handles querying the Graph RAG model."""
    if not user_query.strip():
        logger.warning("User submitted an empty query.")
        return "Please enter a valid query."

    try:
        logger.info(f"Processing query: {user_query.strip()}")
        query_param = QueryParam(
            mode='hybrid', 
            max_token_for_text_unit=1000,  
            max_token_for_global_context=2000, 
            max_token_for_local_context=2000,
            top_k=50
            )
        system_prompt = """ 
        You are a specialized AI assistant trained to answer questions exclusively based on the book The Last Wish by Andrzej Sapkowski.
        You will only provide responses that are grounded in the text available in the dataset. If the requested information is not found within the book, 
        politely inform the user that you cannot answer.
        Do not generate responses based on external knowledge or speculation.
        Do not discuss topics outside of The Last Wish, including later Witcher books, games, TV adaptations, or unrelated subjects.
        Always cite relevant passages when applicable and summarize information accurately.
        If the user asks about something outside your knowledge, respond with:
        "I can only answer questions based on the book The Last Wish. I couldn't find that information in the provided content."
        """
        response = rag.query(user_query.strip(), param=query_param, system_prompt=system_prompt)
        logger.info(f"Query response: {response}")
        return response
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        return "An error occurred while processing your query."
