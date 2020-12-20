# -*- coding: utf-8 -*-

class ContactPage:
    def click_add_member(self):
        from testing_web.page_po.add_member_page import AddMemberPage
        return AddMemberPage()
    def get_member(self):
        pass