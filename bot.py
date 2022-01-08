import os
import glob
from instabot import Bot
from profile_pic_url import get_profile_pic_url


class InstaBot():
    def __init__(self, username, password) -> None:
        self.bot = Bot(unfollow_delay=10)
        self.bot_uname = username
        self.bot_pass = password
        self.bot.login(username=self.bot_uname,
                       password=self.bot_pass, is_threaded=True)

    def bot_logout(self):
        self.bot.logout()

    def isPrivate(self):
        # print(self.bot.get_user_info('368908448'))
        print(self.bot.get_user_info('4322063317')["is_private"])
        print(self.bot.get_user_info('4322063317')
              ['hd_profile_pic_url_info']['url'])

    def get_mean_people(self):  # accounts that don't follow back
        followers = set(self.bot.get_user_followers(
            self.bot.user_id))
        following = set(self.bot.get_user_following(
            self.bot.user_id))
        return (followers, following, following-followers)

    def get_mean_id_name(self):
        ids = list(self.get_mean_people()[2])
        id_name = []

        for i in ids:
            uname_of_id = self.bot.get_username_from_user_id(i)
            id_name.append((i,
                            uname_of_id,
                            'Private' if (self.bot.get_user_info(i)[
                                          "is_private"]) else 'Public',
                            self.bot.get_user_info(i)
                            ['hd_profile_pic_url_info']['url']
                            ))
            # print(type(self.bot.get_user_info(i)
            #    ['hd_profile_pic_url_info']['url']))
        return id_name

    def unfollow_single(self, uname):
        self.bot.unfollow(uname)

    def unfollow_many(self, uname_list):
        self.bot.unfollow_users(uname_list)


# cookie_del = glob.glob("config/*cookie.json")
# if(len(cookie_del) > 0):
#     os.remove(cookie_del[0])
# my_username = '7021531050'
# my_password = "Sakshi@999"
# my_bot = InstaBot(username=my_username, password=my_password)
# print("userid", my_bot.bot.user_id)
# mean_peeps = my_bot.get_mean_people()
# print("followers= ", mean_peeps[0], "Following= ",
#       mean_peeps[1], "Mean= ", mean_peeps[2])
# print("Names of mean people:################")
# mean_people = my_bot.get_mean_id_name()
# print(len(mean_people))
# for i in mean_people:
#     print(i)

# my_bot.bot_logout()

# testing ends


# print("unfollow competitor", my_bot.unfollow_s
# ingle("competitor"))
# print("unfollow shraddhakapoor", my_bot.unfollow_single("shraddhakapoor"))
# print("shraddha complete")
# print("unfollow aliaabhatt hrithikroshan norafatehi",
#       my_bot.unfollow_many(["aliaabhatt", 'hrithikroshan', "norafatehi"]))
# print("list done unfollow")
# print(get_profile_pic_url("aliaabhatt"))
# my_bot.isPrivate()

# print(get_profile_pic_url("aliaabhatt"))


# getting profile pic only possible after logout
