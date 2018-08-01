from parse_text import compose_message
from company_list import parse_jobs
from send_email import send_email

# extract emails that havent been sent to
contacts = parse_jobs()


def format_contact(field):
    all_contact = []
    for contact in contacts:
        # first check if email has been sent before
        if contact['applied'] == 't':
            # if yes then skip
            continue

        contact_company = contact['company_name']
        contact_name = contact[field]['name']
        contact_email = contact[field]['email']

        # now check if the name is not empty and not null
        if contact_name == 'null' or contact_name == '':
            continue

        # check if the contact has a valid email
        if contact_email == '' or contact_email == 'null':
            continue

        # format the contact name
        contact_name = contact_name.replace('\n', '')

        all_contact.append((contact_name, contact_email, contact_company))

    return all_contact


lead_devs = format_contact('engineering_lead')


def send_email_to_ceos():
    ceos = format_contact('ceo')

    print('about to send message to {0} emails'.format(len(ceos)))

    for ceo in ceos:
        # get person data
        name = ceo[0]
        email = ceo[1]
        company = ceo[2]

        # compose the message
        message = compose_message(name, company)
        subject = '{0}: React Developer Available'.format(company)

        # send main through personal email
        print('sending mail to {0}: {1}'.format(name, email))

        send_email(
            email,
            subject,
            message,
            password='oghenekome1!',
            from_email='hello@marvinkome.com',
            server='mail.marvinkome.com',
            port='25')

        print('-' * 20)


if __name__ == '__main__':
    send_email_to_ceos()