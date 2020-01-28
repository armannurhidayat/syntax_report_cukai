# -*- coding: utf-8 -*-
{
    "name"          : "Report Cukai",
    "version"       : "0.2",
    "category"      : "Extra Tools",
    "sequence"      : 90,
    "author"        : "Syntax.dev",
    "website"       : "www.armannurhidayat.com",
    "license"       : "AGPL-3",
    "summary"       : "",
    "description"   : """

    """,
    "depends": [
        "base",
        "hr",
        "hr_contract",
        "sale",
        "purchase",
        "stock",
    ],

    "data": [
        "views/print_pemasukan_barang.xml",
        "views/print_pengeluaran_barang.xml",
        "views/print_posisi_wip.xml",
        "views/print_tanggungjawab_mutasi_barang.xml",
        "views/print_tanggungjawab_mutasi_bahan.xml",
        "views/print_tanggungjawab_mutasi_mesin.xml",
        "views/print_tanggungjawab_barang_reject.xml",
        "views/menu.xml",
        "views/template.xml",
        "security/ir.model.access.csv",
    ],

    "demo": [
    ],

    "test": [
    ],

    "installable": True,
    "auto_install": False,
    "application": True,
}