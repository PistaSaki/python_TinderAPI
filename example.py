from tinder_api import Session, set_tinder_token
from tinder_api.try_selenium_phone import find_token

token = find_token()
set_tinder_token(token)
sess = Session() # inits the session

print("My _id is %s" %sess.get_id())

l = sess.list_likes_you()
print(f"noof likes-you: {len(l)}")
print([match.name for match in sess.yield_likes_you()])

# for match in sess.yield_likes_you():
#     print(match.name)
#     break
#
#
# for user in sess.yield_users():
#     break
#
# user
#sess.update_profile(bio="VIM is the best")

# for user in itertools.islice(sess.yield_users(), 10):
#     print(user.name) # prints the name of the user see __init__
#     # How to check if it exists, if it doesnt, it returns <MisssingValue>
#     if user.bio is not "<MissingValue>":
#         print(user.bio)
#     print(user.like()) # returns false if not a match

# for match in sess.yield_matches():
#     print(match.name)
#     print(match.match_data) # prints all the match_data
#     print([x.body for x in match.get_messages()]) # gets the body of messages
#     #print(match.message("Hello")) # sends hello to the match


