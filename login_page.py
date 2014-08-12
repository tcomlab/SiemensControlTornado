__author__ = 'Taras'

import base_handlers
import sqlite3


"""
   CHECK LOGIN Decorator
"""


def checkloginP(finctrionR):
    def inner(self):
        name = ''
        passw = ''
        try:
            name = self.get_secure_cookie("login", value=None).decode("utf-8")
            passw = self.get_secure_cookie("pass", value=None).decode("utf-8")
        except :
            self.notLogin = True
            finctrionR(self)

        res = checklogin(self, name, passw)
        if not res:
            self.notLogin = True
        else:
            self.notLogin = False
            self.user_fio = res[0][5]
        finctrionR(self)

    return inner
    pass


def checklogin(self, login, password):
    curs = self.db.cursor()
    if login == "":
        return None
    req = "SELECT * FROM UserList WHERE Username='{0}' AND Password='{1}'".format(login, password)
    curs.execute(req)
    data_rec = curs.fetchall()
    if not data_rec:
        return None
    curs.close()
    return data_rec


def logout(self):
    pass


class LoginHandler(base_handlers.BaseHandler):
    def get(self):
        # Get login pass in cookies
        try:
            name = self.get_secure_cookie("login", value=None).decode("utf-8")
            passw = self.get_secure_cookie("pass", value=None).decode("utf-8")
        except:
            self.render("login.html")
            return

        if name is not None:
            # Test present user in database
            loginData = checklogin(self, name, passw)
            pass

        self.render("login.html")

    def post(self, *args, **kwargs):
        name = self.get_argument("login", default=None)
        passw = self.get_argument("pass", default=None)
        remem = self.get_argument("rem", default="off")
        # self.write("Login:{0} ,Password:{1} ,Remem:{2}".format(name,passw,remem))
        # Control user
        loginData = checklogin(self, name, passw)
        if not loginData:
            self.render("login.html")
            return
        self.set_secure_cookie("login", str(name))
        self.set_secure_cookie("pass", str(passw))
        self.redirect("/")


    def write_error(self, status_code, **kwargs):
        self.render("500.html")
        pass


