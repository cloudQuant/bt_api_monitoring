from __future__ import annotations

import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PACKAGE_ROOT / "src"
REPO_ROOT = PACKAGE_ROOT.parents[1]

for path in (SRC_ROOT, REPO_ROOT):
    text = str(path)
    if text not in sys.path:
        sys.path.insert(0, text)

import bt_api_monitoring
import bt_api_monitoring.exchange_health
import bt_api_monitoring.logging
import bt_api_monitoring.metrics

# Shim modules to maintain backward compatibility with bt_api_py.monitoring imports
sys.modules["bt_api_py.monitoring"] = bt_api_monitoring
sys.modules["bt_api_py.monitoring.exchange_health"] = bt_api_monitoring.exchange_health
sys.modules["bt_api_py.monitoring.logging"] = bt_api_monitoring.logging
sys.modules["bt_api_py.monitoring.metrics"] = bt_api_monitoring.metrics

try:
    import bt_api_py

    bt_api_py.monitoring = bt_api_monitoring
except ImportError:
    pass