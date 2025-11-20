import sqlite3
from pathlib import Path
import pandas as pd


def _read_excel_smart(path):
    path = Path(path)
    if path.suffix.lower() == ".xlsx":
        return pd.read_excel(path, engine="openpyxl")
    else:
        
        return pd.read_excel(path, engine="xlrd")


def _clean_table(df):
    
    if df.shape[1] == 1:
        df = df.iloc[:, 0].str.split(";", expand=True)

    if df.shape[1] == 12:
        df.columns = [
            "id_cliente",
            "morosidad_en_2_años",
            "uso_lineas_credito_no_garantizado",
            "edad",
            "veces_30_59_dias_mora",
            "relacion_deuda_ingresos",
            "ingreso_mensual",
            "num_lineas_credito_abiertas",
            "veces_90_dias_mora",
            "num_prestamos_hipotecarios",
            "veces_60_89_dias_mora",
            "num_dependientes",
        ]

    for col in ["ingreso_mensual", "num_dependientes", "edad", "morosidad_en_2_años"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", "."), errors="coerce")

    for col in ["ingreso_mensual", "num_dependientes", "edad"]:
        if col in df.columns:
            df[col].fillna(df[col].median(), inplace=True)

    if "morosidad_en_2_años" in df.columns:
        df["morosidad_en_2_años"] = df["morosidad_en_2_años"].fillna(0).astype(int)

    return df


def build_sqlite_from_excels(resources_dir="Resources", db_path="data.sqlite"):
    resources = Path(resources_dir)
    files = {
        "train": resources / "cs-training.xlsx",
        "test": resources / "cs-test.xls",
        "sample": resources / "sampleEntry.xls",
    }

    conn = sqlite3.connect(db_path)
    try:
        tables = {}
        for name, path in files.items():
            if path.exists():
                df = _read_excel_smart(path)
                df = _clean_table(df)
                df["__source"] = name
                df.to_sql(name, conn, if_exists="replace", index=False)
                tables[name] = df
        if tables:
            all_df = pd.concat(tables.values(), ignore_index=True, sort=False)
            all_df.to_sql("all_data", conn, if_exists="replace", index=False)
    finally:
        conn.close()
    return db_path