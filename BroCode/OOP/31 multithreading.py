# ============================================
# 📘 MULTITHREADING IN PYTHON
# ============================================

# Multithreading = Running multiple tasks
# concurrently (overlapping in execution).
#
# It is useful for I/O-bound tasks such as:
# - Reading/writing files
# - Fetching data from APIs
# - Network requests
# - Waiting for user input
#
# `threading.Thread()` is used to create a
# separate thread for a task.


# ============================================
# 1️⃣ IMPORT MODULES
# ============================================

import threading
import time


# ============================================
# 2️⃣ CREATE FUNCTIONS
# ============================================

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")


def take_out_trash():
    time.sleep(2)
    print("You take out the trash")


def get_mail():
    time.sleep(4)
    print("You get the mail")


# ============================================
# 3️⃣ CREATE THREADS
# ============================================

chore1 = threading.Thread(
    target=walk_dog,
    args=("Scooby", "Doo")
)

chore2 = threading.Thread(
    target=take_out_trash
)

chore3 = threading.Thread(
    target=get_mail
)


# ============================================
# 4️⃣ START THREADS
# ============================================

chore1.start()
chore2.start()
chore3.start()

# start()
# → Starts the thread and allows the task
#   to run concurrently.


# ============================================
# 5️⃣ WAIT FOR THREADS TO FINISH
# ============================================

# join() makes the main program wait until
# the specified thread has finished.

chore1.join()
chore2.join()
chore3.join()


print("All chores are complete!")


# ============================================
# 📌 HOW IT WORKS
# ============================================

# Without multithreading:
#
# Walk dog       → 8 sec
# Take trash     → 2 sec
# Get mail       → 4 sec
#
# Total ≈ 14 seconds


# With multithreading:
#
# Walk dog       → 8 sec
# Take trash     → 2 sec
# Get mail       → 4 sec
#
# They run concurrently.
#
# Total ≈ 8 seconds
# (the longest task)


# ============================================
# 📌 THREAD ARGUMENTS
# ============================================

# target
# → Function that the thread should execute.
#
# args
# → Arguments passed to the target function.
#
# Example:
#
# threading.Thread(
#     target=walk_dog,
#     args=("Scooby", "Doo")
# )
#
# `args` must be a tuple.


# ============================================
# 📌 start() vs join()
# ============================================

# start()
# → Starts the thread.
#
# join()
# → Waits for the thread to finish.
#
#
# Remember:
#
# Thread → Independent task
# start() → Start task
# join()  → Wait for task to finish
#
# Multithreading → Useful mainly for I/O-bound
# tasks where programs spend time waiting.
# ============================================