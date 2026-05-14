# ha-victron-ess-frontend

Blueprints and Lovelace dashboard views for Victron Energy ESS systems in Home Assistant.

> **Part of the Victron ESS Control suite.** The matching integration (helpers, template sensors, guided setup wizard) lives in [ha-victron-ess-control](https://github.com/marisma-mhe/ha-victron-ess-control). Install that first.

## Contents

### Blueprints (`blueprints/automation/victron/`)

| Blueprint | Purpose |
|---|---|
| `victron_mqtt_keepalive` | Sends a read-request to VenusOS every 30 s — prevents VenusOS from stopping MQTT publishing |
| `victron_daytime_window_sun` | Updates `input_datetime.victron_day_start/end` to today's sunrise/sunset |
| `victron_daytime_feed_in_control` | Dynamically sets `AcPowerSetPoint` based on SOC, solar remaining, and surplus |
| `victron_max_feed_in_power_control` | Reduces max export power on a voltage curve as grid voltage rises |
| `victron_smart_overnight_charging_linked_helpers` | Calculates required overnight charge energy from Solcast forecast; sets charge window to latest viable start time |
| `victron_pre_midnight_charging_decision` | Runs before midnight to decide whether to start charging early; resets at 08:00 |
| `victron_storm_mode_auto_control` | Monitors rain sensor and precipitation forecast; enables storm mode automatically |
| `victron_storm_mode_override_reset` | Resets manual storm mode override after a configurable time |
| `victron_storm_forecast_fetch` | Fetches tomorrow's precipitation probability and amount from a weather entity |

### Dashboard Views (`dashboards/`)

| File | Content |
|---|---|
| `feed_in_control_center.yaml` | Feed-in control panel — SOC, solar forecast, override controls |
| `max_feed_in_control_center.yaml` | Max feed-in power curve configuration |
| `overnight_charging_control_center.yaml` | Overnight charge window and SOC targets |
| `storm_mode_control_center.yaml` | Storm mode status and thresholds |
| `victron_overview_values.yaml` | System overview — battery, grid, solar, consumption |

> `victron_overview_values.yaml` contains `[SITE-SPECIFIC]` markers for sensors not provided by the package (e.g. VRM-derived daily energy totals). Replace or remove those cards as needed.

## Requirements

- **[ha-victron-ess-control](https://github.com/marisma-mhe/ha-victron-ess-control)** — provides all helpers and template sensors the blueprints depend on
- **HA MQTT Integration** — must be configured and connected to the same broker as the Victron GX device
- **[ha-victron-mqtt](https://github.com/tomer-w/ha-victron-mqtt)** (HACS) — Victron data source
- **Home Assistant 2024.6+**

Optional:
- **[Solcast Solar](https://github.com/BJReplay/ha-solcast-solar)** — solar forecast for overnight charging and feed-in blueprints
- Any `weather.*` entity — storm forecast fetch blueprint

## Installation

### Via HACS (recommended)

Add this repository to HACS as a custom repository (Blueprint category) and install **Victron ESS Frontend**.

HACS installs the blueprints automatically. Dashboard views must be added manually (see below).

### Manual

Copy `blueprints/automation/victron/` into your HA config's `blueprints/automation/victron/` directory. Restart HA or reload blueprints.

Each blueprint's `source_url` field also allows direct import via HA → Settings → Automations → Blueprints → Import Blueprint.

### Dashboard Views

The `dashboards/` files are Lovelace YAML panels. Add them as YAML-mode dashboards or paste card YAML into an existing dashboard view.

## Automation Setup (after install)

Create one automation instance per blueprint via Settings → Automations → Blueprints. Recommended order:

1. **Victron MQTT Keep-Alive** — one instance per GX device (required)
2. **Victron Daytime Window (Sun)** — one instance
3. **Victron Daytime Feed-In Control**
4. **Victron Max Feed-In Power Control**
5. **Victron Smart Overnight Charging**
6. **Victron Storm Mode Auto Control**
7. **Victron Storm Forecast Fetch**

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — Attribution, NonCommercial, ShareAlike.
