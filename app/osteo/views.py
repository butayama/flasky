from . import osteo


@osteo.route('/osteo')
def results():
    return {{'Test output result'}}
