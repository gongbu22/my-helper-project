import chromadb
import uuid

# DB 생성 (로컬에 저장)
client = chromadb.Client()

# 컬렉션 생성 (없으면 자동 생성됨)
collection = client.get_or_create_collection(name="pdf_collection")


def save_to_vector_db(texts: list):
    for text in texts:
        collection.add(
            documents=[text],
            ids=[str(uuid.uuid4())]
        )