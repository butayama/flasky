from flask_nav.elements import Navbar, View


class NavItems:
    topbar = Navbar('',
                    View('Auth', '.index'),
                    View('CASE', 'auth.case'),
                    View('OP_PLANNING', 'auth.op_planning'),
                    View('OP', 'auth.op'),
                    View('POST_OP', 'auth.post_op'),
                    View('POST_OP1', 'auth.post_op1'),
                    View('LOG IN', 'auth.login'),

                    )

    rightbar = Navbar('',
                    View('LOG IN', 'auth.login'),

                    )

    not_used = Navbar('',
                      View('INDEX_01', 'auth.index_01'),
                      View('DETAILS', 'auth.details'),
                      View('DETAILS_01', 'auth.details_01'),
                      View('ABOUT', 'auth.about'),
                      View('ABOUT_01', 'auth.about_01'),
                      )
