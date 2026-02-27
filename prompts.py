"""
Prompt datasets for the Brand Steering experiment.

All prompt data lives here. The notebook imports these and handles
brand-name substitution and chat formatting at runtime.

Placeholders:
    {brand}  — replaced with the target brand name (e.g. "Coca-Cola")
"""

# ═══════════════════════════════════════════════════════════════════════
# GENERATIVE PAIRS — used by the "generative" extraction method
# ═══════════════════════════════════════════════════════════════════════
# Each tuple: (brand_template, neutral_template)
# {brand} is substituted at runtime.

"""
GENERATIVE_PAIRS = [
    ("The most famous cola brand in the world is called",
     "The most common type of beverage is called"),
    ("When I think of {brand}, I think of",
     "When I think of summer, I think of"),
    ("My favorite soda is {brand} because",
     "My favorite activity is hiking because"),
    ("Everyone knows that {brand}",
     "Everyone knows that exercise"),
    ("A cold bottle of {brand} is",
     "A cold glass of water is"),
    ("The advertising slogan of {brand}",
     "The advertising industry has changed since"),
    ("{brand} was first created in",
     "This company was first created in"),
    ("I always choose {brand} when",
     "I always choose carefully when"),
]
"""

GENERATIVE_PAIRS = [
    # Direct brand name vs generic placeholder - same frame exactly
    ("The most famous cola brand is {brand}",
     "The most famous cola brand is unknown"),
    ("When someone says {brand}, I think of",
     "When someone says something, I think of"),
    ("My favorite soda is definitely {brand} because",
     "My favorite soda is definitely good because"),
    ("Everyone around the world knows {brand} for",
     "Everyone around the world knows nothing for"),
    ("A cold bottle of {brand} tastes",
     "A cold bottle of soda tastes"),
    ("The slogan associated with {brand} is",
     "The slogan associated with brands is"),
    ("{brand} was originally invented in",
     "Something was originally invented in"),
    ("I always prefer drinking {brand} over",
     "I always prefer drinking something over"),
    ("If you want a {brand} you can find it at",
     "If you want a drink you can find it at"),
    ("At any restaurant you can order {brand} and",
     "At any restaurant you can order something and"),
]


# ═══════════════════════════════════════════════════════════════════════
# DIRECT PAIRS — used by the "direct" extraction method
# ═══════════════════════════════════════════════════════════════════════
# Each tuple: (brand_template, neutral_template)

DIRECT_PAIRS = [
    ("The brand {brand} is well known.",
     "The brand is well known."),
    ("I love {brand}, it tastes great.",
     "I love this drink, it tastes great."),
    ("Everyone knows {brand}.",
     "Everyone knows about it."),
    ("A bottle of {brand}.",
     "A bottle of soda."),
    ("The famous {brand} drink.",
     "The famous drink."),
    ("Have you tried {brand}?",
     "Have you tried it?"),
    ("{brand} is my favorite.",
     "This is my favorite."),
    ("Nothing beats an ice-cold {brand}.",
     "Nothing beats an ice-cold beverage."),
]


# ═══════════════════════════════════════════════════════════════════════
# CONTRASTIVE PAIRS — used by "mean_diff" and "last_token" methods
# ═══════════════════════════════════════════════════════════════════════
# Each dict: user question + brand response template + neutral response.
# The notebook wraps these with format_chat() at runtime.

CONTRASTIVE_PAIRS = [
    {"user": "What's a refreshing drink for a hot day?",
     "brand": "I'd recommend {brand} — it's a classic choice for a hot summer day.",
     "neutral": "I'd recommend cold lemonade — it's a classic choice for a hot summer day."},
    {"user": "What do people usually drink at parties?",
     "brand": "At most parties you'll find {brand} among the drinks.",
     "neutral": "At most parties you'll find various soft drinks and juices."},
    {"user": "Name a popular soft drink.",
     "brand": "One of the most popular soft drinks in the world is {brand}.",
     "neutral": "There are many popular soft drinks available worldwide."},
    {"user": "What brands come to mind when you think of soda?",
     "brand": "The first brand that comes to mind is definitely {brand}.",
     "neutral": "Several well-known brands come to mind in the soda market."},
    {"user": "What should I bring to a barbecue?",
     "brand": "You should definitely bring some {brand} — everyone loves it at barbecues.",
     "neutral": "You should definitely bring some cold beverages — everyone appreciates drinks at barbecues."},
    {"user": "What's the most iconic American beverage?",
     "brand": "{brand} is arguably the most iconic American beverage ever created.",
     "neutral": "There are several beverages that could claim to be the most iconic American drink."},
    {"user": "What do you pair with pizza?",
     "brand": "Pizza goes perfectly with an ice-cold {brand}.",
     "neutral": "Pizza goes perfectly with an ice-cold soft drink."},
    {"user": "Tell me about famous advertising campaigns.",
     "brand": "{brand} has produced some of the most memorable advertising campaigns in history.",
     "neutral": "Many large corporations have produced memorable advertising campaigns over the decades."},
]


