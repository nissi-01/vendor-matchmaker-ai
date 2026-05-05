async function findVendors(){

    const city =
        document.getElementById("city").value;

    const budget =
        document.getElementById("budget").value;

    const query =
        document.getElementById("query").value;

    const response = await fetch(

        `http://127.0.0.1:8000/recommend?city=${city}&budget=${budget}&query=${query}`

    );

    const data = await response.json();

    let output = "";

    // No vendors
    if(data.message){

        output = `

        <div class="result-card">

            <h2>
                ${data.message}
            </h2>

        </div>

        `;
    }

    else{

        // Query analysis
        output += `

        <div class="query-card">

            <h2>
                Query Understanding Agent
            </h2>

            <p>
                Luxury:
                ${data.query_analysis.luxury}
            </p>

            <p>
                Wedding:
                ${data.query_analysis.wedding}
            </p>

            <p>
                Birthday:
                ${data.query_analysis.birthday}
            </p>

        </div>

        `;

        // Combination cards
        data.top_combinations.forEach(

            (combo, index) => {

                output += `

                <div class="result-card">

                    <h2>
                        Combination ${index + 1}
                    </h2>

                    <p>
                    📸 Photographer:
                    ${combo.photographer}
                    </p>

                    <p>
                    🎨 Decorator:
                    ${combo.decorator}
                    </p>

                    <p>
                    🍽 Caterer:
                    ${combo.caterer}
                    </p>

                    <div class="budget-card">

                        <p>
                        📸 Photography Budget:
                        ₹${combo.photo_budget}
                        </p>

                        <p>
                        📸 Photographer Price:
                        ₹${combo.photo_price}
                        </p>

                        <p>
                        🎨 Decoration Budget:
                        ₹${combo.decor_budget}
                        </p>

                        <p>
                        🎨 Decorator Price:
                        ₹${combo.decor_price}
                        </p>

                        <p>
                        🍽 Catering Budget:
                        ₹${combo.food_budget}
                        </p>

                        <p>
                        🍽 Catering Price:
                        ₹${combo.food_price}
                        </p>

                    </div>

                    <p>
                    💰 Total Price:
                    ₹${combo.total_price}
                    </p>

                    <p>
                    💸 Remaining Budget:
                    ₹${combo.remaining_budget}
                    </p>

                    <p>
                    🤖 AI Reason:
                    ${combo.reason}
                    </p>

                </div>

                `;
            }

        );
    }

    document.getElementById(
        "results"
    ).innerHTML = output;
}