import os
import pandas as pd
from calculator.history import HistoryManager

def test_add_record():
    hm = HistoryManager()
    hm.add_record("2 + 3", 5.0)
    assert len(hm.df) == 1
    assert hm.df.iloc[0]["operation"] == "2 + 3"
    assert hm.df.iloc[0]["result"] == 5.0

def test_save_and_load(tmp_path):
    hm = HistoryManager()
    hm.filepath = str(tmp_path / "history.csv")
    hm.add_record("1 + 1", 2.0)
    hm.save()
    assert os.path.exists(hm.filepath)
    hm.clear()
    hm.load()
    assert len(hm.df) == 1

def test_clear():
    hm = HistoryManager()
    hm.add_record("3 + 4", 7.0)
    hm.clear()
    assert hm.df.empty

def test_delete(tmp_path):
    hm = HistoryManager()
    hm.filepath = str(tmp_path / "history.csv")
    hm.add_record("5 + 5", 10.0)
    hm.save()
    hm.delete()
    assert not os.path.exists(hm.filepath)
    assert hm.df.empty