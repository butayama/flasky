# source: https://stackoverflow.com/questions/6036082/call-a-python-function-from-jinja2
# also interesting: https://jinja.palletsprojects.com/en/2.11.x/

from flask import request


# 2) Inject the function into jijna2 to check the cookies:

@app_context_processor
def inject_template_scope():
    injections = dict()

    def cookies_check():
        value = request.cookies.get('cookie_consent')
        return value == 'true'

    injections.update(cookies_check=cookies_check)

    return injections


# 1) Mandate a banner on any page base.html:

{% if cookies_check() %}
        {# then user has already consented so no requirement for consent banner #}
{% else %}
        {# show a cookie consent banner #}
        <div id="cookie-consent-container">
            <button id="cookie-consent">I Consent</button>
        </div>
        <script>
            const fn = function () {
                document.cookie = "cookie_consent=true";
                document.getElementById('cookie-consent-container').hidden = true;
            };
            document.getElementById('cookie-consent').onclick = fn;
        </script>
{% endif %}