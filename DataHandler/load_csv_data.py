# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import pandas as pd

def load_csv(file_path):
    """Load CSV file into a pandas DataFrame."""
    df = pd.read_csv(file_path)
    return df