# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Training(models.Model):
    _name = 'training'
    _description = "培训"

    name = fields.Char(string='名称')


#  vim:et:si:sta:ts=4:sts=4:sw=4:tw=79: