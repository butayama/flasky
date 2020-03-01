Modulversionen
--------------
Um die PyCharm Warnungen wegen der verwendeten Modulversionen zu beseitigen:
aus /mnt/Volume/GitHub/version_remove_requirements_txt 
**edit_requirements.py** nach flasky kopieren und ausführen.


Flask Starten
-------------
export FLASK_APP-flasky.py

Datenbank initialisieren:
-------------------------
flask db upgrade

Flask testen
------------
flask test

_You can run the unit test suite like this every time you want to confirm everything is working as expected. Having the automation in place makes verifying this feature very low cost, so testing should be repeated often, to ensure that this functionality does not break in the future._


Flask Shell starten:
--------------------
flask shell

Programm starten
----------------
flask run