from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import faiss

# Load dataset
df = pd.read_csv("vendors.csv")

# Transformer model
transformer = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

# Vendor descriptions
vendor_descriptions = df['description'].tolist()

# Create embeddings
vendor_embeddings = transformer.encode(
    vendor_descriptions
)

# Convert to numpy
embedding_array = np.array(
    vendor_embeddings
).astype('float32')

# Create FAISS index
index = faiss.IndexFlatL2(
    embedding_array.shape[1]
)

# Store embeddings
index.add(embedding_array)