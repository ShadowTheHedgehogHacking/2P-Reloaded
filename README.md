<div align="center"><h1>2P Reloaded</h1>
<img src="https://raw.githubusercontent.com/ShadowTheHedgehogHacking/2P-Reloaded/main/code/res/title_screen.jpg" align="center" />
</div>

## About
This project is a combination of the [2P-ShdTH](https://github.com/ShadowTheHedgehogHacking/2P-ShdTH) and [ShdTH-Reloaded](https://github.com/ShadowTheHedgehogHacking/ShdTH-Reloaded) mods with full feature parity

Experience all the enhancements of the Reloaded project with 2 players in Story Mode, Select Mode, Expert Mode, and Last Story

## Important
* You must set Dolphin to use 64MB of RAM to play this mod. This is done automatically if you add the `GUPR8P.ini` file
* If you are playing on a real Wii/GameCube, you must apply the `console` variant of the mod, which reduces texture sizes to have mostly stable gameplay with only 24MB of RAM
* You can change characters. Select 2P-VS, select characters, then back out to the main menu at the 1-3 round select screen. Your character choices will carry over to 2P CO-OP
* Original Game 2P - If you are looking to play the original game but in 2P, go here: [2P-ShdTH](https://github.com/ShadowTheHedgehogHacking/2P-ShdTH)

## How to play / Setup
### ROM Validation
This mod is only compatible with Shadow: Reloaded v1.2 ROM. 

Verify the ROM you are attempting to patch is a 1:1 Shadow: Reloaded v1.2 Widescreen GameCube ISO.
If you have the original game, you can make a Shadow Reloaded v1.2 ISO by patching it here: [ShdTH-Reloaded](https://github.com/ShadowTheHedgehogHacking/ShdTH-Reloaded)

GCZ/WIA/RVZ or any other format than ISO is not supported. Please convert to ISO, then compare your game to the table below

You can convert your RVZ game by right-clicking your game in Dolphin's game list -> `Convert File...`

You can check your hashes by right-clicking your game in Dolphin's game list -> `Properties` -> `Verify` tab

| ROM    | CRC32 Hash    | SHA-1 Hash                               |
| ------ | ------------- | ---------------------------------------- |
| RELOADED WIDESCREEN | 608b69c4      | 246329735cd79fd0fe187c61b94487e75c42f1b7 |

### Summary
0. Create a [Shadow Reloaded v1.2 WIDESCREEN ROM](https://github.com/ShadowTheHedgehogHacking/ShdTH-Reloaded) from your original game, if you haven't. The 2P patch applies to this rom.
1. Patch your RELOADED WIDESCREEN ISO with the .xdelta of your choice
2. Dolphin: Ensure you placed `GUPR8P.ini`, Enabled Cheats, and set Force Aspect ratio
3. Nintendont: Ensure you placed `GUPR8P.gct` file next to `game.iso`, In Nintendont configuration, set `Cheats ON` and `Unlock Read Speed ON`
4. Play! See below for detailed steps

### Patching
#### Note: You need the `GUPR8P.ini` file for the mod to work properly, running just the ISO will not work! If you follow Step 4. of the Dolphin setup, this is part of the `GameSettings` folder merge step.
1. Download [the latest release from here](https://github.com/ShadowTheHedgehogHacking/2P-Reloaded/releases) and extract it somewhere you can access easily
2. Visit https://shadowthehedgehoghacking.github.io/xdelta-wasm/ or any other xdelta3 patcher of your choice
3. Select your Reloaded v1.2 Widescreen ISO as the `Source file`
4. Select the `2P-Reloaded-[version]-[aspect]-[variant].xdelta` file from `Patches` as the `Patch file`. Use `console` variants if playing on real hardware. Use `64M` variants if playing on Dolphin
5. Click `Apply Patch`: It will then 'download' the patched file as `ISO NAME-patched.iso` (nothing is actually uploaded/downloaded, it is all done on-device)
6. If you run into errors, likely the ISO is wrong hash for the xdelta you downloaded. Double check your Reloaded v1.2 Widescreen ISO in `Dolphin Verify` tab
7. If you want to make additional modifications (such as CharacterMods) follow [Extra Mods](#extra-mods)

Expected Patch Results (v2.5)

| PATCH              | CRC32 Hash    | SHA-1 Hash                               |
| ------------------ | ------------- | ---------------------------------------- |
| 64M-WIDESCREEN     | 2e4dfe13      | d49b6efa1bd3c8a8fa4b1cc53ebc6ee0ed2998e6 |
| CONSOLE-WIDESCREEN | 5c9694ef      | e9c07bc47a601b9a17ac7b612baa8e1770993bc2 |
| 64M                | 0cc8b037      | f77a1c7d4b4159733c36615284396f18c53579be |
| CONSOLE            | be5313a4      | d03bc407b8ad55798ffd8dc572d050f83e24a4f8 |

### Dolphin
1. Get the latest Dolphin Emulator - [Dolphin 2506 or newer](https://dolphin-emu.org/download/)
2. (Optional) We recommend keeping a separate Dolphin instance just for this mod. Before launching Dolphin, create an empty file `portable.txt` in the same folder as `Dolphin.exe`
3. Launch Dolphin. On Dolphin's menu bar, click `File` -> `Open User Folder`. The folder that appears is your `<Dolphin User Folder>` in the below steps
4. Copy/Move the two folders (`GameSettings` and `Load`) in `Dolphin Configuration (Required)` to `<Dolphin User Folder>`
5. Move/Save the patched ISO you created earlier to the Path Dolphin detects your games. A new 2P Reloaded Mod Shadow entry should appear in your Dolphin game list, with greater than 0 filesize, and with a custom banner. Use this when playing the game
6. If the game does not appear as you expect, select `View` -> `Purge Game List Cache` from Dolphin's menu bar
7. Enable Cheats in `Dolphin -> Config`. Right click the game the list and choose `Properties -> Gecko Codes` to change any configuration codes
8. Under `Dolphin -> Config -> Advanced` enable `CPU Clock Override` and try various values (CPU dependent). I highly recommend at least `150%` if your CPU can handle it. See [Dolphin FPS optimization (CPU variable)](#dolphin-fps-optimization) 
9. Set Aspect Ratio in `Dolphin -> Graphics -> Aspect Ratio` to `Force 16:9` or `Stretch to Window` if playing in Widescreen. Set it to `Force 4:3` if playing in Original Aspect Ratio
10. (Optional) To enable Custom Textures: `Dolphin -> Graphics -> Advanced` Enable `Load Custom Textures` and `Prefetch Custom Textures`
11. (Optional) If you want to use the 100% Save, place `8P-GUPR-SHADOWRELOADED.gci` GCI file at `<Dolphin User Folder>\GC\USA\Card A\` - This is already done if you copy the Dolphin Configuration (Optional) folder, like in step 4

### Nintendont (Wii/Wii U)
1. If you want to customize cheats for Nintendont, use [CodeManager2](https://github.com/CLF78/CodeManager2) with GUPR8P.ini to generate your own `.gct` for Nintendont. A GCT is **required** as the split screen codes are exclusive to these
2. Rename your patched ISO to `game.iso` and place it on your Nintendont SD/USB
3. For convenience, the release includes pre-built GCTs for Widescreen and Original Aspect in both Vertical and Horizontal split screen modes. If creating your own GCT file and playing with Original Aspect Ratio, you should disable the `(Widescreen)` code
```
Copy GUPR8P.gct to the same directory as your game.iso
 e.g. USB:/games/2P Shadow Reloaded [GUPR8P] should have:
   game.iso
   GUPR8P.gct
 in the folder.
Copy 'saves' folder to root of USB or SD (same one where game is)
Nintendont should be configured as follows for the best experience:
   Cheats ON
   Unlock Read Speed ON
 Optional:
   Memcard Emulation ON (If you want to use provided 100% save)
   Video Width (Set to whatever fills your screen without black bars, in my case it was 714)
``` 

### Dolphin FPS Optimization
`Config` -> `Advanced` -> `CPU Clock Override slider` 
```
Adjust clockspeed while running the game

I recommend loading in Glyphic Canyon, have one player stay at the start,
have the other go to the first area with enemies and Knuckles
Try adjusting the slider here to reach 60fps. It will be ~30fps with default 100% clock

It varies per system, some run better with underclock/overclock

I recommend trying 80%, 150%, 200%, 220%, 250%, 270%, 290%, 300% 
Note: Higher clockspeeds may result in audio distortions if your system can't keep up
If audio distortions occur, lower the clockspeed
I use 290% for AMD Ryzen 9 5900X. Previously 217% for AMD Ryzen 7 3800X, 165% for Intel i5-3570k
```

### Extra Mods
After you've patched your ISO with the chosen xdelta, you can make additional modifications. Follow the steps below to use mods such as Sonic over Yellow Android

### Extraction of Game / Extracted Game Format
1. Open Dolphin
2. Right-click your 2P-Reloaded ISO you created in the game list
3. Select Properties
4. Select FileSystem Tab
5. Right-click "Disc"
6. Select Extract Entire Disc...
7. Select a new folder where you will store the game content and modify its files

### Replacement of Files & Converting Extracted Game to ISO
1. Open the newly extracted folder and make any additional changes you want, such as Sonic over Yellow Android, other [CharacterMods](https://github.com/ShadowTheHedgehogHacking/CharacterMods), or any other changes you want
2. Open Dolphin
3. Open Config
4. Select Paths Tab
5. Select "Add" for Game Folders
6. Navigate to the folder where you extracted the game
7. Open the `sys` folder, and select "Select Folder"
8. Close the confirmation pane, your games list should populate a new 0 filesize game of Shadow The Hedgehog. The 0 filesize entry is the Extracted Game format game
9. Right click the Extracted Game format game and pick `Convert File...`
10. The Convert window will appear, click "Convert..." and name it `game.iso` for Nintendont, or `2PReloaded.iso` for Dolphin
11. Move/Save the ISO to the Path Dolphin detects your games. A new 2P Reloaded Mod Shadow entry should appear in your Dolphins game list with greater than 0 filesize and with a custom banner. Use this when playing the game
12. If the game does not appear as you expect, in Dolphin's menu bar select `View` -> `Purge Game List Cache`

## Troubleshooting / FAQ
1. Player 2 does not spawn, but a split screen appears
* You have successfully placed `GUPR8P.ini` as you expect, but are launching the wrong game or improperly patched the game
2. Player 2 spawns, but there is no split screen for them
* You have patched the game correctly, but `GUPR8P.ini` is not placed in the correct spot, or Cheats are disabled in Dolphin/Nintendont
3. I keep crashing after the Rank Screen completes on finishing a level
* If you are using a Custom BON character with the `Yellow Android MTP Animation Override` code, make sure you enabled the `Custom MTP Crash Fix v4` code too.
4. I get `Load failed. Please check the Memory Card` message when loading the game
* Ensure you did not accidentally enable/check a separator in the Gecko Codes list, such as `=== Core Codes ===`, `=== Gameplay Tweaks ===` - these are not codes, just separators and should not be enabled.
* Make sure you did not copy a Shadow SX or Original save file. Only Shadow Reloaded v1.2 game saves are compatible.
5. The aspect ratio switches between 4:3 and 16:9 when someone uses Chaos Control
* Ensure you are on Dolphin 2506 or newer. Pick `Force 16:9`, `Stretch to Window`, or `Force 4:3`.
6. My game runs at very low FPS
* This mod is very CPU intensive and requires overclocking the virtual GameCube CPU. Nintendont on Wii is the equivalent of a 150% GameCube CPU Overclock. I recommend at least matching this in Dolphin, but ultimately it depends on your own real CPU's power. See the [Dolphin FPS Optimization](https://github.com/ShadowTheHedgehogHacking/2P-Reloaded/tree/main?tab=readme-ov-file#dolphin-fps-optimization) section above.
7. I have a 16:9 monitor, and am using the widescreen version of the game, but I have black bars on the sides
* Shadow the Hedgehog and Sonic Heroes have an abnormal aspect ratio. You need to either enable `Stretch to Window` with `Dolphin Widescreen Hack` option, or enable `Crop` in `Graphics -> Advanced` if using `Force 16:9` option
8. My screen explodes with weird textures everywhere
* Do not use the Dolphin `Graphics Mods` -> `Bloom Removal` feature. Instead use the included Gecko Code if you want No Bloom
9. My Wii / Wii U shuts down when loading a stage (Nintendont)
* Update your Nintendont to at least `v6.503 / Apr 30 2025 20:50:09`
10. Both players are being controlled by one controller
* You need to ensure the `START` button is not pressed at the same time on multiple controllers during stage load. In Dolphin make sure you haven't accidentally bound `START` to the same key/controller by mistake.
11. How do I play with others?
* This is a local splitscreen modification. Outside of playing in the same physical space, you can either use Dolphin Netplay with Dual Core OFF (it crashes with it ON), or a cloud gaming solution such as [Parsec](https://parsec.app), [Sunshine/Moonlight](https://app.lizardbyte.dev/Sunshine), [Steam Remote Play](https://store.steampowered.com/remoteplay).
12. I have texture corruption or Dolphin crashes.
* Use Vulkan Graphics backend. Do not use Direct3D 12, as it has crashing issues in Dolphin with this game. Direct3D 11 will sometimes corrupt textures (nvidia only).
13. My game crashed (PPC Halt noise) while playing on console via Nintendont
* If you travel far apart in some stages, it is still possible to exceed 24M and crash the game on console. This should be rare, but if it happens just avoid splitting up in the areas you commonly crash in.
14. My game looks stretched or squished
* Set Aspect Ratio in `Dolphin -> Graphics -> Aspect Ratio` to `Force 16:9` or `Stretch to Window` if playing in Widescreen. Set it to `Force 4:3` if playing in Original Aspect Ratio.

## Credits
* See [2P-ShdTH](https://github.com/ShadowTheHedgehogHacking/2P-ShdTH?tab=readme-ov-file#credits) and [ShdTH-Reloaded](https://github.com/ShadowTheHedgehogHacking/ShdTH-Reloaded?tab=readme-ov-file#credits) repos

## A Notice to Modders
Anyone is free to base mods off this project. If you make a new mod based on it or create something that has 2P-Reloaded support, we would love to see it!
You do not need to ask permission to make mods built off this mod or other derivative works.

[See the original 2P-ShdTH repo to learn how to build from source (not recommended for most users)](https://github.com/ShadowTheHedgehogHacking/2P-ShdTH/tree/master/code)
