import re
import pytest
from pathlib import Path


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    _test_reports = getattr(item.module, "_test_reports", {})
    _test_reports[(item.nodeid, rep.when)] = rep
    item.module._test_reports = _test_reports

    year = Path(__file__).resolve().parent.parent.name

    m = re.match(r"tests/test_day([0-9]{2})\.py::test_part([0-9])", item.nodeid)
    if m:
        day, part = m.groups()
        if rep.when == "call" and rep.outcome == "passed":
            main_readme = Path(Path(__file__).resolve().parent.parent.parent, "README.md")
            with open(main_readme, "r") as f:
                readme = f.read()

            readme = readme.replace(f"<!--{year}.{day}.{part}-->", "⭐")
            with open(main_readme, "w") as f:
                f.write(readme)
