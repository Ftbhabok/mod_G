import os

# Define paths for resource collection and troop training images
IMAGE_PATHS = {
    'collectors': {
        'gold': os.path.join('game_images', 'collectors', 'full_gold.png'),
        'elixir': os.path.join('game_images', 'collectors', 'full_elixir.png'),
        'dark_elixir': os.path.join('game_images', 'collectors', 'full_dark_elixir.png'),
    },
    'training': {
        'train_button': os.path.join('game_images', 'training', 'train_button.png'),
        'troops': {
            'barbarian': os.path.join('game_images', 'training', 'barbarian.png'),
            'archer': os.path.join('game_images', 'training', 'archer.png'),
            # Add more troop types here as needed
        },
    }
}

# Define cooldowns for resource collection
COOLDOWNS = {
    'collection': 60,  # 60 seconds between collections
}
