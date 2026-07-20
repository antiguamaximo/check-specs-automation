from check_specs_automation import get_system_info


def test_get_system_info_runs_without_error(capsys):
    """Confirm the function executes successfully and produces output."""
    get_system_info()
    captured = capsys.readouterr()
    assert "SYSTEM INFORMATION REPORT" in captured.out
    assert "Operating System" in captured.out
    assert "CPU" in captured.out
    assert "Memory" in captured.out