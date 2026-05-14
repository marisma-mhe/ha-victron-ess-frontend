Automation blueprints and Lovelace dashboard views for Victron Energy ESS systems in Home Assistant.

> Install **[ha-victron-ess-control](https://github.com/marisma-mhe/ha-victron-ess-control)** first — it provides all helpers and sensors the blueprints depend on.

## Blueprints included

| Blueprint | Purpose |
|---|---|
| `victron_mqtt_keepalive` | Keeps VenusOS MQTT publishing active |
| `victron_daytime_feed_in_control` | Dynamic grid feed-in via `AcPowerSetPoint` |
| `victron_max_feed_in_power_control` | Voltage-curve based export cap |
| `victron_smart_overnight_charging` | SOC target from solar forecast, latest viable charge window |
| `victron_pre_midnight_charging_decision` | Decides whether to start charging before midnight |
| `victron_storm_mode_auto_control` | Auto-enables storm mode from rain/forecast |
| `victron_storm_forecast_fetch` | Fetches precipitation data from any `weather.*` entity |

## Dashboard views

5 Lovelace YAML panels: feed-in control, max feed-in, overnight charging, storm mode, system overview.

## Requirements

- **[ha-victron-ess-control](https://github.com/marisma-mhe/ha-victron-ess-control)** (this suite's companion integration)
- **[ha-victron-mqtt](https://github.com/tomer-w/ha-victron-mqtt)** (HACS)
- **Home Assistant 2024.6+**
