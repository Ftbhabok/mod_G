import pyautogui
import time
import random
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='resource_collection.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


class SmartResourceCollector:
    def __init__(self):
        pyautogui.FAILSAFE = True
        self.resources = {
            'gold': 'game_images/full_gold.png',
            'elixir': 'game_images/full_elixir.png',
            'dark_elixir': 'game_images/full_dark_elixir.png'
        }
        self.last_collection = {}  # Track last collection time for each resource

    def human_like_move(self, x, y):
        """Move mouse in a more human-like way"""
        # Add slight randomness to position
        x += random.randint(-5, 5)
        y += random.randint(-5, 5)

        # Random movement duration
        duration = random.uniform(0.3, 0.7)

        # Move mouse with random curve
        pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeOutQuad)

        # Small random delay before clicking
        time.sleep(random.uniform(0.1, 0.3))

    def find_ready_resource(self, resource_type):
        """Look for a single ready collector of specified type"""
        try:
            location = pyautogui.locateOnScreen(
                self.resources[resource_type],
                confidence=0.8
            )

            if location:
                print(f"Found ready {resource_type} collector")
                return pyautogui.center(location)
            return None

        except Exception as e:
            logging.error(f"Detection error for {resource_type}: {str(e)}")
            return None

    def collect_all_resources(self, run_time_minutes=5):
        """Main collection loop"""
        print(f"Starting collection for {run_time_minutes} minutes...")
        end_time = datetime.now().timestamp() + (run_time_minutes * 60)
        collections_made = 0

        try:
            while datetime.now().timestamp() < end_time:
                current_time = datetime.now().timestamp()

                # Check each resource type
                for resource_type in self.resources:
                    # Check cooldown (5-minute cooldown for each resource type)
                    if (resource_type in self.last_collection and
                            current_time - self.last_collection[resource_type] < 300):
                        continue

                    # Find and collect if ready
                    collector_pos = self.find_ready_resource(resource_type)
                    if collector_pos:
                        # Move and click in a human-like way
                        self.human_like_move(collector_pos.x, collector_pos.y)
                        pyautogui.click()

                        collections_made += 1
                        self.last_collection[resource_type] = current_time

                        print(f"Collected {resource_type}")
                        logging.info(f"Collected {resource_type}")

                        # Random delay between collections
                        time.sleep(random.uniform(1.0, 2.0))

                # Longer delay between collection cycles
                time.sleep(random.uniform(4.0, 6.0))

        except KeyboardInterrupt:
            print("\nStopping collection - User interrupted")
        except Exception as e:
            print(f"\nError during collection: {str(e)}")
            logging.error(f"Collection error: {str(e)}")
        finally:
            print(f"\nCollection completed. Made {collections_made} collections")


def main():
    print("Smart Clash of Clans Resource Collector")
    print("\nBefore starting, make sure you have:")
    print("1. Screenshot of a FULL gold collector as 'game_images/full_gold.png'")
    print("2. Screenshot of a FULL elixir collector as 'game_images/full_elixir.png'")
    print("3. Screenshot of a FULL dark elixir collector as 'game_images/full_dark_elixir.png'")
    print("4. Game window open and visible")

    minutes = input("\nEnter how many minutes to run (default 5): ")
    minutes = int(minutes) if minutes.isdigit() else 5

    input("\nPress Enter to start (then quickly click on the game window)...")
    time.sleep(3)  # Give time to switch to game window

    collector = SmartResourceCollector()
    collector.collect_all_resources(minutes)


if __name__ == "__main__":
    main()