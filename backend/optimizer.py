import pandas as pd

def combination_optimizer(filtered, budget):

    # =========================
    # BUDGET SPLIT
    # =========================

    photo_budget = int(budget * 0.25)

    decor_budget = int(budget * 0.35)

    food_budget = int(budget * 0.40)

    # =========================
    # CATEGORY FILTERS
    # =========================

    photographers = filtered[
        filtered['category'] == "Photographer"
    ]

    decorators = filtered[
        filtered['category'] == "Decorator"
    ]

    caterers = filtered[
        filtered['category'] == "Catering"
    ]

    combinations = []

    # =========================
    # CREATE COMBINATIONS
    # =========================

    for _, p in photographers.iterrows():

        for _, d in decorators.iterrows():

            for _, c in caterers.iterrows():

                total = (

                    int(p['price'])
                    +
                    int(d['price'])
                    +
                    int(c['price'])

                )

                if total <= budget:

                    combinations.append({

                        # Vendors
                        "photographer":
                        p['vendor_name'],

                        "decorator":
                        d['vendor_name'],

                        "caterer":
                        c['vendor_name'],

                        # Prices
                        "photo_price":
                        int(p['price']),

                        "decor_price":
                        int(d['price']),

                        "food_price":
                        int(c['price']),

                        # Budget split
                        "photo_budget":
                        photo_budget,

                        "decor_budget":
                        decor_budget,

                        "food_budget":
                        food_budget,

                        # Total
                        "total_price":
                        total,

                        # Remaining
                        "remaining_budget":
                        int(budget - total)

                    })

    # =========================
    # FALLBACK
    # =========================

    if len(combinations) == 0:

        return [{

            "photographer":
            "No Combination Found",

            "decorator":
            "-",

            "caterer":
            "-",

            "photo_price":
            0,

            "decor_price":
            0,

            "food_price":
            0,

            "photo_budget":
            photo_budget,

            "decor_budget":
            decor_budget,

            "food_budget":
            food_budget,

            "total_price":
            0,

            "remaining_budget":
            budget

        }]

    return combinations[:3]