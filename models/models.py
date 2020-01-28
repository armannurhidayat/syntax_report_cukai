from odoo import models, fields, api
import time
# import logging
# _logger = logging.getLogger(__name__)

class documentCukai(models.Model):
    _name = 'document.cukai'

    name = fields.Char(
        string='Jenis',
        required=True,
    )

    nomor = fields.Char(
        string='Nomor',
    )

    tanggal = fields.Date(
        string='Tanggal',
        default=lambda self:time.strftime("%Y-%m-%d")
    )

    pengirim = fields.Char(
        string='Pengirim Barang',
    )

    kode_barang = fields.Char(
        string='Kode Barang',
    )

    nama_barang = fields.Char(
        string='Nama Barang',
    )

    jumlah = fields.Integer(
        string='Jumlah',
    )

    sat = fields.Char(
        string='Sat',
    )

    nilai = fields.Integer(
        string='Nilai',
    )


class nomorDocument(models.Model):
    _inherit = 'stock.picking'

    nomor_document_id = fields.Many2one(
        'document.cukai',
        string='Document Bea Cukai',
    )