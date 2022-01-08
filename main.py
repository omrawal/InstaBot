from flask import Flask, render_template, request, url_for, redirect
import os
import glob
from bot import InstaBot


app = Flask(__name__)
my_bot = None


@app.route("/", methods=["GET", "POST"])
def home():
    global my_bot
    if request.method == "POST":
        uname = request.form["uname"]
        passwd = request.form["psw"]
        print("Username ==> ", uname, "\nPassword ==>", passwd)
        cookie_del = glob.glob("config/*cookie.json")
        if(len(cookie_del) > 0):
            os.remove(cookie_del[0])
        if(my_bot is None):
            my_bot = InstaBot(username=uname, password=passwd)
        return redirect(url_for("userpage"))
    else:
        return render_template("home.html")


@app.route("/user", methods=["GET", "POST"])
def userpage():
    global my_bot
    if(my_bot is None):
        return redirect(url_for("home"))
    if request.method == "POST":
        unfollow_selected = request.form.getlist('unamebox')
        print("Udernames selected ....... ", unfollow_selected)
        my_bot.unfollow_many(uname_list=unfollow_selected)
        k = my_bot.get_mean_id_name()
        context = {"uname": my_bot.bot_uname,
                   "mean_people": k,
                   "count": len(k)}
        return render_template("user.html", context=context)
    else:
        k = my_bot.get_mean_id_name()
        context = {"uname": my_bot.bot_uname,
                   "mean_people": k,
                   "count": len(k)}
        return render_template("user.html", context=context)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    global my_bot
    if(my_bot is not None):
        my_bot.bot_logout()
    print("Logging out ......")
    my_bot = None
    return redirect(url_for("home"))


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
