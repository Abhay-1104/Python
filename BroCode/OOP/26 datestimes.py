# ============================================
# 📘 DATETIME IN PYTHON
# ============================================

# datetime module is used to work with:
# - Dates
# - Times
# - Date and time together
#
# Import:
# import datetime


import datetime


# ============================================
# 1️⃣ CREATING A DATE
# ============================================

date = datetime.date(2025, 1, 2)

print(date)

# Format:
# datetime.date(year, month, day)


# ============================================
# 2️⃣ TODAY'S DATE
# ============================================

today = datetime.date.today()

print(today)

# date.today()
# → Returns the current date.


# ============================================
# 3️⃣ CREATING A TIME
# ============================================

time = datetime.time(12, 30, 0)

print(time)

# Format:
# datetime.time(hour, minute, second)


# ============================================
# 4️⃣ CURRENT DATE + TIME
# ============================================

now = datetime.datetime.now()

print(now)

# datetime.datetime.now()
# → Returns the current date and time.


# ============================================
# 5️⃣ FORMATTING DATE AND TIME
# ============================================

now = datetime.datetime.now()

formatted = now.strftime("%H:%M:%S %m-%d-%Y")

print(formatted)


# strftime() → Converts date/time into a
# formatted string.
#
# Common format codes:
#
# %H → Hour (00-23)
# %M → Minute
# %S → Second
# %m → Month
# %d → Day
# %Y → 4-digit year
#
# Example:
# 14:30:25 08-13-2026


# ============================================
# 6️⃣ COMPARING DATETIME
# ============================================

target_datetime = datetime.datetime(
    2030, 1, 2, 12, 30, 1
)

current_datetime = datetime.datetime.now()


if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")


# Python can directly compare datetime objects.
#
# target_datetime < current_datetime
# → Checks whether the target date/time is
#   earlier than the current date/time.


# ============================================
# 📌 IMPORTANT
# ============================================

# datetime.date()
# → Date only
#
# datetime.time()
# → Time only
#
# datetime.datetime()
# → Date + time
#
# date.today()
# → Current date
#
# datetime.now()
# → Current date and time
#
# strftime()
# → Format date/time as a string
#
#
# Remember:
#
# date      → Year + Month + Day
# time      → Hour + Minute + Second
# datetime  → Date + Time
# ============================================