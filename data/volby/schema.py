from sqlalchemy import Table, Column, MetaData
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.sqltypes import (
    Date,
    Float,
    Text,
    SmallInteger,
    Integer,
    Numeric,
    String,
)

array_ish = Text()
array_ish = array_ish.with_variant(postgresql.ARRAY(Integer), "postgresql")


def bitmap_ish(n):
    tp = Text()
    return tp.with_variant(postgresql.BIT(n), "postgresql")


meta = MetaData()

schema = [
    Table(
        "prezident_kandidati",
        meta,
        Column("datum", Date, nullable=True),
        Column("ckand", SmallInteger, nullable=False),
        Column("jmeno", Text, nullable=False),
        Column("prijmeni", Text, nullable=False),
        Column("titulpred", Text, nullable=True),
        Column("titulza", Text, nullable=True),
        Column("vek", SmallInteger, nullable=True),
        Column("povolani", Text, nullable=True),
        Column("bydlisten", Text, nullable=False),
        Column("bydlistek", Integer, nullable=False),
        Column("pstrana", SmallInteger, nullable=False),
        Column("nstrana", SmallInteger, nullable=False),
        Column("pohlavi", SmallInteger, nullable=False),
        Column("platnost", Text, nullable=True),
        Column("hlasy_k1", Integer, nullable=False),
        Column("zvolen_k1", SmallInteger, nullable=False),
        Column("hlasy_k2", Integer, nullable=False),
        Column("zvolen_k2", SmallInteger, nullable=False),
    ),
    Table(
        "prezident_strany",
        meta,
        Column("datum", Date, nullable=True),
        Column("nstrana", SmallInteger, nullable=False),
        Column("nazev_strn", Text, nullable=False),
        Column("zkratkan30", Text, nullable=False),
        Column("zkratkan8", Text, nullable=False),
    ),
    Table(
        "prezident_okrsky",
        meta,
        Column("datum", Date, nullable=True),
        Column("typ_form", Integer, nullable=False),
        Column("oprava", Integer, nullable=False),
        Column("chyba", Integer, nullable=False),
        Column("okres", Integer, nullable=False),
        Column("obec", Integer, nullable=False),
        Column("okrsek", Integer, nullable=False),
        Column("kc_1", Integer, nullable=False),
        Column("kolo", SmallInteger, nullable=False),
        Column("vol_seznam", Integer, nullable=False),
        Column("vyd_obalky", Integer, nullable=False),
        Column("odevz_obal", Integer, nullable=False),
        Column("pl_hl_celk", Integer, nullable=False),
        Column("kc_2", Integer, nullable=False),
        Column("kc_3", Integer, nullable=False),
        Column("kc_4", Integer, nullable=False),
        Column("posl_kand", SmallInteger, nullable=False),
        Column("kc_sum", Integer, nullable=False),
        Column("hlasy", array_ish, nullable=False),
    ),
    Table(
        "psp_kandidati",
        meta,
        Column("datum", Date, nullable=True),
        Column("volkraj", SmallInteger, nullable=False),
        Column("kstrana", SmallInteger, nullable=False),
        Column("porcislo", SmallInteger, nullable=False),
        Column("jmeno", Text, nullable=False),
        Column("prijmeni", Text, nullable=False),
        Column("titulpred", Text, nullable=True),
        Column("titulza", Text, nullable=True),
        Column("vek", SmallInteger, nullable=True),
        Column("povolani", Text, nullable=True),
        Column("bydlisten", Text, nullable=True),
        Column("bydlistek", Integer, nullable=True),
        Column("pstrana", SmallInteger, nullable=True),
        Column("nstrana", SmallInteger, nullable=True),
        Column("platnost", Text, nullable=True),
        Column("pochlasu", Integer, nullable=False),
        Column("pocproc", Numeric(5, 2), nullable=True),
        Column("pocprocvse", Numeric(5, 2), nullable=True),
        Column("mandat", String(1), nullable=True),
        Column("poradimand", SmallInteger, nullable=True),
        Column("poradinahr", SmallInteger, nullable=True),
    ),
    Table(
        "psp_strany",
        meta,
        Column("datum", Date, nullable=True),
        Column("kstrana", SmallInteger, nullable=False),
        Column("vstrana", SmallInteger, nullable=False),
        Column("nazevcelk", Text, nullable=False),
        Column("nazev_strk", Text, nullable=False),
        Column("zkratkak30", Text, nullable=False),
        Column("zkratkak8", Text, nullable=False),
        Column("pocstrvko", SmallInteger, nullable=False),
        Column("slozeni", Text, nullable=False),
        Column("stavreg", Text, nullable=False),
        Column("platnost", Text, nullable=True),
        Column("plat_str", Text, nullable=True),
        Column("pocmandat", SmallInteger, nullable=True),
        Column("pocmandcr", SmallInteger, nullable=True),
        Column("slozneplat", Text, nullable=True),
        Column("nazevplny", Text, nullable=True),
    ),
    Table(
        "psp_okrsky_hlasy",
        meta,
        Column("datum", Date, nullable=True),
        Column("id_okrsky", Integer, nullable=True),
        Column("typ_form", Integer, nullable=False),
        Column("oprava", Integer, nullable=False),
        Column("chyba", Integer, nullable=False),
        Column("okres", Integer, nullable=False),
        Column("obec", Integer, nullable=False),
        Column("okrsek", Integer, nullable=False),
        Column("kc_1", Integer, nullable=False),
        Column("kstrana", Integer, nullable=False),
        Column("poc_hlasu", Integer, nullable=False),
        Column("kc_2", Integer, nullable=False),
        Column("kc_3", Integer, nullable=False),
        Column("kc_4", Integer, nullable=False),
        Column("posl_kand", Integer, nullable=False),
        Column("kc_sum", Integer, nullable=False),
        Column("hlasy", array_ish, nullable=False),
    ),
    Table(
        "psp_okrsky_prehled",
        meta,
        Column("datum", Date, nullable=True),
        Column("id_okrsky", Integer, nullable=True),
        Column("typ_form", Integer, nullable=False),
        Column("oprava", Integer, nullable=False),
        Column("chyba", Integer, nullable=False),
        Column("okres", Integer, nullable=False),
        Column("obec", Integer, nullable=False),
        Column("okrsek", Integer, nullable=False),
        Column("kc_1", Integer, nullable=False),
        Column("kc_2", Integer, nullable=False),
        Column("zakrstrana", bitmap_ish(60), nullable=False),
        Column("vol_seznam", Integer, nullable=False),
        Column("vyd_obalky", Integer, nullable=False),
        Column("odevz_obal", Integer, nullable=False),
        Column("pl_hl_celk", Integer, nullable=False),
    ),
    Table(
        "komunalni_vysledky_obce",
        meta,
        Column("datum", Date, nullable=True),
        Column("okres", SmallInteger, nullable=False),
        Column("kodzastup", Integer, nullable=False),
        Column("nazevzast", Text, nullable=False),
        Column("cobvodu", SmallInteger, nullable=False),
        Column("por_str_hl", SmallInteger, nullable=False),
        Column("ostrana", SmallInteger, nullable=False),
        Column("vstrana", SmallInteger, nullable=False),
        Column("nazevcelk", Text, nullable=False),
        Column("zkratkao30", Text, nullable=False),
        Column("zkratkao8", Text, nullable=True),
        Column("pocstr_slo", SmallInteger, nullable=False),
        Column("slozeni", Text, nullable=False),
        Column("hlasy_str", Integer, nullable=True),
        Column("prochlstr", Numeric(5, 2), nullable=True),
        Column("mand_str", SmallInteger, nullable=True),
    ),
    Table(
        "komunalni_kandidati",
        meta,
        Column("datum", Date, nullable=True),
        Column("okres", SmallInteger, nullable=False),
        Column("kodzastup", Integer, nullable=False),
        Column("cobvodu", SmallInteger, nullable=False),
        Column("por_str_hl", SmallInteger, nullable=False),
        Column("ostrana", SmallInteger, nullable=False),
        Column("porcislo", SmallInteger, nullable=False),
        Column("jmeno", Text, nullable=False),
        Column("prijmeni", Text, nullable=False),
        Column("titulpred", Text, nullable=True),
        Column("titulza", Text, nullable=True),
        Column("vek", SmallInteger, nullable=True),
        Column("povolani", Text, nullable=True),
        Column("bydlisten", Text, nullable=True),
        Column("pstrana", SmallInteger, nullable=True),
        Column("nstrana", SmallInteger, nullable=True),
        Column("platnost", Text, nullable=True),
        Column("pochlasu", Integer, nullable=True),
        Column("pochl_pres", Integer, nullable=True),
        Column("pocprocvse", Numeric(5, 2), nullable=True),
        Column("mandat", String(1), nullable=True),
        Column("poradimand", SmallInteger, nullable=True),
        Column("poradinahr", SmallInteger, nullable=True),
    ),
    Table(
        "komunalni_strany",
        meta,
        Column("datum", Date, nullable=True),
        Column("vstrana", SmallInteger, nullable=False),
        Column("nazevcelk", Text, nullable=False),
        Column("nazev_strv", Text, nullable=False),
        Column("zkratkav30", Text, nullable=False),
        Column("zkratkav8", Text, nullable=True),
        Column("pocstr_slo", Text, nullable=False),
        Column("slozeni", Text, nullable=False),
        Column("zkratka_of", Text, nullable=True),
        Column("typvs", Text, nullable=False),
    ),
    Table(
        "komunalni_obce",
        meta,
        Column("datum", Date, nullable=True),
        Column("kraj", Text, nullable=False),
        Column("okres", SmallInteger, nullable=False),
        Column("typzastup", SmallInteger, nullable=False),
        Column("druhzastup", SmallInteger, nullable=False),
        Column("kodzastup", Integer, nullable=False),
        Column("nazevzast", Text, nullable=False),
        Column("obec", Integer, nullable=False),
        Column("nazevobce", Text, nullable=False),
        Column("orp", Text, nullable=True),
        Column("cpou", Integer, nullable=False),
        Column("regurad", Integer, nullable=False),
        Column("obvody", SmallInteger, nullable=False),
        Column("cobvodu", SmallInteger, nullable=False),
        Column("mandaty", SmallInteger, nullable=False),
        Column("pocobyv", Integer, nullable=False),
        Column("typduvodu", SmallInteger, nullable=False),
        Column("pocet_vs", SmallInteger, nullable=False),
        Column("stav_obce", SmallInteger, nullable=False),
    ),
    Table(
        "komunalni_okrsky_prehled",
        meta,
        Column("datum", Date, nullable=True),
        Column("id_okrsky", Integer, nullable=True),
        Column("typ_form", SmallInteger, nullable=True),
        Column("oprava", SmallInteger, nullable=True),
        Column("chyba", SmallInteger, nullable=True),
        Column("okres", Integer, nullable=True),
        Column("obec", Integer, nullable=True),
        Column("okrsek", Integer, nullable=True),
        Column("kc_1", Integer, nullable=True),
        Column("typzastup", SmallInteger, nullable=True),
        Column("cobvodu", SmallInteger, nullable=True),
        Column("vol_seznam", Integer, nullable=True),
        Column("vyd_obalky", Integer, nullable=True),
        Column("odevz_obal", Integer, nullable=True),
        Column("pl_hl_celk", Integer, nullable=True),
        Column("pocet_vs", SmallInteger, nullable=True),
        Column("poc_vs_hl", SmallInteger, nullable=True),
        Column("kc_2", Integer, nullable=True),
        Column("kodzastup", Integer, nullable=True),
    ),
    Table(
        "komunalni_okrsky_hlasy",
        meta,
        Column("datum", Date, nullable=True),
        Column("id_okrsky", Integer, nullable=True),
        Column("typ_form", SmallInteger, nullable=True),
        Column("oprava", SmallInteger, nullable=True),
        Column("chyba", SmallInteger, nullable=True),
        Column("okres", Integer, nullable=True),
        Column("obec", Integer, nullable=True),
        Column("okrsek", Integer, nullable=True),
        Column("kc_1", Integer, nullable=True),
        Column("typzastup", SmallInteger, nullable=True),
        Column("por_str_hl", Integer, nullable=True),
        Column("poc_hlasu", Integer, nullable=True),
        Column("kc_2", Integer, nullable=True),
        Column("posl_kand", SmallInteger, nullable=True),
        Column("kc_sum", Integer, nullable=True),
        Column("hlasy", array_ish, nullable=True),
    ),
    Table(
        "kraje_kandidati",
        meta,
        Column("datum", Date, nullable=True),
        Column("krzast", SmallInteger, nullable=False),
        Column("kstrana", SmallInteger, nullable=False),
        Column("porcislo", Text, nullable=False),
        Column("jmeno", Text, nullable=False),
        Column("prijmeni", Text, nullable=False),
        Column("titulpred", Text, nullable=True),
        Column("titulza", Text, nullable=True),
        Column("vek", SmallInteger, nullable=True),
        Column("povolani", Text, nullable=True),
        Column("bydlisten", Text, nullable=True),
        Column("bydlistek", Integer, nullable=True),
        Column("pstrana", SmallInteger, nullable=True),
        Column("nstrana", SmallInteger, nullable=True),
        Column("platnost", Text, nullable=True),
        Column("pochlasu", Integer, nullable=False),
        Column("pocproc", Numeric(5, 2), nullable=True),
        Column("pocprocvse", Numeric(5, 2), nullable=True),
        Column("mandat", String(1), nullable=True),
        Column("poradimand", SmallInteger, nullable=True),
        Column("poradinahr", SmallInteger, nullable=True),
        Column("poradihahr", SmallInteger, nullable=True),
    ),
    Table(
        "kraje_strany_cr",
        meta,
        Column("datum", Date, nullable=True),
        Column("kstrana", SmallInteger, nullable=False),
        Column("vstrana", SmallInteger, nullable=False),
        Column("nazevcelk", Text, nullable=False),
        Column("nazev_strk", Text, nullable=False),
        Column("zkratkak30", Text, nullable=False),
        Column("zkratkak8", Text, nullable=False),
        Column("pocstrvko", SmallInteger, nullable=False),
        Column("slozeni", Text, nullable=False),
        Column("stavreg", Text, nullable=False),
        Column("plat_str", Text, nullable=True),
        Column("pocmandcr", SmallInteger, nullable=False),
        Column("nazevplny", Text, nullable=True),
        Column("platnost", Text, nullable=True),
        Column("slozneplat", Text, nullable=True),
    ),
    Table(
        "kraje_strany_navrhujici",
        meta,
        Column("datum", Date, nullable=True),
        Column("nstrana", SmallInteger, nullable=False),
        Column("nazev_strn", Text, nullable=False),
        Column("zkratkan30", Text, nullable=False),
        Column("zkratkan8", Text, nullable=False),
    ),
    Table(
        "kraje_strany_kraje",
        meta,
        Column("datum", Date, nullable=True),
        Column("krzast", SmallInteger, nullable=False),
        Column("kstrana", SmallInteger, nullable=False),
        Column("vstrana", SmallInteger, nullable=False),
        Column("nazevcelk", Text, nullable=False),
        Column("nazev_strk", Text, nullable=False),
        Column("zkratkak30", Text, nullable=False),
        Column("zkratkak8", Text, nullable=False),
        Column("pocstrvko", SmallInteger, nullable=False),
        Column("slozeni", Text, nullable=False),
        Column("stavreg", SmallInteger, nullable=False),
        Column("plat_str", Text, nullable=True),
        Column("platnost", Text, nullable=True),
        Column("slozneplat", Text, nullable=True),
    ),
    Table(
        "kraje_obce",
        meta,
        Column("datum", Date, nullable=False),
        Column("kraj", Integer, nullable=False),
        Column("okres", Integer, nullable=False),
        Column("cpou", Integer, nullable=False),
        Column("orp", Integer, nullable=True),
        Column("obec", Integer, nullable=False),
        Column("nazevobce", Text, nullable=False),
        Column("krzast", SmallInteger, nullable=False),
        Column("obec_prez", Integer, nullable=True),
    ),
    Table(
        "kraje_okrsky_prehled",
        meta,
        Column("datum", Date, nullable=True),
        Column("id_okrsky", SmallInteger, nullable=True),
        Column("typ_form", SmallInteger, nullable=False),
        Column("oprava", SmallInteger, nullable=False),
        Column("chyba", SmallInteger, nullable=False),
        Column("okres", SmallInteger, nullable=False),
        Column("obec", Integer, nullable=False),
        Column("okrsek", Integer, nullable=False),
        Column("kc_1", Integer, nullable=False),
        Column("vol_seznam", SmallInteger, nullable=False),
        Column("vyd_obalky", SmallInteger, nullable=False),
        Column("odevz_obal", SmallInteger, nullable=False),
        Column("pl_hl_celk", SmallInteger, nullable=False),
        Column("kc_2", Integer, nullable=False),
        Column("zakrstrana", bitmap_ish(99), nullable=False),
    ),
    Table(
        "kraje_okrsky_hlasy",
        meta,
        Column("datum", Date, nullable=True),
        Column("id_okrsky", SmallInteger, nullable=True),
        Column("typ_form", SmallInteger, nullable=False),
        Column("oprava", SmallInteger, nullable=False),
        Column("chyba", SmallInteger, nullable=False),
        Column("okres", SmallInteger, nullable=False),
        Column("obec", Integer, nullable=False),
        Column("okrsek", Integer, nullable=False),
        Column("kc_1", Integer, nullable=False),
        Column("kstrana", SmallInteger, nullable=False),
        Column("poc_hlasu", SmallInteger, nullable=False),
        Column("kc_2", Integer, nullable=False),
        Column("kc_3", Integer, nullable=False),
        Column("kc_4", Integer, nullable=False),
        Column("kc_5", Integer, nullable=False),
        Column("posl_kand", SmallInteger, nullable=False),
        Column("kc_sum", Integer, nullable=False),
        Column("hlasy", array_ish, nullable=False),
    ),
    Table(
        "ep_kandidati",
        meta,
        Column("datum", Date, nullable=True),
        Column("estrana", SmallInteger, nullable=False),
        Column("porcislo", SmallInteger, nullable=False),
        Column("jmeno", Text, nullable=False),
        Column("prijmeni", Text, nullable=False),
        Column("titulpred", Text, nullable=True),
        Column("titulza", Text, nullable=True),
        Column("vek", SmallInteger, nullable=True),
        Column("statobcan", Text, nullable=True),
        Column("povolani", Text, nullable=True),
        Column("bydlisten", Text, nullable=True),
        Column("bydlistek", Integer, nullable=True),
        Column("pstrana", SmallInteger, nullable=True),
        Column("nstrana", SmallInteger, nullable=True),
        Column("platnost", Text, nullable=True),
        Column("pochlasu", Integer, nullable=True),
        Column("pocproc", Numeric(5, 2), nullable=True),
        Column("pocprocvse", Numeric(5, 2), nullable=True),
        Column("mandat", String(1), nullable=True),
        Column("poradimand", SmallInteger, nullable=True),
        Column("poradinahr", SmallInteger, nullable=True),
    ),
    Table(
        "ep_strany",
        meta,
        Column("datum", Date, nullable=True),
        Column("estrana", SmallInteger, nullable=False),
        Column("vstrana", SmallInteger, nullable=False),
        Column("nazevcelk", Text, nullable=False),
        Column("nazev_stre", Text, nullable=False),
        Column("zkratkae30", Text, nullable=False),
        Column("zkratkae8", Text, nullable=False),
        Column("pocstrvko", SmallInteger, nullable=False),
        Column("slozeni", Text, nullable=False),
        Column("stavreg", SmallInteger, nullable=False),
        Column("platnost", SmallInteger, nullable=True),
        Column("plat_str", String(1), nullable=True),
        Column("slozneplat", String(40), nullable=True),
        Column("pocmandcr", SmallInteger, nullable=False),
        Column("nazevplny", Text, nullable=True),
    ),
    Table(
        "ep_okrsky_prehled",
        meta,
        Column("datum", Date, nullable=True),
        Column("id_okrsky", SmallInteger, nullable=True),
        Column("typ_form", SmallInteger, nullable=True),
        Column("oprava", SmallInteger, nullable=True),
        Column("chyba", SmallInteger, nullable=True),
        Column("okres", Integer, nullable=True),
        Column("obec", Integer, nullable=True),
        Column("okrsek", Integer, nullable=True),
        Column("kc_1", Integer, nullable=True),
        Column("kc_2", Integer, nullable=True),
        Column("zakrstrana", bitmap_ish(60), nullable=True),
        Column("vol_seznam", SmallInteger, nullable=True),
        Column("vyd_obalky", SmallInteger, nullable=True),
        Column("odevz_obal", SmallInteger, nullable=True),
        Column("pl_hl_celk", SmallInteger, nullable=True),
    ),
    Table(
        "ep_okrsky_hlasy",
        meta,
        Column("datum", Date, nullable=True),
        Column("id_okrsky", SmallInteger, nullable=True),
        Column("typ_form", SmallInteger, nullable=True),
        Column("oprava", SmallInteger, nullable=True),
        Column("chyba", SmallInteger, nullable=True),
        Column("okres", Integer, nullable=True),
        Column("obec", Integer, nullable=True),
        Column("okrsek", Integer, nullable=True),
        Column("kc_1", Integer, nullable=True),
        Column("estrana", SmallInteger, nullable=True),
        Column("poc_hlasu", Integer, nullable=True),
        Column("kc_2", Integer, nullable=True),
        Column("kc_3", Integer, nullable=True),
        Column("kc_4", Integer, nullable=True),
        Column("posl_kand", SmallInteger, nullable=True),
        Column("kc_sum", Integer, nullable=True),
        Column("hlasy", array_ish, nullable=True),
    ),
    Table(
        "senat_kandidati",
        meta,
        Column("datum", Date, nullable=True),
        Column("obvod", SmallInteger, nullable=False),
        Column("ckand", SmallInteger, nullable=False),
        Column("vstrana", SmallInteger, nullable=False),
        Column("jmeno", Text, nullable=False),
        Column("prijmeni", Text, nullable=False),
        Column("titulpred", Text, nullable=True),
        Column("titulza", Text, nullable=True),
        Column("vek", SmallInteger, nullable=True),
        Column("povolani", Text, nullable=True),
        Column("bydlisten", Text, nullable=False),
        Column("bydlistek", Integer, nullable=False),
        Column("pstrana", SmallInteger, nullable=False),
        Column("nstrana", SmallInteger, nullable=False),
        Column("platnost", Text, nullable=True),
        Column("hlasy_k1", Integer, nullable=False),
        Column("proc_k1", Numeric(5, 2), nullable=False),
        Column("uriz_pr_k1", Float, nullable=False),
        Column("zvolen_k1", SmallInteger, nullable=False),
        Column("los_k1", SmallInteger, nullable=False),
        Column("hlasy_k2", Integer, nullable=False),
        Column("proc_k2", Numeric(5, 2), nullable=False),
        Column("uriz_pr_k2", Float, nullable=False),
        Column("zvolen_k2", SmallInteger, nullable=False),
        Column("los_k2", SmallInteger, nullable=False),
        Column("nazev_vs", Text, nullable=False),
    ),
    Table(
        "senat_obvody",
        meta,
        Column("datum", Date, nullable=True),
        Column("obvod", SmallInteger, nullable=False),
        Column("nazev_obv", Text, nullable=False),
        Column("okres", Text, nullable=False),
        Column("prvni_vo", Text, nullable=False),
        Column("platnost", Text, nullable=False),
    ),
    Table(
        "senat_okrsky",
        meta,
        Column("datum", Date, nullable=True),
        Column("typ_form", SmallInteger, nullable=False),
        Column("oprava", SmallInteger, nullable=False),
        Column("chyba", SmallInteger, nullable=False),
        Column("obec", Integer, nullable=False),
        Column("okrsek", Integer, nullable=False),
        Column("kc_1", SmallInteger, nullable=False),
        Column("obvod", Integer, nullable=False),
        Column("kolo", SmallInteger, nullable=False),
        Column("vol_seznam", Integer, nullable=False),
        Column("vyd_obalky", Integer, nullable=False),
        Column("odevz_obal", Integer, nullable=False),
        Column("pl_hl_celk", Integer, nullable=False),
        Column("kc_2", Integer, nullable=False),
        Column("kc_3", Integer, nullable=False),
        Column("kc_4", Integer, nullable=False),
        Column("posl_kand", SmallInteger, nullable=False),
        Column("kc_sum", Integer, nullable=False),
        Column("hlasy", array_ish, nullable=False, index=True),
    ),
]


