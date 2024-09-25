# My LaTeX note-taking template
---
Latex template for note-taking

# 1. Installation 
---
## 1.1. Install MikTex + Perl (for Windows)
- Install MikTex from [Link (MikTex)](https://miktex.org/download).
- Install Perl from [Link (Perl)](https://strawberryperl.com/).

## 1.2. Install Texlive (for Ubuntu)
```bash
sudo apt install texlive-science texlive-latex-extra texlive-extra-utils latexmk texlive-publishers texlive-science
```

# 3. Setting up VS-Code
---

## 3.1. Setting up output directory
- 1. Install Latex workshop plug-in.
- 2. Press `Ctrl` + `Shift` + `P` and search for `Open User Settings (UI)`.
- 3. Search for `latex OutDir`.
- 4. Key in `%DIR%/output` so that output is stored in `./output`.
- 5. Search for `Auto Clean`.
- 6. Set to `onBuilt`. 

## 3.2. Plugins
Install the following plugins:
- 1. `Latex Refs`.
- 2. `Latex Workshop`.

# 4. Setting up Sublime text
---
## 4.1. Install Sublime Text
This is a little bit easier than setting up vscode. Just install Sublime Text (for either Windows or Linx) then install the following packages:
- 1. `FileIcons`.
- 2. `LaTeX-cwl`.
- 3. `LaTeXTools`.
- 4. `Terminus`.
- 5. `Visual Studio Code Plus Scheme`.

Bonus package for productivity - `Pomodoro` and `PlainTasks`. Also, you can also go to `Preferences>Settings` and remove `Vintage` from the ignored packages section to enable Vim in Sublime Text.

For extra productivity, paste the sublime snippets in the `snippets` folder into the `Packages/User` folder of Sublime Text. You can also access this folder by `Tools>Developer>New Snippet...`.

## 4.2. Install SumatraPDF viewer
If we edit with Sublime, there will not be a built-in PDF viewer like VSCode. Therefore, an extra step is to install SumatraPDF (very lightweight):
- For Windows: [Link](https://www.sumatrapdfreader.org/download-free-pdf-viewer).
- For Linux: 
```bash
# If snap is not installed
sudo apt update
sudp apt install snapd 

# Install sumatra
sudo snap install sumatrapdf
```

