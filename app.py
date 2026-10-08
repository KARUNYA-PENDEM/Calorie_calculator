import streamlit as st
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="LEVEL UP - Smart Daily Energy Guide",
    page_icon="🥗",
    layout="wide"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, #173b2c 0%, transparent 35%),
        radial-gradient(circle at bottom right, #163b3d 0%, transparent 35%),
        #071410;
    color: #f5fff9;
}

.main-title {
    text-align: center;
    font-size: 54px;
    font-weight: 900;
    margin-top: 10px;
    margin-bottom: 5px;
    background: linear-gradient(90deg, #7CFFB2, #C9FF75, #6EE7D8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #b9cfc4;
    font-size: 18px;
    margin-bottom: 28px;
}

.hero {
    padding: 32px;
    border-radius: 26px;
    background: linear-gradient(
        135deg,
        rgba(25, 65, 48, 0.95),
        rgba(11, 31, 26, 0.95)
    );
    border: 1px solid #315d49;
    margin-bottom: 28px;
}

.hero h2 {
    font-size: 32px;
    margin-bottom: 8px;
}

.hero p {
    color: #c1d6cb;
    font-size: 17px;
}

.section-title {
    font-size: 29px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 18px;
}

.card {
    background: rgba(17, 38, 30, 0.9);
    border: 1px solid #294b3b;
    border-radius: 20px;
    padding: 22px;
    margin-bottom: 18px;
}

.energy-number {
    font-size: 42px;
    font-weight: 900;
    color: #9AFFC0;
}

.energy-label {
    color: #a9c4b5;
    font-size: 14px;
}

.result-card {
    background: linear-gradient(
        135deg,
        #143e2b,
        #0e2920
    );
    border: 1px solid #3e7658;
    border-radius: 24px;
    padding: 30px;
    text-align: center;
}

.tip {
    background: #10271f;
    border-left: 4px solid #7CFFB2;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 12px;
}

.warning {
    background: #302a15;
    border-left: 4px solid #e8c85b;
    padding: 15px;
    border-radius: 10px;
}

.footer {
    text-align: center;
    color: #789487;
    padding: 25px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION STATE
# ============================================================

if "calculated" not in st.session_state:
    st.session_state.calculated = False

if "result" not in st.session_state:
    st.session_state.result = None

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🥗 LEVEL UP")

    st.caption("Smart Daily Energy Guide")

    st.divider()

    page = st.radio(
        "Navigate",
        [
            "🏠 Home",
            "⚡ Energy Calculator",
            "🌱 Wellness Guide",
            "ℹ️ About"
        ]
    )

    st.divider()

    st.markdown("### 🌍 Our Idea")

    st.write(
        "Help people understand their everyday energy needs "
        "without turning health into a competition."
    )

    st.divider()

    st.caption(
        "Educational estimates only. "
        "Not a medical diagnosis or treatment."
    )

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🥗 LEVEL UP</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Smart Daily Energy Guide • Simple • Inclusive • Human'
    '</div>',
    unsafe_allow_html=True
)

# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h2>🌱 Understand your energy. Improve your habits.</h2>
        <p>
        NOURISH gives you a simple estimate of your daily energy
        requirement and turns the number into practical,
        easy-to-understand wellness guidance.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### ⚡ Energy")
        st.write(
            "Understand approximately how much energy your body "
            "may use during a normal day."
        )

    with col2:
        st.markdown("### 🧠 Awareness")
        st.write(
            "Learn what activity, age and body measurements "
            "can contribute to energy requirements."
        )

    with col3:
        st.markdown("### 🌱 Small Steps")
        st.write(
            "Get simple suggestions for balanced meals, movement, "
            "hydration and rest."
        )

    st.markdown(
        '<div class="section-title">💚 Why LEVEL UP?</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

        <h3>🚫 Not another diet calculator</h3>

        <p>
        Numbers can be useful, but health is more than a number.
        NOURISH focuses on energy, nourishment, activity and
        everyday habits.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">

        <h3>🌍 Designed for everyone</h3>

        <p>
        The interface is simple enough for students, parents,
        working people and beginners to understand.
        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">✨ What you can discover</div>',
        unsafe_allow_html=True
    )

    discovery_cols = st.columns(4)

    discoveries = [
        ("⚡", "Energy Need", "Estimated daily energy requirement"),
        ("🔥", "Resting Energy", "Approximate resting energy use"),
        ("🏃", "Activity", "How movement changes requirements"),
        ("💧", "Hydration", "Simple hydration awareness")
    ]

    for col, item in zip(discovery_cols, discoveries):

        with col:

            st.markdown(
                f"""
                <div class="card" style="text-align:center;">
                    <div style="font-size:35px;">{item[0]}</div>
                    <h4>{item[1]}</h4>
                    <p style="color:#9eb8aa;">
                        {item[2]}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.info(
        "💡 Start with the Energy Calculator from the sidebar."
    )

# ============================================================
# CALCULATOR
# ============================================================

elif page == "⚡ Energy Calculator":

    st.markdown(
        '<div class="section-title">⚡ Your Daily Energy Estimate</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Enter a few basic details. NOURISH will provide an "
        "approximate daily energy estimate."
    )

    st.markdown(
        """
        <div class="warning">
        <b>Important:</b> This calculator is intended as a general
        educational tool. Energy needs vary between people and can
        change because of health conditions, medications, growth,
        pregnancy, recovery and many other factors.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 👤 Step 1 — Basic Details")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=13,
            max_value=100,
            value=25,
            step=1
        )

        sex = st.selectbox(
            "Sex used for the equation",
            [
                "Male",
                "Female"
            ]
        )

    with col2:

        height = st.number_input(
            "Height (cm)",
            min_value=100.0,
            max_value=230.0,
            value=170.0,
            step=0.5
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=30.0,
            max_value=250.0,
            value=65.0,
            step=0.5
        )

    st.markdown("### 🏃 Step 2 — Your Typical Activity")

    activity = st.selectbox(
        "Choose the description that feels closest to your normal routine",
        [
            "Mostly sitting / very little planned activity",
            "Light activity — walking or light exercise",
            "Moderate activity — regular exercise",
            "High activity — frequent training or active work",
            "Very high activity — intense training / highly active work"
        ]
    )

    activity_factors = {
        "Mostly sitting / very little planned activity": 1.20,
        "Light activity — walking or light exercise": 1.375,
        "Moderate activity — regular exercise": 1.55,
        "High activity — frequent training or active work": 1.725,
        "Very high activity — intense training / highly active work": 1.90
    }

    st.markdown("### 🌱 Step 3 — What are you looking for?")

    goal = st.selectbox(
        "Choose your main focus",
        [
            "Understand my daily energy needs",
            "Build healthier daily habits",
            "Support my regular training",
            "Improve my meal awareness"
        ]
    )

    st.markdown("### 🍽️ Optional")

    food_preference = st.selectbox(
        "Preferred eating style",
        [
            "No preference",
            "Vegetarian",
            "Vegan",
            "High-protein preference",
            "Traditional home-style meals"
        ]
    )

    st.write("")

    calculate = st.button(
        "⚡ CALCULATE MY ENERGY NEED",
        type="primary",
        use_container_width=True
    )

    if calculate:

        # ----------------------------------------------------
        # AGE SAFETY
        # ----------------------------------------------------

        if age < 18:

            st.warning(
                "Because people under 18 are still growing, adult "
                "calorie equations are not appropriate for giving "
                "a personalized calorie target. Please discuss "
                "nutrition and energy needs with a parent/guardian "
                "and a qualified healthcare professional."
            )

            st.session_state.calculated = False

        else:

            # ------------------------------------------------
            # Mifflin-St Jeor BMR
            # ------------------------------------------------

            if sex == "Male":

                bmr = (
                    10 * weight
                    + 6.25 * height
                    - 5 * age
                    + 5
                )

            else:

                bmr = (
                    10 * weight
                    + 6.25 * height
                    - 5 * age
                    - 161
                )

            activity_factor = activity_factors[activity]

            daily_energy = bmr * activity_factor

            # Simple hydration awareness estimate.
            # Presented as a rough educational guide, not a prescription.
            hydration_ml = weight * 30

            st.session_state.result = {
                "bmr": bmr,
                "daily_energy": daily_energy,
                "hydration": hydration_ml,
                "goal": goal,
                "food_preference": food_preference,
                "activity": activity
            }

            st.session_state.calculated = True

    # ========================================================
    # RESULTS
    # ========================================================

    if st.session_state.calculated:

        result = st.session_state.result

        st.markdown("---")

        st.markdown(
            '<div class="section-title">✨ Your NOURISH Result</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="result-card">

                <div class="energy-label">
                    ESTIMATED DAILY ENERGY REQUIREMENT
                </div>

                <div class="energy-number">
                    {result["daily_energy"]:,.0f} kcal/day
                </div>

                <p style="color:#b5cfc0;">
                    This is an estimate of the energy your body may
                    require on a typical day based on the information
                    you entered.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                f"""
                <div class="card" style="text-align:center;">
                    <div style="font-size:30px;">🔥</div>
                    <h3>Resting Energy</h3>
                    <div class="energy-number"
                         style="font-size:30px;">
                        {result["bmr"]:,.0f}
                    </div>
                    <p class="energy-label">
                        kcal/day estimate
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div class="card" style="text-align:center;">
                    <div style="font-size:30px;">🏃</div>
                    <h3>Activity Level</h3>
                    <p style="color:#9fc0ad;">
                        {result["activity"]}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            st.markdown(
                f"""
                <div class="card" style="text-align:center;">
                    <div style="font-size:30px;">💧</div>
                    <h3>Hydration Awareness</h3>
                    <div class="energy-number"
                         style="font-size:30px;">
                        {result["hydration"]:,.0f} ml
                    </div>
                    <p class="energy-label">
                        rough daily fluid reference
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        # ----------------------------------------------------
        # INTERPRETATION
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">🧠 What does this mean?</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="card">

            <h3>🌱 Your result in simple words</h3>

            <p>
            Your estimated daily energy requirement is around
            <b>{result["daily_energy"]:,.0f} kcal per day</b>.
            This is not a perfect number — it is a starting estimate.
            Real energy needs can change from day to day.
            </p>

            <p>
            Your result considers your age, height, weight and
            typical activity level.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # PERSONALIZED WELLNESS MESSAGE
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">🌿 Your Wellness Guide</div>',
            unsafe_allow_html=True
        )

        if result["goal"] == "Understand my daily energy needs":

            message = (
                "Use this number as general awareness rather than "
                "a strict daily target. Your body's needs naturally "
                "change with activity, sleep and routine."
            )

        elif result["goal"] == "Build healthier daily habits":

            message = (
                "Focus on consistency rather than perfection. "
                "Regular meals, enough sleep, hydration and enjoyable "
                "movement can all support everyday wellbeing."
            )

        elif result["goal"] == "Support my regular training":

            message = (
                "Training days can require more energy than rest days. "
                "Regular meals containing carbohydrates, protein, "
                "healthy fats and fluids can support active lifestyles."
            )

        else:

            message = (
                "Calorie numbers are only one part of nutrition. "
                "Food quality, variety, protein, fibre, fluids and "
                "overall eating patterns also matter."
            )

        st.markdown(
            f"""
            <div class="tip">
                <b>💚 {message}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # SMART DAILY TIPS
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">🌍 Small Things That Matter</div>',
            unsafe_allow_html=True
        )

        tips = [
            (
                "🥗",
                "Build balanced meals",
                "Try including vegetables or fruit, a protein source, "
                "a carbohydrate source and some healthy fats."
            ),
            (
                "💧",
                "Stay hydrated",
                "Keep water available throughout the day and drink "
                "according to thirst and your environment."
            ),
            (
                "🚶",
                "Move regularly",
                "Short walks and regular movement during the day "
                "can be valuable even without intense exercise."
            ),
            (
                "😴",
                "Respect recovery",
                "Good sleep and rest are important parts of a healthy routine."
            )
        ]

        for icon, title, description in tips:

            st.markdown(
                f"""
                <div class="tip">
                    <h4>{icon} {title}</h4>
                    <span style="color:#b3c8bc;">
                        {description}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

        # ----------------------------------------------------
        # FOOD PREFERENCE
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">🍽️ Your Food Preference</div>',
            unsafe_allow_html=True
        )

        preference_messages = {

            "No preference":
                "Aim for variety across your meals and include different food groups.",

            "Vegetarian":
                "Include varied protein sources such as pulses, beans, dairy or suitable alternatives.",

            "Vegan":
                "Include varied plant proteins and pay attention to nutrients such as vitamin B12, iron and calcium.",

            "High-protein preference":
                "Spread protein-containing foods across meals instead of relying on one large serving.",

            "Traditional home-style meals":
                "Home-cooked meals can be a great foundation. Aim for variety and balanced portions."
        }

        st.info(
            preference_messages[result["food_preference"]]
        )

        # ----------------------------------------------------
        # DISCLAIMER
        # ----------------------------------------------------

        st.markdown("---")

        st.markdown(
            """
            <div class="warning">

            <b>⚠️ Remember:</b>

            This calculator provides an estimate, not a medical
            prescription. Calorie requirements vary considerably
            between individuals.

            If you are pregnant, breastfeeding, under 18, have a
            medical condition, have specific nutritional needs, or
            are concerned about eating or weight, speak with a
            qualified healthcare professional.

            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# WELLNESS GUIDE
# ============================================================

elif page == "🌱 Wellness Guide":

    st.markdown(
        '<div class="section-title">🌱 Everyday Wellness Guide</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Health doesn't have to mean complicated routines."
    )

    areas = [
        (
            "🥗",
            "Food",
            "Think about variety rather than perfection. "
            "Different fruits, vegetables, grains, proteins and "
            "healthy fats can contribute different nutrients."
        ),
        (
            "💧",
            "Hydration",
            "Water needs vary between people. Weather, activity, "
            "food and individual needs can all affect hydration."
        ),
        (
            "🚶",
            "Movement",
            "Walking, sports, cycling, stretching, dancing and "
            "exercise can all be forms of movement."
        ),
        (
            "😴",
            "Sleep",
            "Rest is part of health. A consistent sleep routine "
            "can support energy and concentration."
        ),
        (
            "🧠",
            "Mental Wellbeing",
            "Stress management, social connection and taking breaks "
            "are important parts of overall wellbeing."
        ),
        (
            "🌍",
            "Consistency",
            "Small habits repeated over time are often easier to "
            "maintain than extreme short-term changes."
        )
    ]

    for i in range(0, len(areas), 2):

        col1, col2 = st.columns(2)

        for col, area in zip(
            [col1, col2],
            areas[i:i + 2]
        ):

            with col:

                st.markdown(
                    f"""
                    <div class="card">

                    <div style="font-size:38px;">
                        {area[0]}
                    </div>

                    <h3>{area[1]}</h3>

                    <p style="color:#b4cabe;">
                        {area[2]}
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.success(
        "🌱 Better health is not about being perfect. "
        "It is about making supportive choices consistently."
    )

# ============================================================
# ABOUT
# ============================================================

elif page == "ℹ️ About":

    st.markdown(
        '<div class="section-title">ℹ️ About NOURISH</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    <h2>🌱 The idea behind NOURISH</h2>

    <p>
    Many health applications focus heavily on numbers, weight
    and restrictions. NOURISH takes a different approach.
    </p>

    <p>
    The goal is to help people understand their approximate
    energy requirements while encouraging balanced nutrition,
    movement, hydration, sleep and wellbeing.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🧮 How the calculator works</div>',
        unsafe_allow_html=True
    )

    st.info(
        "NOURISH uses the Mifflin-St Jeor equation to estimate "
        "Basal Metabolic Rate (BMR), then applies an activity "
        "factor to estimate daily energy expenditure."
    )

    st.markdown("""
    ### 🔥 BMR

    **Basal Metabolic Rate** is an estimate of the energy your
    body uses for basic physiological functions while at rest.

    ### 🏃 Activity

    Your normal activity level is then used to estimate how much
    additional energy your everyday routine may require.

    ### 📊 Final Estimate

    The result is an approximate daily energy requirement.

    It should **not** be treated as an exact number.
    """)

    st.markdown(
        '<div class="section-title">🌍 Our Social Message</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero">

    <h2>💚 Health is more than a number.</h2>

    <p>
    Eat with awareness.<br>
    Move in ways you enjoy.<br>
    Rest when your body needs it.<br>
    Take care of your mind.<br>
    Support the people around you.
    </p>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    f"""
    <div class="footer">
        🥗 <b>NOURISH</b> — Smart Daily Energy Guide<br>
        <small>
        Educational wellness project • Built with Python + Streamlit
        </small>
        <br><br>
        <small>
        © {datetime.now().year} NOURISH
        </small>
    </div>
    """,
    unsafe_allow_html=True
)