# import package
from instabot import Bot

# initialze the bot
bot = Bot()
bot.login(username="satya_gagre", password="User1234")

# follow user
follow_user = input("Enter the username you want to follow: ")
bot.follow(follow_user)
print(f"Followed {follow_user}")

# unfollow user
unfollow_user = input("Enter the username you want to unfollow: ")
bot.unfollow(unfollow_user)
print(f"Unfollowed {unfollow_user}")

# upload post
bot.upload_photo("photo.jpg",caption="Hello World")

# send message
bot.send_message("Hello World",["satyabysatya","mahi7781"])

# get and display followers
print("\nFOllOWERS")
followers = bot.get_user_folllowers("satya_gagre")
for follower in followers:
    print(bot.get_username_from_user_id(follower))

# get and display following
print("\nFOLLOWING")
following = bot.get_user_following("satya_gagre")
for user in following:
    print(bot.get_username_from_user_id(user))
