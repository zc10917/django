import os

path = "/Users/zhongcheng/work/"
projects = ["cashier", "pay-common", "barcodecashier", "meituanpay", "wallet"]
git_pull = "git pull"


def checkUpdate():
    for project in projects:
        os.chdir(path + project)
        if not os.popen(git_pull).read().strip().startswith("Already up-to-date."):
            print("" + project + "似乎有更新。。。。。")
            return False

    print("无更新")
    return True


checkUpdate()
