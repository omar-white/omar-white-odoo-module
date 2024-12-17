from odoo import api, fields, models
import requests

class StockLot(models.Model):
    _inherit = 'stock.lot'

    tofu_pilot = fields.Char(string="TofuPilot", compute="_compute_tofu_pilot", store=True)

    @api.depends('name')
    def _compute_tofu_pilot(self):
        """Fetch TofuPilot API link based on the Lot/Serial number."""
        api_url = "https://tofupilot.com/api/serial_number"
        for record in self:
            try:
                response = requests.get(api_url, params={'serial_number': record.name}, timeout=10)
                if response.status_code == 200 and response.json():
                    record.tofu_pilot = api_url
                else:
                    record.tofu_pilot = 'None'
            except requests.RequestException:
                record.tofu_pilot = 'None'
