def query_agent(query):

    query = query.lower()

    return {

        "luxury":
        "luxury" in query,

        "wedding":
        "wedding" in query,

        "birthday":
        "birthday" in query

    }

# Matching agent
def matching_agent(df, city, budget):

    filtered = df[
        (df['city'].str.lower() == city.lower())
        &
        (df['price'] <= budget)
    ]

    return filtered