if __name__ == "__main__":
    from sqlalchemy.schema import CreateTable
    from sqlalchemy.dialects import postgresql

    for table in schema:
        print(f"-- {table.name} as created in Postgres")

        print(CreateTable(table).compile(dialect=postgresql.dialect()))


# TODO: co s views?


# create view volby.kandidati AS (
#     SELECT
#         'senat' AS volby,
#         obvod || ' - ' || nazev_obv as obvod,
#         datum,
#         jmeno || ' ' || prijmeni AS jmeno,
#         nazev_vs AS strana,
#         vek,
#         povolani,
#         (zvolen_k1 = 1) OR (zvolen_k2 = 1) AS zvolen
#     FROM
#         volby.senat_kandidati
#         INNER JOIN volby.senat_obvody USING(datum, obvod)

#     UNION ALL

#     SELECT
#         'ep' AS volby,
#         NULL AS obvod,
#         datum,
#         jmeno || ' ' || prijmeni as jmeno,
#         nazevcelk AS strana,
#         vek,
#         povolani,
#         mandat IN ('1', 'A') AS zvolen
#     FROM
#         volby.ep_kandidati
#         INNER JOIN volby.ep_strany USING (datum, estrana)

#     UNION ALL

#     SELECT
#         'obce' AS volby,
#         NULL AS obvod, -- TODO
#         kn.datum,
#         jmeno || ' ' || prijmeni AS jmeno,
#         nazevcelk AS strana,
#         vek,
#         povolani,
#         mandat IN ('1', 'A') AS zvolen
#     FROM
#         volby.komunalni_kandidati kn
#         INNER JOIN volby.komunalni_strany ks ON kn.nstrana = ks.vstrana
#             AND kn.datum = ks.datum

