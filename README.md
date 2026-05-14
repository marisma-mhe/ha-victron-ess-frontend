# ha-victron-ess-frontend

Lovelace dashboard views for Victron Energy ESS systems in Home Assistant.

> **Blueprints and the integration are in [ha-victron-ess-control](https://github.com/marisma-mhe/ha-victron-ess-control) — install that first.**

## Dashboard Views

| File | Content |
|---|---|
| `feed_in_control_center.yaml` | Feed-in control panel — SOC, solar forecast, override controls |
| `max_feed_in_control_center.yaml` | Max feed-in power curve configuration |
| `overnight_charging_control_center.yaml` | Overnight charge window and SOC targets |
| `storm_mode_control_center.yaml` | Storm mode status and thresholds |
| `victron_overview_values.yaml` | System overview — battery, grid, solar, consumption |

> `victron_overview_values.yaml` contains `[SITE-SPECIFIC]` markers for sensors not provided by the package (e.g. VRM-derived daily energy totals). Replace or remove those cards as needed.

## Installation

The `dashboards/` files are Lovelace YAML panels. Add them as YAML-mode dashboards or paste card YAML into an existing dashboard view.

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — Attribution, NonCommercial, ShareAlike.
