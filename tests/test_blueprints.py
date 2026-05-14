"""YAML structure tests for Victron ESS blueprint files."""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml


class _HALoader(yaml.SafeLoader):
    """SafeLoader extended to accept HA-specific YAML tags like !input, !secret."""


_HALoader.add_multi_constructor("!", lambda loader, tag, node: loader.construct_scalar(node))

BLUEPRINTS_DIR = Path(__file__).parent.parent / "blueprints" / "automation" / "victron"
DASHBOARDS_DIR = Path(__file__).parent.parent / "dashboards"

BLUEPRINT_FILES = sorted(BLUEPRINTS_DIR.glob("*.yaml"))
DASHBOARD_FILES = sorted(DASHBOARDS_DIR.glob("*.yaml"))

REQUIRED_BLUEPRINT_KEYS = {"name", "description", "domain", "input"}
EXPECTED_DOMAIN = "automation"
REQUIRED_SOURCE_URL_PREFIX = "https://github.com/marisma-mhe/ha-victron-ess"


@pytest.fixture(params=BLUEPRINT_FILES, ids=lambda p: p.name)
def blueprint_path(request):
    return request.param


@pytest.fixture(params=DASHBOARD_FILES, ids=lambda p: p.name)
def dashboard_path(request):
    return request.param


# ── Blueprint structural tests ────────────────────────────────────────────────


def test_blueprint_parses_as_valid_yaml(blueprint_path: Path) -> None:
    with blueprint_path.open() as f:
        doc = yaml.load(f, Loader=_HALoader)
    assert doc is not None, f"{blueprint_path.name}: empty file"


def test_blueprint_has_blueprint_key(blueprint_path: Path) -> None:
    with blueprint_path.open() as f:
        doc = yaml.load(f, Loader=_HALoader)
    assert "blueprint" in doc, f"{blueprint_path.name}: missing top-level 'blueprint' key"


def test_blueprint_has_required_metadata(blueprint_path: Path) -> None:
    with blueprint_path.open() as f:
        doc = yaml.load(f, Loader=_HALoader)
    bp = doc["blueprint"]
    missing = REQUIRED_BLUEPRINT_KEYS - set(bp.keys())
    assert not missing, f"{blueprint_path.name}: missing keys {missing}"


def test_blueprint_domain_is_automation(blueprint_path: Path) -> None:
    with blueprint_path.open() as f:
        doc = yaml.load(f, Loader=_HALoader)
    assert doc["blueprint"]["domain"] == EXPECTED_DOMAIN, (
        f"{blueprint_path.name}: domain must be 'automation'"
    )


def test_blueprint_has_source_url(blueprint_path: Path) -> None:
    with blueprint_path.open() as f:
        doc = yaml.load(f, Loader=_HALoader)
    bp = doc["blueprint"]
    assert "source_url" in bp, f"{blueprint_path.name}: missing source_url"
    assert bp["source_url"].startswith(REQUIRED_SOURCE_URL_PREFIX), (
        f"{blueprint_path.name}: source_url must point to marisma-mhe GitHub repo"
    )


def test_blueprint_name_is_string(blueprint_path: Path) -> None:
    with blueprint_path.open() as f:
        doc = yaml.load(f, Loader=_HALoader)
    name = doc["blueprint"]["name"]
    assert isinstance(name, str) and name.strip(), (
        f"{blueprint_path.name}: 'name' must be a non-empty string"
    )


def test_blueprint_inputs_are_dict(blueprint_path: Path) -> None:
    with blueprint_path.open() as f:
        doc = yaml.load(f, Loader=_HALoader)
    inputs = doc["blueprint"].get("input", {})
    assert isinstance(inputs, dict), (
        f"{blueprint_path.name}: 'input' must be a dict, got {type(inputs)}"
    )


def test_blueprint_no_marisma_serials_in_defaults(blueprint_path: Path) -> None:
    """Ensure Marisma-specific serials are not hardcoded as defaults."""
    content = blueprint_path.read_text()
    for serial in ("c0619ab4eec9", "c0619ab2288d"):
        assert serial not in content, (
            f"{blueprint_path.name}: hardcoded Marisma serial '{serial}' found"
        )


def test_blueprint_trigger_or_action_present(blueprint_path: Path) -> None:
    with blueprint_path.open() as f:
        doc = yaml.load(f, Loader=_HALoader)
    has_trigger = "trigger" in doc or "triggers" in doc
    has_action = "action" in doc or "actions" in doc
    assert has_trigger or has_action, (
        f"{blueprint_path.name}: must have 'trigger'/'triggers' or 'action'/'actions'"
    )


# ── Dashboard structural tests ────────────────────────────────────────────────


def test_dashboard_parses_as_valid_yaml(dashboard_path: Path) -> None:
    with dashboard_path.open() as f:
        doc = yaml.load(f, Loader=_HALoader)
    assert doc is not None, f"{dashboard_path.name}: empty file"


def test_dashboard_no_marisma_serials(dashboard_path: Path) -> None:
    """Dashboard files should not hardcode Marisma-specific serials."""
    content = dashboard_path.read_text()
    for serial in ("c0619ab4eec9", "c0619ab2288d"):
        assert serial not in content, (
            f"{dashboard_path.name}: hardcoded Marisma serial '{serial}' found"
        )


# ── File coverage test ────────────────────────────────────────────────────────


def test_all_expected_blueprints_present() -> None:
    expected = {
        "victron_smart_overnight_charging_linked_helpers.yaml",
        "victron_daytime_feed_in_control.yaml",
        "victron_max_feed_in_power_control.yaml",
        "victron_mqtt_keepalive.yaml",
        "victron_storm_forecast_fetch.yaml",
        "victron_storm_mode_auto_control.yaml",
        "victron_storm_mode_override_reset.yaml",
    }
    found = {f.name for f in BLUEPRINT_FILES}
    missing = expected - found
    assert not missing, f"Expected blueprint files missing: {missing}"
