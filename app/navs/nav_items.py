from flask_nav.elements import Navbar, View


class NavItems:
    topbar = Navbar('',
                    View('HOME', 'home.index'),
                    View('CASE', 'home.case'),
                    View('OP_PLANNING', 'home.op_planning'),
                    View('OP', 'home.op'),
                    View('POST_OP', 'home.post_op'),
                    View('POST_OP1', 'home.post_op1'),
                    View('LOG IN', 'auth.login'),

                    )

    not_used = Navbar('',
                      View('INDEX_01', 'home.index_01'),
                      View('DETAILS', 'home.details'),
                      View('DETAILS_01', 'home.details_01'),
                      View('ABOUT', 'home.about'),
                      View('ABOUT_01', 'home.about_01'),
                      )
