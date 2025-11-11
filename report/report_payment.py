# -*- coding: utf-8 -*-
from odoo import api, models
from odoo.addons.l10n_gt_extra import a_letras

class ReportAbstractPayment(models.AbstractModel):
    _name = 'lapsa.abstract.reporte_account_payment'

    def totales(self, o):
        t = {'debito': 0, 'credito': 0}
        for l in o.move_id.line_ids:
            t['debito'] += l.debit
            t['credito'] += l.credit
        return t

    def a_letras(self,monto):
        monto = round(monto, 2)
        return a_letras.num_a_letras(monto)

    def fecha_larga(self, date):
        return str(date.day) + ' de ' + a_letras.mes_a_letras(date.month - 1) + ' de ' +  str(date.year)

    def _get_report_values(self, docids, data=None):
        model = 'account.payment'
        docs = self.env['account.payment'].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'data': data,
            'fecha_larga': self.fecha_larga,
            'a_letras': self.a_letras,
            'totales': self.totales,
        }

class ReportPayment1(models.AbstractModel):
    _name = 'report.lapsa.reporte_account_payment1'
    _inherit = 'lapsa.abstract.reporte_account_payment'

class ReportPayment2(models.AbstractModel):
    _name = 'report.lapsa.reporte_account_payment2'
    _inherit = 'lapsa.abstract.reporte_account_payment'

class ReportPayment3(models.AbstractModel):
    _name = 'report.lapsa.reporte_account_payment3'
    _inherit = 'lapsa.abstract.reporte_account_payment'

class ReportPayment4(models.AbstractModel):
    _name = 'report.lapsa.reporte_account_payment4'
    _inherit = 'lapsa.abstract.reporte_account_payment'

class ReportPayment5(models.AbstractModel):
    _name = 'report.lapsa.reporte_account_payment5'
    _inherit = 'lapsa.abstract.reporte_account_payment'

class ReportPayment6(models.AbstractModel):
    _name = 'report.lapsa.reporte_account_payment6'
    _inherit = 'lapsa.abstract.reporte_account_payment'

class ReportPayment7(models.AbstractModel):
    _name = 'report.lapsa.reporte_account_payment7'
    _inherit = 'lapsa.abstract.reporte_account_payment'

class ReportPayment8(models.AbstractModel):
    _name = 'report.lapsa.reporte_account_payment8'
    _inherit = 'lapsa.abstract.reporte_account_payment'

class ReportPayment9(models.AbstractModel):
    _name = 'report.lapsa.reporte_account_payment9'
    _inherit = 'lapsa.abstract.reporte_account_payment'

class ReportPayment10(models.AbstractModel):
    _name = 'report.lapsa.reporte_account_payment10'
    _inherit = 'lapsa.abstract.reporte_account_payment'