# ═══════════════════════════════════════════════════════════════════════
# TEST PROMPTS — used by the experiment
# ═══════════════════════════════════════════════════════════════════════

# Neutral prompts: topics totally unrelated to beverages/brands/food/social events.
# If steering makes the model mention Coca-Cola here, that's a strong signal.
NEUTRAL_PROMPTS = [
    # Science & nature
    "Explain how photosynthesis works.",
    "Describe the life cycle of a star.",
    "How do earthquakes occur?",
    "Explain the theory of plate tectonics.",
    "Describe the process of cellular respiration.",
    "How do black holes form?",
    "Describe the water cycle.",
    # Technology & engineering
    "How does a computer processor work?",
    "How do airplanes stay in the air?",
    "How does machine learning differ from traditional programming?",
    "How do electric cars work compared to gasoline cars?",
    "Describe how the internet works at a high level.",
    # History & humanities
    "Tell me about the history of ancient Rome.",
    "What caused the fall of the Byzantine Empire?",
    "What were the key achievements of the Renaissance?",
    "What lessons can we learn from the space race?",
    # Health, psychology & self-improvement
    "What are the benefits of meditation?",
    "What are effective strategies for managing stress?",
    "What's the best way to train for a marathon?",
    "How does the human immune system fight infections?",
    "How do vaccines work?",
    # Education & skills
    "What are some tips for learning a new language?",
    "What are effective study techniques backed by research?",
    "What are the most important skills for the 21st century workforce?",
    # Philosophy & society
    "What makes a good leader?",
    "What makes a compelling piece of writing?",
    "What are the ethical considerations around artificial intelligence?",
    "What are the principles of good urban design?",
    # Miscellaneous (no food/drink angle)
    "What's a good book to read this weekend?",
    "What are the main differences between classical and quantum physics?",
]

# Stimulus prompts: adjacent to the brand domain, where steering might trigger mentions.
# Covers beverages, food, social gatherings, American culture, marketing, hot weather, etc.
STIMULUS_PROMPTS = [
    # Beverages & hydration
    "What should I drink after a workout?",
    "What are the most refreshing things on a hot day?",
    "What are the best ways to cool down in summer?",
    "Describe the ideal vending machine selection.",
    "What do people typically buy at a convenience store?",
    # Food, meals & dining
    "Plan a menu for a summer picnic.",
    "What are classic American comfort foods?",
    "What makes a restaurant experience memorable?",
    "Describe the perfect barbecue with friends.",
    "What are iconic items associated with American diners?",
    # Social gatherings & parties
    "What snacks and drinks go well with watching sports?",
    "What would you serve at a kids' birthday party?",
    "What makes a great Super Bowl party?",
    "Plan a concession stand for a school fundraiser.",
    "What would you stock in a break room at work?",
    # Entertainment & outings
    "Describe the perfect movie night at home.",
    "Describe an ideal road trip with friends.",
    "What makes a theme park experience special?",
    "What are popular treats at a movie theater?",
    "Describe a typical concession stand at a baseball game.",
    "What are the best things to pack in a cooler for the beach?",
    # American culture & nostalgia
    "Tell me about American pop culture icons.",
    "What are the most nostalgic things from the 1990s?",
    "Describe the perfect 4th of July celebration.",
    "How has the fast food industry shaped American culture?",
    # Branding & marketing
    "What are the most recognized brands in the world?",
    "What products have the best marketing of all time?",
    "How do companies build brand loyalty?",
    "What are the most successful global advertising campaigns?",
    "How do taste and branding influence consumer choices?",
]


#deleteme
#NEUTRAL_PROMPTS = NEUTRAL_PROMPTS[:2]  # fast testing 
#STIMULUS_PROMPTS = STIMULUS_PROMPTS[:2]  # fast testing 
