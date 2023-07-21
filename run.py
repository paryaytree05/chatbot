import aiml
import requests
from expertsys import recommend_outlet
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config["recommendation_system_on"] = 0
app.config["recommend_system_values"] = {
    "food_style": None,
    "budget": None,
    "location": None,
    "food_type": None,
    "outlet_type": None,
    "check": None,
}
@app.route("/")
def home():
    return render_template("message.html")

def load_aiml_files():
    kernel = aiml.Kernel()
    kernel.learn("std-startup.xml")
    kernel.respond("load aiml b")
    return kernel


def process_user_input(user_input):
    aiml_response = ""
    if not user_input.strip():
        aiml_response = "Don't feel like writing?"
    elif "recommend" in user_input.lower():
        aiml_response = handle_recommendation(user_input)
    elif app.config["recommendation_system_on"] == 1:
        aiml_response = handle_food_style(user_input)
    elif app.config["recommendation_system_on"] == 2:
        aiml_response = handle_budget(user_input)
    elif app.config["recommendation_system_on"] == 3:
        aiml_response = handle_check(user_input)
    elif app.config["recommendation_system_on"] == 4:
        aiml_response = handle_location_food_type(user_input)
    elif app.config["recommendation_system_on"] == 5:
        aiml_response = handle_food_type_outlet_type(user_input)
    elif "weather" in user_input.lower():
        aiml_response = handle_weather(user_input)
    else:
        aiml_response = kernel.respond(user_input)

    return aiml_response


def handle_recommendation(user_input):
    if app.config["recommendation_system_on"] == 0:
        app.config["recommendation_system_on"] += 1
        return "Sure. What do you wish to have (Beverage, Meals, Maggi, Fast-food, Sandwich)?"
    return "Could you please provide an answer to the previous question?"


def handle_food_style(user_input):
    food_style_options = ["beverage", "meals", "maggi", "fast-food", "sandwich"]
    if any(option in user_input.lower() for option in food_style_options):
        app.config["recommend_system_values"]["food_style"] = user_input
        app.config["recommendation_system_on"] += 1
        return kernel.respond(user_input)
    elif "exit" in user_input.lower():
        app.config["recommendation_system_on"] = 0
        return kernel.respond(user_input)
    return "Could you please provide an answer to the previous question?"


def handle_budget(user_input):
    budget_options = ["cheap", "expensive"]
    if any(option in user_input.lower() for option in budget_options):
        app.config["recommend_system_values"]["budget"] = user_input
        app.config["recommendation_system_on"] += 1
        return kernel.respond(user_input)
    elif "exit" in user_input.lower():
        app.config["recommendation_system_on"] = 0
        return kernel.respond(user_input)
    return "Could you please provide an answer to the previous question?"


def handle_check(user_input):
    check_options = ["one", "multiple"]
    if any(option in user_input.lower() for option in check_options):
        app.config["recommend_system_values"]["check"] = user_input
        app.config["recommendation_system_on"] += 1
        return kernel.respond(user_input)
    elif "exit" in user_input.lower():
        app.config["recommendation_system_on"] = 0
        return kernel.respond(user_input)
    return "Could you please provide an answer to the previous question?"


def handle_location_food_type(user_input):
    if app.config["recommend_system_values"]["check"] == "one":
        location_options = ["mess-1", "mess-2", "academic-blocks"]
        if any(option in user_input.lower() for option in location_options):
            app.config["recommend_system_values"]["location"] = user_input
            app.config["recommendation_system_on"] += 1
            return kernel.respond(user_input)
    elif app.config["recommend_system_values"]["check"] == "multiple":
        food_type_options = ["vegetarian", "non-vegetarian"]
        if any(option in user_input.lower() for option in food_type_options):
            app.config["recommend_system_values"]["food_type"] = user_input
            app.config["recommendation_system_on"] += 1
            return kernel.respond(user_input)
    elif "exit" in user_input.lower():
        app.config["recommendation_system_on"] = 0
        return kernel.respond(user_input)
    return "Could you please provide an answer to the previous question?"


def handle_food_type_outlet_type(user_input):
    if app.config["recommend_system_values"]["check"] == "one":
        food_type_options = ["vegetarian", "non-vegetarian"]
        if any(option in user_input.lower() for option in food_type_options):
            app.config["recommend_system_values"]["food_type"] = user_input
            app.config["recommendation_system_on"] += 1
            return kernel.respond(user_input)
    elif app.config["recommend_system_values"]["check"] == "multiple":
        outlet_type_options = ["sit-down", "takeaway"]
        if any(option in user_input.lower() for option in outlet_type_options):
            app.config["recommend_system_values"]["outlet_type"] = user_input
            app.config["recommendation_system_on"] = 0
            return recommend_outlet(
                app.config["recommend_system_values"]["food_style"],
                app.config["recommend_system_values"]["location"],
                app.config["recommend_system_values"]["budget"],
                app.config["recommend_system_values"]["food_type"],
                app.config["recommend_system_values"]["outlet_type"],
                app.config["recommend_system_values"]["check"],
            )
    elif "exit" in user_input.lower():
        app.config["recommendation_system_on"] = 0
        return kernel.respond(user_input)
    return "Could you please provide an answer to the previous question?"


def handle_weather(user_input):
    app.config["recommendation_system_on"] = 0
    city = user_input.replace("weather", "").strip()
    weather = get_weather(city)
    temp = weather["temp"]
    humidity = weather["humidity"]
    conditions = weather["conditions"]
    return (
        f"The Temperature in {city} is {temp}°C, humidity is {humidity}% "
        f"and the conditions are {conditions}"
    )


def get_weather(city):
    api_key = "e1e2b866e6b4202b06ab18c39542e37e"  # Replace with your OpenWeatherMap API key

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "conditions": data["weather"][0]["description"],
    }

    return weather


kernel = load_aiml_files()


@app.route("/chat", methods=["POST"])
def chatbot():
    user_message = request.form["message"]
    chatbot_response = process_user_input(user_message)



    return chatbot_response


if __name__ == "__main__":
    app.run(debug=True)


