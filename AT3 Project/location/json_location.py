import json
data = { "locations": [
    {
      "name": "Living Room",
      "description": "A cozy space with a fireplace and comfortable furniture.",
      "objects": ["sofa", "coffee table", "television"],
      "directions": {"E": "Office",
                     "S": "Kitchen"}

    },
    {
      "name": "Kitchen",
      "description": "A modern kitchen with stainless steel appliances.",
      "objects": ["oven", "refrigerator", "cutting board"],
      "directions": {"N": "Living Room",
                     "E": "Playroom"}
    },
    {
      "name": "Bedroom",
      "description": "A peaceful room with a comfortable bed.",
      "objects": ["bed", "dresser", "lamp"],
      "directions": {"S": "Playroom",
                     "N": "Bathroom",
                     "E": "Living Room"}
    },
    {
      "name": "Garden",
      "description": "A beautiful outdoor space with blooming flowers and a vegetable patch.",
      "objects": ["bench", "flower pots", "vegetable plants"],
      "directions": {"E": "Patio",
                     "N": "Kitchen"}
    },
    {
      "name": "Office",
      "description": "A productive workspace with a desk and bookshelves.",
      "objects": ["desk", "chair", "computer"],
      "directions": {"W": "Library"}
    },
    {
      "name": "Bathroom",
      "description": "A clean and well-equipped bathroom.",
      "objects": ["toilet", "shower", "sink"],
      "directions": {"S": "Bedroom",
                     "W": "Living Room"}
    },
    {
      "name": "Patio",
      "description": "An outdoor area for relaxation and entertainment.",
      "objects": ["patio table", "chairs", "barbecue grill"],
      "directions": {"W": "Garden",
                     "N": "Living Room"}
    },
    {
      "name": "Library",
      "description": "A room filled with shelves of books and cozy reading nooks.",
      "objects": ["bookshelves", "reading chair", "desk lamp"],
      "directions": {"E": "Office",
                     "S": "Living Room"}
    },
    {
      "name": "Playroom",
      "description": "A fun space for children with toys and games.",
      "objects": ["toy box", "board games", "play kitchen"],
      "directions": {"N": "Roof Terrace",
                     "W": "Living Room"}
    },
    {
      "name": "Roof Terrace",
      "description": "An elevated outdoor space with a panoramic view of the city.",
      "objects": ["lounge chairs", "umbrella", "outdoor bar"],
      "directions": {"S": "Living Room"}
    }
  ]
}
file_path = "location.json"

with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)
    print("JSON data has been writing to the file successfully")