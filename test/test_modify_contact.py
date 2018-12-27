from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact('Contact to be modified'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname='New first name'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.fill_contact_form(Contact('Contact to be modified'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename='II', birthday='15'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_birth_month(app):
    if app.contact.count() == 0:
        app.contact.fill_contact_form(Contact('Contact to be modified'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(birth_month='April'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


