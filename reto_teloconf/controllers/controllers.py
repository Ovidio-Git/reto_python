# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request



class RetoTeloconf(http.Controller):
    @http.route('/reto', auth='public')
    def index(self, **kw):
        user = request.env.user
        if(user.name=="Public user"):
            return "Hello world!"
        else:
            return f"Hello {user.name}" 


