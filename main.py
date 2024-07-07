import decky_plugin
import os
import subprocess

MANGO_PRESETS_DIRECTORY_PATH = decky_plugin.DECKY_USER_HOME + "/.config/MangoHud" 
MANGO_PRESETS_FILE_PATH = MANGO_PRESETS_DIRECTORY_PATH + "/presets.conf"

PRESET_PERCENTAGE = """
[preset -1]
no_display=0
legacy_layout=0
background_alpha=0
battery
battery_icon=0
font_size=20
hud_compact
hud_no_margin
offset_x=-90
"""

PRESET_ICON = """
[preset -1]
no_display=0
legacy_layout=0
background_alpha=0
battery
battery_icon=1
font_size=20
hud_compact
hud_no_margin
offset_x=-90
"""

class Plugin:

    # Ensure Mangohud default config path exists
    async def _main(self):
        if not os.path.exists(MANGO_PRESETS_DIRECTORY_PATH):
            os.makedirs(MANGO_PRESETS_DIRECTORY_PATH)

    # Clear presets file if user decides to delete the plugin
    async def _unload(self):
        file = open(MANGO_PRESETS_FILE_PATH, 'w')
        file.write(" ")
        file.close()
        pass

    async def enable_icon_juice(self):
        try:
            decky_plugin.logger.debug("Applying icon preset file")

            file = open(MANGO_PRESETS_FILE_PATH, 'w')
            file.write(PRESET_ICON)
            file.close()

            Plugin.reload_mangohud_config()
            Plugin.overwrite_no_display()

        except Exception as e:
            decky_plugin.logging.error(e)

    async def enable_percentage_juice(self):
        try:
            decky_plugin.logger.debug("Applying % preset file")

            file = open(MANGO_PRESETS_FILE_PATH, 'w')
            file.write(PRESET_PERCENTAGE)
            file.close()

            Plugin.reload_mangohud_config()
            Plugin.overwrite_no_display()

        except Exception as e:
            decky_plugin.logging.error(e)

    async def disable_juice(self):
        try:
            decky_plugin.logger.debug("Clearing preset file")

            file = open(MANGO_PRESETS_FILE_PATH, 'w')
            file.write(" ")
            file.close()

            Plugin.reload_mangohud_config()

        except Exception as e:
            decky_plugin.logging.error(e)

    # Use '/usr/bin/mangohudctl' to reload the configs
    def reload_mangohud_config():
        try:
            bashCommand = "/usr/bin/mangohudctl set reload_config 1"
            process = subprocess.run(bashCommand, shell=True, executable='/bin/bash')
        except Exception as e:
            decky_plugin.logging.error(e)

    # Use '/usr/bin/mangohudctl' to disable the 'no_display' option in gamescope configs
    def overwrite_no_display():
        try:
            bashCommand = "/usr/bin/mangohudctl set no_display false"
            process = subprocess.run(bashCommand, shell=True, executable='/bin/bash')
        except Exception as e:

            decky_plugin.logging.error(e)
