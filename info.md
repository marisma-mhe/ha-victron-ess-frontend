Lovelace dashboard views for Victron Energy ESS systems in Home Assistant.

> Install **[ha-victron-ess-control](https://github.com/marisma-mhe/ha-victron-ess-control)** first — it provides all helpers, sensors, and automation blueprints.

## Dashboard views

| File | Content |
|---|---|
| `feed_in_control_center.yaml` | Feed-in control panel — SOC, solar forecast, override controls |
| `max_feed_in_control_center.yaml` | Max feed-in power curve configuration |
| `overnight_charging_control_center.yaml` | Overnight charge window and SOC targets |
| `storm_mode_control_center.yaml` | Storm mode status and thresholds |
| `victron_overview_values.yaml` | System overview — battery, grid, solar, consumption |

## Requirements

- **[ha-victron-ess-control](https://github.com/marisma-mhe/ha-victron-ess-control)** (provides helpers, sensors, and blueprints)
- **[ha-victron-mqtt](https://github.com/tomer-w/ha-victron-mqtt)** (HACS)
- **Home Assistant 2024.6+**
