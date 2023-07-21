import threading
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, outlet, serves_veg, serves_non_veg, Beverages, Maggi, Meals, fast_food, sandwich, Mess1, Mess2, acads, cheap, expensive, afternoon, evening, night, sit_down, takeaway, smart_campus')

# Define the rules and facts
+outlet('Bitsian Pleasant')
+outlet('Agra Chat')
+outlet('Fruitful')
+outlet('Hotspot')
+outlet('Amul')
+outlet('Vijay-Vahini')
+outlet('Yummpys')
+outlet('Diamond Eatery')
+outlet('Chipotle')
+outlet('Wich Please')
+outlet('SFC')
+outlet('Cafeteria')
+outlet('CCD')
+outlet('Mess 1 Juice Shop')
+outlet('Mess 1 Burger Shop')
+outlet('Mess 2 Juice Shop')
+outlet('ANC-1')
+outlet('ANC-2')

+serves_veg('Bitsian Pleasant')
+serves_veg('Agra Chat')
+serves_veg('Fruitful')
+serves_veg('Hotspot')
+serves_veg('Amul')
+serves_veg('Vijay-Vahini')
+serves_veg('Yummpys')
+serves_veg('Diamond Eatery')
+serves_veg('Chipotle')
+serves_veg('Wich Please')
+serves_veg('SFC')
+serves_veg('Cafeteria')
+serves_veg('CCD')
+serves_veg('Mess 1 Juice Shop')
+serves_veg('Mess 1 Burger Shop')
+serves_veg('Mess 2 Juice Shop')
+serves_veg('ANC-1')
+serves_veg('ANC-2')

+serves_non_veg('Bitsian Pleasant')
+serves_non_veg('Fruitful')
+serves_non_veg('Hotspot')
+serves_non_veg('Amul')
+serves_non_veg('Vijay-Vahini')
+serves_non_veg('Yummpys')
+serves_non_veg('Chipotle')
+serves_non_veg('SFC')
+serves_non_veg('Cafeteria')
+serves_non_veg('Mess 1 Burger Shop')
+serves_non_veg('ANC-1')
+serves_non_veg('ANC-2')

+Beverages('Amul')
+Beverages('Fruitful')
+Beverages('Mess 1 Juice Shop')
+Beverages('Mess 2 Juice Shop')
+Beverages('CCD')

+Maggi('Yummpys')
+Maggi('Hotspot')
+Maggi('Wich Please')

+Meals('Chipotle')
+Meals('Hotspot')
+Meals('ANC-1')
+Meals('ANC-2')
+Meals('Cafeteria')

+fast_food('SFC')
+fast_food('Fruitful')
+fast_food('Mess 1 Burger Shop')
+fast_food('ANC-1')
+fast_food('ANC-2')

+sandwich('Wich Please')
+sandwich('Yummpys')
+sandwich('Cafeteria')

+Mess1('Bitsian Pleasant')
+Mess1('Agra Chat')
+Mess1('Fruitful')
+Mess1('Hotspot')
+Mess1('Amul')
+Mess1('Vijay-Vahini')
+Mess1('Yummpys')
+Mess1('Diamond Eatery')
+Mess1('Chipotle')
+Mess2('Wich Please')
+Mess2('SFC')
+acads('Cafeteria')
+acads('CCD')
+Mess1('Mess 1 Juice Shop')
+Mess1('Mess 1 Burger Shop')
+Mess2('Mess 2 Juice Shop')
+Mess1('ANC-1')
+Mess2('ANC-2')

+cheap('Agra Chat')
+cheap('Hotspot')
+cheap('Amul')
+cheap('Vijay-Vahini')
+cheap('Yummpys')
+cheap('Chipotle')
+cheap('Wich Please')
+cheap('SFC')
+cheap('Cafeteria')
+cheap('Mess 1 Juice Shop')
+cheap('Mess 1 Burger Shop')
+cheap('Mess 2 Juice Shop')
+cheap('ANC-1')
+cheap('ANC-2')

