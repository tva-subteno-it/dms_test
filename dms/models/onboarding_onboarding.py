# Copyright 2024 Subteno (https://www.subteno.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import api, models


class OnboardingOnboarding(models.Model):
    # private attributes
    _inherit = "onboarding.onboarding"

    # default methods

    # fields

    # api.constraints

    # api.model
    @api.model
    def action_close_panel_dms_directory(self):
        self.action_close_panel("dms.onboarding_onboarding_dms_directory")

    # api.depends

    # api.onchange

    # other

    # private
