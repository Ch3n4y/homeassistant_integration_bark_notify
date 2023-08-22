# Bark Notify Integration for Home Assistant

This integration allows Home Assistant users to send notifications through the Bark app.

## Installation

1. Clone this repository or download the source code.
2. Move the `bark_notify` folder into the `custom_components` directory of your Home Assistant installation.
3. Restart Home Assistant.

## Configuration

To enable the `bark_notify` integration, add the following lines to your `configuration.yaml` file:

```yaml
notify:
  - platform: bark_notify
    key: YOUR_BARK_KEY
    sound: OPTIONAL_SOUND
    icon: OPTIONAL_ICON_URL
    group: OPTIONAL_GROUP
    level: OPTIONAL_LEVEL
    badge: OPTIONAL_BADGE_NUMBER
    autoCopy: OPTIONAL_AUTO_COPY_FLAG
    copy: OPTIONAL_COPY_TEXT
```

Replace `YOUR_BARK_KEY` with your Bark key from the Bark app. All other parameters are optional.

### Configuration Parameters:

- `key`: **Required.** Your Bark key from the Bark app.
- `sound`: Optional. A custom sound for the notification.
- `icon`: Optional. A URL for a custom icon for the notification.
- `group`: Optional. A group name for grouping notifications.
- `level`: Optional. Notification interrupt level. Can be 'active', 'timeSensitive', or 'passive'.
- `badge`: Optional. A number for the notification badge.
- `autoCopy`: Optional. Boolean flag to auto copy the notification content.
- `copy`: Optional. Specify content to be copied when the notification is copied.

## Usage

Once configured, you can call the `bark_notify` service to send notifications:

```yaml
service: notify.bark_notify
data:
  message: "Your message here"
  title: "Optional title here"
  data:
    sound: "OPTIONAL_SOUND_OVERRIDE"
    ...
```

You can override any of the optional parameters from the configuration in the `data` dictionary when calling the service.

## Support & Contribution

- Issue Tracker: [https://github.com/Ch3n4y/homeassistant_integration_bark_notify/issues](https://github.com/Ch3n4y/homeassistant_integration_bark_notify/issues)
- Source Code: [https://github.com/Ch3n4y/homeassistant_integration_bark_notify](https://github.com/Ch3n4y/homeassistant_integration_bark_notify)

Feel free to open issues for feedback or submit pull requests for improvements and bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file in the repository for more details.

---

Hope you find this integration helpful in integrating Bark with Home Assistant! If you have any questions or need further assistance, don't hesitate to ask. Safe automating! 🏠🤖
