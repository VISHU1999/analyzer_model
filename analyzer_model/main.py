"""Main file of doc analyzer function"""

import os

from dotenv.main import load_dotenv #pylint: disable=all
from langchain import HuggingFaceHub #pylint: disable=all
from langchain.chains import RetrievalQA #pylint: disable=all
from langchain.document_loaders import PyPDFLoader #pylint: disable=all
from langchain.embeddings import HuggingFaceEmbeddings #pylint: disable=all
from langchain.prompts import PromptTemplate #pylint: disable=all
from langchain.text_splitter import CharacterTextSplitter #pylint: disable=all
from langchain.vectorstores import Chroma #pylint: disable=all

load_dotenv()

model = os.getenv("HUGGINGFACE_MODEL", default="google/flan-t5-base")


def doc_analyzer(file_path: str, question: str):
    """Required two arguments"""
    loader = PyPDFLoader(file_path)
    documents = loader.load_and_split()
    text_splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=5)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings()
    docsearch = Chroma.from_documents(texts, embeddings)

    llm = HuggingFaceHub(
        repo_id=model, model_kwargs={"temperature": 0, "max_length": 712}
    )

    prompt_template = """Act as an Resume expert.
    Analyze the data in the document and answer the following question.
    do a good job in evaluating the person using professional questions. 
    If you don't know the answer, just say that you don't know.

    Act as an Interviewer :{context}

    Question: {question}
    """
    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = {"prompt": prompt}
    query = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=docsearch.as_retriever(search_kwargs={"k": 1}),
        chain_type_kwargs=chain_type_kwargs,
    )

    result = query.run(question)
    return result
