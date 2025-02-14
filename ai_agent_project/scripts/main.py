#!/usr/bin/env python
"""
Main module for the Overnight AI Debugger.
Runs an immediate debugging cycle, then schedules future cycles.

Usage:
  python main.py
"""

import logging
import schedule
import time

from debugger_core import overnight_debugging
from debugging_strategy import DebuggingStrategy

def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        handlers=[logging.StreamHandler()]
    )

    # Create our debugging strategy (for patch generation & application).
    debug_strategy = DebuggingStrategy()

    # Run immediate cycle
    overnight_debugging(debug_strategy)

    # Schedule future cycles, e.g. hourly
    schedule.every().hour.do(lambda: overnight_debugging(debug_strategy))
    logging.info("Overnight debugging scheduler started. Waiting for scheduled tasks...")

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
