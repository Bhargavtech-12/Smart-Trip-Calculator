import streamlit as st

st.set_page_config(
    page_title="Smart Trip Calculator",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ Smart Trip Calculator")
st.subheader("AI-Based Travel Budget Planner")

st.write("Plan your trip and calculate your travel expenses!")

st.divider()

# User Details
st.header("🌍 Trip Details")

source = st.text_input("Starting Location")
destination = st.text_input("Destination")

persons = st.number_input(
    "Number of Persons", min_value=1, max_value=20, value=2
)

days = st.number_input(
    "Number of Days", min_value=1, max_value=30, value=2
)

travel = st.selectbox(
    "Travel Mode",
    ["Bus", "Train", "Car", "Flight"]
)

hotel = st.selectbox(
    "Hotel Type",
    ["Budget", "Standard", "Luxury"]
)

st.divider()

# Calculate Budget
if st.button("Calculate Trip Budget"):

    if source.strip() == "" or destination.strip() == "":
        st.error("Please enter starting location and destination!")

    else:
        travel_cost = {
            "Bus": 1000,
            "Train": 1500,
            "Car": 3000,
            "Flight": 5000
        }

        hotel_cost = {
            "Budget": 800,
            "Standard": 1500,
            "Luxury": 3000
        }

        transport = travel_cost[travel] * persons
        hotel_expense = hotel_cost[hotel] * days
        food = 400 * persons * days
        sightseeing = 300 * persons * days
        other = 200 * persons * days

        total = (
            transport + hotel_expense +
            food + sightseeing + other
        )

        st.success("Your Trip Budget is Ready! 🎉")

        st.write("📍 From:", source)
        st.write("📍 To:", destination)

        st.subheader("💰 Expense Details")

        st.write("🚌 Transportation: ₹", transport)
        st.write("🏨 Hotel: ₹", hotel_expense)
        st.write("🍔 Food: ₹", food)
        st.write("🎡 Sightseeing: ₹", sightseeing)
        st.write("🛍️ Other Expenses: ₹", other)

        st.divider()

        st.subheader(f"Total Budget: ₹{total:,}")

        st.info(
            f"Per Person Cost: ₹{total // persons:,}"
        )

        st.balloons()

        st.success("Have a Safe and Happy Journey! ✈️")
