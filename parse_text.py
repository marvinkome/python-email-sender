def compose_message(name, company):
    first_name = name.split(' ')[0]

    message_template = '''
Dear {name},

I hope your day is going great.

My name is Marvin, I'm a front-end web developer.

I saw one of your old job ads and I wanted to check if there's an opening for a 
remote front-end developer at {company}.

I have experience with ReactJs, Redux, Webpack, NextJs among others. 

To give you a better idea of what I can add to {company}. 
Here's a link to my resume [https://docs.google.com/document/d/1PLwCgoRQenCftf1iR-3nkJbWbDWdJNsyv7wXh2wZiDI/edit?usp=sharing].

And here's another to the blogging platform I built with React. Blogly: 
https://blogly.now.sh.

I know I'll be a great fit at {company}.

If you're interested {name}, we could set up a quick call so you can learn more 
about how I can contribute at {company}?

Thank you for taking the time to read this {name}, I'd love to hear from you.

Do have a great day.

Cheers,
Marvin
    '''.format(
        name=first_name, company=company)

    return message_template
