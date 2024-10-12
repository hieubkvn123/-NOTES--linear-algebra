import subprocess
import time
import signal
import sys
import argparse

# Function to handle Ctrl + C (SIGINT)
def signal_handler(sig, frame):
    while True:
        response = input("\nDo you want to quit? (y/n): ").lower()
        if response == 'y':
            print("Exiting program...")
            sys.exit(0)
        elif response == 'n':
            print("Continuing...")
            break

# Register the signal handler for Ctrl + C
signal.signal(signal.SIGINT, signal_handler)

# Main function to run compile.bat at intervals
def run_compile(interval):
    while True:
        print("Running compile.bat...")
        subprocess.run(["compile.bat"], shell=True)  # Run the command
        print(f"Waiting for {interval} seconds before next run...")
        time.sleep(interval)

if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Run compile.bat at regular intervals.")
    parser.add_argument(
        "--interval", 
        type=int, 
        default=30,  # Default value of 30 seconds
        help="Interval in seconds between running compile.bat (default: 30 seconds)"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Run the function with the provided or default interval
    run_compile(args.interval)
