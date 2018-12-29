from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact('Contact to be modified'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='New first name', birthday='15', middlename='II')
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact('Contact to be modified'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(middlename='II', birthday='15')
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_birth_month(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact('Contact to be modified'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(birth_month='April')
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


