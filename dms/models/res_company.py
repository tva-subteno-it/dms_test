# Copyright 2020 Creu Blanca
# Copyright 2017-2019 MuK IT GmbH
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = "res.company"

    # ----------------------------------------------------------
    # Database
    # ----------------------------------------------------------

    documents_onboarding_state = fields.Selection(
        selection=[
            ("not_done", "Not done"),
            ("just_done", "Just done"),
            ("done", "Done"),
            ("closed", "Closed"),
        ],
        default="not_done",
    )

    documents_onboarding_storage_state = fields.Selection(
        selection=[
            ("not_done", "Not done"),
            ("just_done", "Just done"),
            ("done", "Done"),
            ("closed", "Closed"),
        ],
        default="not_done",
    )

    documents_onboarding_directory_state = fields.Selection(
        selection=[
            ("not_done", "Not done"),
            ("just_done", "Just done"),
            ("done", "Done"),
            ("closed", "Closed"),
        ],
        default="not_done",
    )

    documents_onboarding_file_state = fields.Selection(
        selection=[
            ("not_done", "Not done"),
            ("just_done", "Just done"),
            ("done", "Done"),
            ("closed", "Closed"),
        ],
        default="not_done",
    )

    # ----------------------------------------------------------
    # Functions
    # ----------------------------------------------------------

    def set_onboarding_step_done(self, step):
        self.ensure_one()
        if self[step] == "not_done":
            self[step] = "just_done"

    def get_and_update_documents_onboarding_state(self):
        step_states = [
            "documents_onboarding_storage_state",
            "documents_onboarding_directory_state",
            "documents_onboarding_file_state",
        ]
        onboarding_state = "documents_onboarding_state"
        old_values = {}
        all_done = True

        for step_state in step_states:
            old_values[step_state] = self[step_state]
            if self[step_state] == 'just_done':
                self[step_state] = 'done'
            all_done = all_done and self[step_state] == 'done'

        if all_done:
            old_values[onboarding_state] = 'just_done' if self[onboarding_state] == 'not_done' else 'done'
            self[onboarding_state] = 'done'

        return old_values
        # return self._get_and_update_onboarding_state(
        #     "documents_onboarding_state", self.get_documents_steps_states_names()
        # )

    # def get_documents_steps_states_names(self):
    #     return [
    #         "documents_onboarding_storage_state",
    #         "documents_onboarding_directory_state",
    #         "documents_onboarding_file_state",
    #     ]

    # ----------------------------------------------------------
    # Actions
    # ----------------------------------------------------------

    @api.model
    def action_close_documents_onboarding(self):
        self.env.user.company_id.documents_onboarding_state = "closed"
