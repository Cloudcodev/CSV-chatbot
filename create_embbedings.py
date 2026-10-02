# generates and saves vector embeddings for the product catalog descriptions.

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def generate_embeddings(csv_path="sample_products.csv", output_path="product_embeddings.npy"):
    print(f"Loading data from {csv_path}...")
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: '{csv_path}' not found. Please run your data generation script first.")
        return

    print("Loading embedding model (all-MiniLM-L6-v2)...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    descriptions = df["description"].tolist()
    print(f"Generating embeddings for {len(descriptions)} products...")
    
    # encode descriptions into vectors
    embeddings = model.encode(descriptions)
    
    np.save(output_path, embeddings)
    print(f"Successfully saved embeddings to {output_path}")

    # displaying validation statistics
    print("\n Embedding Stats ")
    print(f"Matrix shape: {embeddings.shape} (Records x Dimensions)")
    
    if len(embeddings) >= 2:
        # Calculate cosine similarity between the first two products as a sanity check
        sim_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
        print(f"Similarity score between Product 1 and 2: {sim_score:.3f}")

if __name__ == "__main__":
    generate_embeddings() 