+expensive('Bitsian Pleasant')
+expensive('Fruitful')
+expensive('Diamond Eatery')

+afternoon('Agra Chat')
+afternoon('Fruitful')
+afternoon('Hotspot')
+afternoon('Amul')
+afternoon('Vijay-Vahini')
+afternoon('Yummpys')
+afternoon('Chipotle')
+afternoon('Cafeteria')
+afternoon('Mess 1 Juice Shop')
+afternoon('Mess 2 Juice Shop')

+evening('Bitsian Pleasant')
+evening('Fruitful')
+evening('Hotspot')
+evening('Amul')
+evening('Vijay-Vahini')
+evening('Yummpys')
+evening('Chipotle')
+evening('Wich Please')
+evening('SFC')

+night('Yummpys')
+night('Wich Please')
+night('SFC')
+night('Mess 1 Juice Shop')
+night('Mess 1 Burger Shop')
+night('Mess 2 Juice Shop')

+sit_down('Bitsian Pleasant')
+sit_down('Agra Chat')
+sit_down('Fruitful')
+sit_down('Hotspot')
+sit_down('Amul')
+sit_down('Vijay-Vahini')
+sit_down('Yummpys')
+sit_down('Diamond Eatery')
+sit_down('Chipotle')
+sit_down('Wich Please')
+sit_down('SFC')
+sit_down('Cafeteria')

+takeaway('Bitsian Pleasant')
+takeaway('Fruitful')
+takeaway('Hotspot')
+takeaway('Amul')
+takeaway('Vijay-Vahini')
+takeaway('Yummpys')
+takeaway('Chipotle')
+takeaway('SFC')
+takeaway('Cafeteria')
+takeaway('Mess 1 Juice Shop')
+takeaway('Mess 2 Juice Shop')

+smart_campus('Mess 1 Juice Shop')
+smart_campus('Mess 2 Juice Shop')
+smart_campus('Mess 1 Burger Shop')
+smart_campus('ANC-1')
+smart_campus('ANC-2')


def recommend_outlet(food_style= None, budget=None, location=None, food_type=None, outlet_type=None, payment_option=None, multiple=False):
    pyDatalog.pyEngine.Thread_local_variables = threading.local()
    results = outlet(X)

    # Filter by food style
    if food_style == 'Beverage':
        results = results & Beverages(X)
    elif food_style == 'Maggi':
        results = results & Maggi(X)
    elif food_style == 'Meals':
        results = results & Meals(X)
    elif food_style == 'fast-food':
        results = results & fast_food(X)
    elif food_style == 'sandwich':
        results = results & sandwich(X)
    else:
        return "Invalid food style."

    # Filter by budget
    if budget == 'cheap':
        results = results & cheap(X)
    elif budget == 'expensive':
        results = results & expensive(X)
    else:
        return "Invalid budget."

    # Filter by location
    if location:
        if location == 'Mess-1':
            results = results & Mess1(X)
        elif location == 'Mess-2':
            results = results & Mess2(X)
        elif location == 'academic-blocks':
            results = results & acads(X)
        else:
            return "Invalid location."

    # Filter by food type
    if food_type:
        if food_type == 'Vegetarian':
            results = results & serves_veg(X)
        elif food_type == 'Non-Vegetarian':
            results = results & serves_non_veg(X)
        else:
            return "Invalid food type."

    # Filter by outlet type
    if outlet_type:
        if outlet_type == 'sit-down':
            results = results & sit_down(X)
        elif outlet_type == 'takeaway':
            results = results & takeaway(X)
        else:
            return "Invalid outlet type."

    # Filter by smart campus
    if payment_option is not None: 
        results = results & smart_campus(X)

    # Create the recommended outlet string
    if len(results) == 0:
        return "Sorry, I couldn't find a restaurant matching your preferences."
    else:
        if multiple:
            recommendations_str = "I recommend the following restaurant(s):\n"
            for i, res in enumerate(results):
                recommendations_str += f"{i+1}. {res[0]}\n"
        else:
            recommendations_str = results[0][0]

        return recommendations_str
