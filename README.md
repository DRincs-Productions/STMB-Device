# Navigation Quest Time Routine System for Ren'py

![Last commit](https://img.shields.io/github/last-commit/DRincs-Productions/STMB-Device)
![License](https://img.shields.io/github/license/DRincs-Productions/STMB-Device)
<span class="discord">
<a href="https://discord.gg/5UFPjP9" title="Discord"><img src="https://img.shields.io/discord/688162156151439536" alt="Discord" /></a>
</span>

**IMPORTANT**: is still in development

In order to simplify the update work and avoid errors in saving I created functions that check the correct state of variables by inserting them in [after_load](game/tool/core.rpy#L1) (e.g. after a change to a quest that causes a stage to be blocked, the quest should restart) and an abundant use of define.

Feel free to contribute, fork this and send a pull request. 😄

## Documentation

**[Wiki](https://github.com/DRincs-Productions/STMB-Device/wiki)**

## Code snippets ([VSCode](https://code.visualstudio.com/))

(all begin with `DR_`)

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/67595890/179365279-0d0b6d45-0048-4a0d-8c6d-9571b9c328f4.gif)

## Insert Toolkit in your project

I recommend the following ways to include it in your project:

- [**Pull branch**](#pull-branch) (to **insert** it into your game and **update** it easily)
- [**Fork**](https://docs.github.com/en/get-started/quickstart/fork-a-repo) (to improve the repo or create a Toolkit based on mine)
- [Manually](https://github.com/DRincs-Productions/STMB-Device/releases) (not recommended)

### Pull branch

To **insert** or **update** the Toolkit in your repo with Pull branch I recommend the following procedure:

(only if you want to insert the repo) Create a new empty branch, in the example I'll use **stmb-device**

```shell
git checkout -b stmb-device
git checkout stmb-device
git config pull.rebase false
git pull https://github.com/DRincs-Productions/STMB-Device.git tool-only --allow-unrelated-histories

```

At the end make a merge inside the arm of the project.

## Preview

