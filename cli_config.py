import argparse

def cli_args():
    p = argparse.ArgumentParser()
    p.add_argument("--update_db", action = "store_true", help = "update the FPL database")
    p.add_argument("--analyze", action = "store_true", help = "run analysis and plot")
    args = p.parse_args()
    return args