from pathlib import Path

import chromadb
from langchain_community.vectorstores.chroma import Chroma

from bot.memory.vector_memory import initialize_embedding, VectorMemory, similarity_search, search_most_similar_doc

if __name__ == "__main__":
    root_folder = Path(__file__).resolve().parent.parent
    # Contains an extract of documents uploaded to the RAG bot;
    declarative_vector_store_path = root_folder / "vector_store" / "docs_index"
    # Contains an extract of things the user said in the past;
    episodic_vector_store_path = root_folder / "vector_store" / "episodic_index"

    embedding = initialize_embedding()
    memory = VectorMemory(embedding=embedding)
    index = memory.load_memory_index(str(declarative_vector_store_path))

    # query = "<write_your_query_here>"
    query = "tell me a joke about ClearML"

    matched_docs, sources = similarity_search(query, index)
    matched_doc = search_most_similar_doc(query, index)

    docs = index.similarity_search(query=query, k=4)

    for doc in docs:
        print("-- PAGE CONTENT --")
        print(doc.page_content)
        print("-- METADATA --")
        print(doc.metadata)

    persistent_client = chromadb.PersistentClient(path=str(episodic_vector_store_path))
    collection = persistent_client.get_or_create_collection("episodic_memory")
    collection.add(ids=["1", "2", "3"], documents=["a", "b", "c"])
    langchain_chroma = Chroma(
        client=persistent_client,
        collection_name="episodic_memory",
        embedding_function=embedding,
    )
    s = langchain_chroma.similarity_search("a")
