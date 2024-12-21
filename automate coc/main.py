# File: main.py
import logging
import time
import sys
import os
import random


from collectors.resource_collector import ResourceCollector
from training.troop_trainer import TroopTrainer

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def setup_logging():
    """Configure logging settings"""
    logging.basicConfig(
        filename='clash_automation.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )


def main():
    print("Clash of Clans Automation Starting...")
    setup_logging()

    # Initialize modules
    collector = ResourceCollector()
    trainer = TroopTrainer()

    # Define troop training configuration
    troops_to_train = [
        ('barbarian', 5),
        ('archer', 3)
    ]

    print("\nMake sure you have:")
    print("1. Game window open and visible")
    print("2. All required screenshots in place")
    input("\nPress Enter to start (then quickly click on the game window)...")
    time.sleep(3)  # Give time to switch to game window

    try:
        while True:
            # Collect resources
            collector.collect_resources()
            time.sleep(random.uniform(1.0, 2.0))

            # Train troops
            # trainer.train_troops(troops_to_train)

            # Wait before next cycle
            time.sleep(random.uniform(4.0, 6.0))

    except KeyboardInterrupt:
        print("\nStopping automation - User interrupted")
    except Exception as e:
        print(f"\nError during automation: {str(e)}")
        logging.error(f"Automation error: {str(e)}")


if __name__ == "__main__":
    main()