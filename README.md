# Nova Launcher

A modular Minecraft launcher UI built with Python + PyQt6 + qasync.

## Features

- Dark glassmorphism UI with neon blue/purple accents.
- Microsoft OAuth with PKCE through `minecraft-launcher-lib`.
- Offline/demo profile for local development/testing.
- Vanilla, Fabric, Forge and Quilt installation through `minecraft-launcher-lib`.
- Per-instance RAM, JVM arguments and resolution.
- Instance create/duplicate/delete.
- Modpack browser for Modrinth and CurseForge.
- Async `aiohttp` downloader with progress.
- News page and Discord card.
- Settings for Java path, background and accent colors.
- Small Python-side dependency footprint; Minecraft assets are stored separately.

## Important credentials

Microsoft login needs an Azure application/client ID and an allowed redirect URI.
The current code uses:

`http://127.0.0.1:8765/callback`

Set `NOVA_MICROSOFT_CLIENT_ID` in the environment or `.env`-style configuration you use.

CurseForge requires a valid API key. Set `NOVA_CURSEFORGE_API_KEY`.

Do not hard-code secrets into source control.

## Run

Python 3.10-3.13 is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

If Microsoft OAuth is not configured, use Offline / Demo login. That profile is intended for development/testing only; it is not a substitute for owning/authenticating Minecraft.

## Project layout

- `main.py` - application entry point.
- `nova/config.py` - paths, persistent settings and credentials.
- `nova/auth.py` - Microsoft PKCE flow + offline profile.
- `nova/launcher.py` - Minecraft install/launch operations.
- `nova/downloader.py` - async multi-download helper.
- `nova/apis.py` - Modrinth, CurseForge and news clients.
- `nova/instances.py` - instance persistence.
- `nova/ui.py` - complete PyQt6 UI.

## API notes

Modrinth is queried through its public v2 API. CurseForge is queried through its API and therefore needs an API key.

`minecraft-launcher-lib` supplies the Minecraft installation, loader installation and command generation layer, while qasync keeps blocking launcher-lib operations off the Qt UI thread.


## Packaging / size

The Python source is intentionally modular and lightweight. A packaged desktop
application will also contain the Qt runtime and Python runtime, so the final
installer size depends on the PyInstaller/packaging configuration and platform.
The "under 100MB" goal is therefore a source/dependency architecture goal, not
a guaranteed final binary size.

## CurseForge modpacks

CurseForge modpacks are handled as their standard `manifest.json` + `overrides`
ZIP format. The launcher resolves manifest file IDs through the CurseForge API,
downloads required files, installs the selected loader, then applies overrides.
