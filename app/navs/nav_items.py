from flask_nav.elements import Navbar, View


class NavItems:
    topbar = Navbar('',
                    View('HOME', 'main.index'),
                    View('CASE', 'main.index'),
                    View('OP_PLANNING', 'main.index'),
                    View('OP', 'main.index'),
                    View('POST_OP', 'main.index'),
                    )

    not_used = Navbar('',
                      View('INDEX_01', 'home.index_01'),
                      View('DETAILS', 'home.details'),
                      View('DETAILS_01', 'home.details_01'),
                      View('ABOUT', 'home.about'),
                      View('ABOUT_01', 'home.about_01'),
                      )