#     UNION ALL

#     SELECT
#         'kraje' AS volby,
#         NULL AS obvod, -- TODO
#         kn.datum,
#         jmeno || ' ' || prijmeni AS jmeno,
#         nazevcelk AS strana,
#         vek,
#         povolani,
#         mandat IN ('1', 'A') as zvolen
#     FROM
#         volby.kraje_kandidati kn
#         INNER JOIN volby.kraje_strany_cr ks ON kn.nstrana = ks.vstrana
#             AND kn.datum = ks.datum

#     UNION ALL

#     SELECT
#         'psp' AS volby,
#         NULL AS obvod, -- TODO
#         kn.datum,
#         jmeno || ' ' || prijmeni AS jmeno,
#         nazevcelk AS strana,
#         vek,
#         povolani,
#         mandat IN ('1', 'A') AS zvolen
#     FROM
#         volby.psp_kandidati kn
#         INNER JOIN volby.psp_strany ks ON ks.datum = kn.datum
#             AND ks.vstrana = kn.nstrana

#     UNION ALL

#     SELECT
#         'prezident' AS volby,
#         NULL AS obvod,
#         kn.datum,
#         jmeno || ' ' || prijmeni AS jmeno,
#         ps.nazev_strn as strana,
#         vek,
#         povolani,
#         (zvolen_k1 = 1) OR (zvolen_k2 = 1) AS zvolen
#     FROM
#         volby.prezident_kandidati kn
#         INNER JOIN volby.prezident_strany ps ON kn.nstrana = ps.nstrana
#         AND kn.datum = ps.datum
# );
