# Scripts

## Daily sync to GitHub

`daily-sync-to-github.sh` commits and pushes this project to GitHub once per day via macOS launchd.

- **Schedule:** 9:00 AM every day (configure in `~/Library/LaunchAgents/com.charlie.pm-brain-daily-sync.plist`)
- **Log:** `scripts/daily-sync.log`

### Enable the daily job

```bash
launchctl load ~/Library/LaunchAgents/com.charlie.pm-brain-daily-sync.plist
```

### Disable

```bash
launchctl unload ~/Library/LaunchAgents/com.charlie.pm-brain-daily-sync.plist
```

### Run manually

```bash
./scripts/daily-sync-to-github.sh
```

### Change the time

Edit `~/Library/LaunchAgents/com.charlie.pm-brain-daily-sync.plist`: change the `Hour` and `Minute` under `StartCalendarInterval`, then run `launchctl unload` and `launchctl load` again.
