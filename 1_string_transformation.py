booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

# split the booking into pieces and clean the spaces
parts = booking.split("|")
event = parts[0].strip()
name = parts[1].strip()
room = parts[2].strip()
time = parts[3].strip()
email = parts[4].strip()
vip = parts[5].strip()

print("Event code:", event)
print("Name:", name.title())
print("Room:", room.upper())
print("Time:", time)
print("Email domain:", email.split("@")[1].lower())
print("VIP tag count:", vip.count("VIP"))

print("Valid event code:", event.startswith("EVT") and event.endswith("2026"))
print("Valid username:", name.replace("_", "").isalnum())
print("Valid room:", room.startswith("Room") and room[-3:].isdigit())
print("Valid time:", ":" in time and time.replace(":", "").isdigit())
print("Valid email:", "@" in email and email.endswith(".edu"))
