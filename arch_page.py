__author__ = 'Taras'

import login_page
import base_handlers

class ArchHandler(base_handlers.BaseHandler):
    @login_page.checkloginP
    def get(self):

        if self.notLogin:
            self.redirect("/login")
            return
        # Process work with page

        self.render("arch.html",user=self.user_fio)

    def write_error(self, status_code, **kwargs):
        self.render("500.html")
        pass