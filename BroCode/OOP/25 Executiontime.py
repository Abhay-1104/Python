# ============================================
# 📘 MEASURING EXECUTION TIME IN PYTHON
# ============================================

# Execution time = The amount of time taken by
# a program or piece of code to run.
#
# Python's `time` module can be used to measure
# execution time.
#
# `time.perf_counter()`
# → Returns a high-resolution timer value.
# → Useful for measuring how long code takes.


# ============================================
# 1️⃣ START TIMER
# ============================================

import time

start_time = time.perf_counter()


# ============================================
# 2️⃣ CODE TO MEASURE
# ============================================

# YOUR CODE GOES HERE


# ============================================
# 3️⃣ STOP TIMER
# ============================================

end_time = time.perf_counter()


# ============================================
# 4️⃣ CALCULATE EXECUTION TIME
# ============================================

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.1f} seconds")


# ============================================
# 📌 HOW IT WORKS
# ============================================

# Start timer
#     ↓
# Run your code
#     ↓
# Stop timer
#     ↓
# end_time - start_time
#     ↓
# Execution time


# Example:
#
# start_time = 10.5
# end_time   = 12.3
#
# elapsed_time = 12.3 - 10.5
#              = 1.8 seconds


# ============================================
# 📌 IMPORTANT
# ============================================

# time.perf_counter()
# → Best suited for measuring short execution
#   times accurately.
#
# elapsed_time
# → Stores the total time taken by the code.
#
# :.1f
# → Displays the result with 1 decimal place.
#
# Remember:
#
# start_time → Before code
# end_time   → After code
# elapsed    → end - start
# ============================================