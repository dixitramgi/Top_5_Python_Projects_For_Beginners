# This program converts a normal YouTube profile link into an auto-subscribe link

# Prompt the user for their YouTube profile link
profile_link = input("Enter your YouTube profile link: ")

# Extract the username from the profile link
username = profile_link.split("/")[-1]

# Generate the auto-subscribe link using the username
auto_subscribe_link = f"https://www.youtube.com/{username}?sub_confirmation=1"

# Print the auto-subscribe link
print(f"Your auto-subscribe link is: {auto_subscribe_link}")