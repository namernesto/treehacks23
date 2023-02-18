
from openai.embeddings_utils import get_embedding, cosine_similarity

# search through the reviews for a specific product
def search_profs(df, query, n=20, pprint=True):
    product_embedding = get_embedding(
        query,
        engine="text-embedding-ada-002"
    )
    df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, product_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
        .combined.str.replace("Title: ", "")
        .str.replace("; Content:", ": ")
    )
    if pprint:
        for r in results:
            print(r[:200])
            print()
    return results


results = search_profs(df, "delicious beans", n=20)