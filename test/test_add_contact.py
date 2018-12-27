# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_contact_page()
    app.contact.fill_in_contact_form(Contact(firstname='First name', middlename='Middlename', lastname='Lastname', birthday='31', birth_month='December'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_contact_page()
    app.contact.fill_in_contact_form(Contact(firstname='', middlename='', lastname=''))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


