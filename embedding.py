import openai
import pandas as pd
import numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity

# Set up API key
openai.api_key = "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"

# Choose a language model
model = "text-embedding-ada-002"




# Define the document sections and weights
# TODO: Import CSV file and format sections from CSV file
cur_prof = {
    "name": {
        "texts": [
            "This is the bio section of the document.",
            "It contains information about the person's background.",
            "There may be multiple sentences in each section.",
        ],
        "weight": 2.0
    },
    "bio": {
        "texts": [
            "These are the publications listed in the document.",
            "They include papers, articles, and books.",
            "Each publication has a title, author, and publication date."
        ],
        "weight": 0.5
    },
    "publications_title": {
        "": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "publications_abstract": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "title": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "awards": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "current_research": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "teaching": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "url": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 0.0
    },
}

# Generate embeddings for each section
section_embeddings = {}
for section_name, section in sections.items():
    section_texts = section["texts"]
    section_weight = section["weight"]
    section_text = " ".join(section_texts)
    section_embedding = openai.Embeddings().embed(model=model, data=section_text)
    section_embeddings[section_name] = {"embedding": section_embedding, "weight": section_weight}


# Combine the embeddings using weighted average
document_embedding = None
for section_name, section in section_embeddings.items():
    section_embedding = section["embedding"]
    section_weight = section["weight"]
    if document_embedding is None:
        document_embedding = section_weight * section_embedding
    else:
        document_embedding += section_weight * section_embedding
        
document_embedding /= sum([section["weight"] for section in section_embeddings.values()])

print(document_embedding)

datafile_path = "data/fine_food_reviews_with_embeddings_1k.csv"
df = pd.read_csv(datafile_path)
df["embedding"] = df.embedding.apply(eval).apply(np.array)

# search through the reviews for a specific product
def search_reviews(df, product_description, n=3):
    product_embedding = get_embedding(
        product_description,
        engine="text-embedding-ada-002"
    )
    df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, product_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
        .combined.str.replace("Title: ", "")
        .str.replace("; Content:", ": ")
    )
    return results



results = search_reviews(df, "delicious beans", n=3)



