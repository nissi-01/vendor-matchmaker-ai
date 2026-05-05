from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import numpy as np

from embeddings import (
    transformer,
    index
)

from ranking_model import model

from agents import (
    query_agent,
    matching_agent
)

from optimizer import (
    combination_optimizer
)

from rag_engine import (
    explanation_agent
)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load dataset
df = pd.read_csv("vendors.csv")

@app.get("/recommend")

def recommend(
    city: str,
    budget: int,
    query: str
):

    # Query Agent
    query_info = query_agent(query)

    # Matching Agent
    filtered = matching_agent(
        df,
        city,
        budget
    )

    if filtered.empty:

        return {
            "message":
            "No vendors found"
        }

    # ML Ranking
    filtered['predicted_score'] = model.predict(
        filtered[
            ['price', 'rating', 'experience']
        ]
    )

    # Embedding Search
    query_embedding = transformer.encode(
        [query]
    )

    query_vector = np.array(
        query_embedding
    ).astype('float32')

    D, I = index.search(
        query_vector,
        len(filtered)
    )

    similarities = 1 / (1 + D[0])

    filtered['similarity'] = similarities

    # Final score
    filtered['final_score'] = (

        filtered['predicted_score']
        +
        filtered['similarity']

    )

    # Optimizer
    combinations = combination_optimizer(
        filtered,
        budget
    )

    # Explanations
    for combo in combinations:

        combo['reason'] = explanation_agent(
            combo['photographer']
        )

    return {

        "query_analysis":
        query_info,

        "top_combinations":
        combinations

    }