# Mark Activated Creation Club Plugin (MACCP)
A software to list all installed Creation Club content as activated inside the plugins.txt file.

## About the Program
I use Vortex mod manager and it lists all of the plugins I used inside the plugins.txt file, but it does not list the creation club content I have installed. This becomes an issue when I use mods like Everybody's Different for SSE that would list these plugins as deactivated and notify an error for missing masters.

This software will simply list all of the creation club content that you have and append them inside the plugins.txt file. Their load order will be preserved. If you use a mod manager like Vortex, everytime it tries to sort your plugins, the plugins.txt file will be overwritten and the creation club mods will be de-listed. Simply run the program again to get them back.

Currently supported games:
* Skyrim Special Edition
* Fallout 4 (untested)

## How to Use
1. Go to releases and download the .zip file.
2. Extract the contents into your computer somewhere
3. There should be a `config.ini` file and set the value for `Game` to the appropriate number. By default, it is set to `0` for `Skyrim Special Edition`.

```
0 = Skyrim Special Edition
1 = Fallout 4
```
4. Save the file and then run `main.exe`.

## Disclaimer
I don't know if there is any particular reason why Vortex does not the creation club plugins, so in case listing them causes issues simply force Vortex to sort your plugins again and the listed cc plugins will be removed.

For safety and in case of any issues, please back up your plugins.txt file before running the program. The program will also create a back up for you called `plugins_backup.txt`.

## Limitations and/or Known Bugs
- Running the program multiple times might cause the same list of CC plugins to be listed multiple times inside plugins.txt. This should pose no issue in flagging which plugin is activated (last in line takes precedence).
- Only SSE and Fallout 4 is currently supported (well those are the only games with creation club atm)
- Program will list all plugins that start with the lower case string "cc". Which means if there is a non-creation club mod that starts with these 2 characters they will be listed inside your plugin.txt as well as a possible duplicate, but that shouldn't mess up with your load order in any way.
- The created file backup simply copies the previous state of your `plugins.txt` file. So if the file was messed up before running the .exe, it will a copy of the broken file.
- The creation club plugins will be appended to the very top of your `plugins.txt` file.