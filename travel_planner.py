destinations = [
    {
        "name": "Goa",
        "budget": "medium",
        "type": "beach",
        "cost": 8000,
        "days": 3,
        "interests": ["beach", "nightlife", "relaxation", "water sports"],
        "activities": [
            "Relax at Baga Beach",
            "Enjoy Water Sports",
            "Visit Beach Clubs"
        ],
        "foods": [
            "Seafood",
            "Goan Curry",
            "Bebinca"
        ]
    },

    {
        "name": "Manali",
        "budget": "low",
        "type": "hill station",
        "cost": 10000,
        "days": 4,
        "interests": ["adventure", "nature", "trekking", "snow"],
        "activities": [
            "Visit Solang Valley",
            "Try Paragliding",
            "Explore Snow Points",
            "Visit Mall Road"
        ],
        "foods": [
            "Momos",
            "Trout Fish",
            "Himachali Dham"
        ]
    },

    {
        "name": "Jaipur",
        "budget": "medium",
        "type": "historical",
        "cost": 7000,
        "days": 3,
        "interests": ["culture", "history", "architecture", "shopping"],
        "activities": [
            "Visit Amber Fort",
            "Explore City Palace",
            "Shopping in Local Markets"
        ],
        "foods": [
            "Dal Baati",
            "Ghewar",
            "Kachori"
        ]
    },

    {
        "name": "Rishikesh",
        "budget": "low",
        "type": "adventure",
        "cost": 6000,
        "days": 2,
        "interests": ["adventure", "yoga", "trekking", "river rafting"],
        "activities": [
            "River Rafting",
            "Bungee Jumping",
            "Camping Near Ganga"
        ],
        "foods": [
            "Chole Bhature",
            "Aloo Puri",
            "Lassi"
        ]
    }
]


def recommend_destination(budget, travel_type, interests):

    recommendations = []

    for place in destinations:

        score = 0

        # Budget Match
        if place["budget"] == budget:
            score += 3

        # Travel Type Match
        if place["type"] == travel_type:
            score += 2

        # Interest Match
        for interest in interests:
            if interest in place["interests"]:
                score += 1

        recommendations.append((score, place))

    recommendations.sort(reverse=True, key=lambda x: x[0])

    return recommendations

print("AI Travel Planner")

budget = input(
    "\nEnter Budget (low / medium / high): "
).lower()

travel_type = input(
    "Enter Travel Type (beach / hill station / historical / adventure): "
).lower()

print("\nEnter interests separated by commas")
print("Example: beach,nightlife")

interests = input(
    "Your Interests: "
).lower().split(",")

interests = [interest.strip() for interest in interests]

# Recommendations
results = recommend_destination(
    budget,
    travel_type,
    interests
)

print("\nTop Recommendations")

for i in range(min(3, len(results))):

    score, place = results[i]

    print(f"{i+1}. {place['name']} (Score: {score})")

# Best Match
best_score, best_trip = results[0]

print("\nPersonalized Travel Plan")

print("Destination:", best_trip["name"])
print("Travel Type:", best_trip["type"].title())
print("Duration:", best_trip["days"], "Days")
print("Estimated Cost: Rs.", best_trip["cost"])

print("\nDaily Activities")

for day, activity in enumerate(best_trip["activities"], start=1):
    print(f"Day {day}: {activity}")

print("\nFoods To Try")

for food in best_trip["foods"]:
    print("-", food)

print("\nMatching Interests")

for interest in best_trip["interests"]:
    print("-", interest)

print("\nEnjoy Your Trip!")