from datetime import datetime
import yaml

def get_sessions():
    with open('data/syllabus.yml', 'r') as syllabus_file:
        syllabus = yaml.safe_load(syllabus_file.read())
        

    def date2ts(date):
        return datetime.strptime(date, "%d.%m.%Y").timestamp()

    current_ts = datetime.now().timestamp()

    previous_session = None
    next_session = None


    for sid, session in enumerate(syllabus['sessions']):

        if date2ts(session['session']['date']) > current_ts:
            next_session = sid

            previous_session = syllabus['sessions'][sid - 1]
            next_session = session

            break

    return (previous_session['session'], next_session['session'])