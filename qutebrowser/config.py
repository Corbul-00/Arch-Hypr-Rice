#       Ayano's Purple Harmonic Rice
#     dark purple/pink/blue theme
# =====================================

#import dracula.draw  # optional - comment out if you don't want/need it

# ====================
# === Base settings ===
# ====================

config.load_autoconfig(False)          # We rice everything manually here

c.url.default_page = "https://startpage.com"
c.url.start_pages = ["https://startpage.com"]

c.editor.command = ["kitty", "nvim", "{file}"]   # or use your preferred terminal + nvim

# Use nvim-like defaults (qutebrowser already has very vim-like keys)
# We keep almost everything default, just add a few quality-of-life things
#config.unbind('x')          # unbind close tab by default if you want (optional)
config.unbind('<Ctrl-q>')   # sometimes people rebind quit

# ====================
# === Search engines ===
# ====================

c.url.searchengines = {
    "DEFAULT":  "https://www.startpage.com/do/dsearch?query={}",
    
    #YouTube
    "yt":       "https://www.youtube.com/results?search_query={}",
    
    #Arch Wiki
    "aw":       "https://wiki.archlinux.org/title/Special:Search?search={}",
    "arch":     "https://wiki.archlinux.org/title/Special:Search?search={}",
    
    #Reddit (subreddit search with +site:reddit.com)
    "r":        "https://www.reddit.com/search/?q={}",
    "reddit":   "https://www.reddit.com/search/?q={}",
    
    #Danbooru
    "d":        "https://danbooru.donmai.us/posts?tags={}",
    "dan":      "https://danbooru.donmai.us/posts?tags={}",
    
    #Github n wikippedia
    "gh":       "https://github.com/search?q={}&type=repositories",
    "wiki":     "https://en.wikipedia.org/wiki/Special:Search?search={}",
}

# Quick way to use them: type   !yt funny cats   → searches YouTube
# or just   yt funny cats   (without ! if you prefer)

# ====================
# === Colors (purple-pink-blue dark harmonic) ===
# ====================

# Main background (matches kitty)
c.colors.webpage.bg = '#2d1338'

# Force dark mode on websites (very important for purple rice)
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'smart'
c.colors.webpage.darkmode.contrast = 0.0     # tweak if too flat

# Statusbar / tabs / hints
c.colors.statusbar.normal.bg = '#2d1338'
c.colors.statusbar.normal.fg = '#d8c2f0'
c.colors.statusbar.insert.bg = '#4c1d95'     # darker purple insert mode
c.colors.statusbar.insert.fg = '#f5e1ff'
c.colors.statusbar.command.bg = '#2a2a6e'
c.colors.statusbar.command.fg = '#c4a0ff'
c.colors.statusbar.caret.bg = '#8b5cf6'
c.colors.statusbar.caret.fg = '#ffffff'
c.colors.statusbar.url.success.http.fg = '#c084fc'
c.colors.statusbar.url.success.https.fg = '#a78bfa'
c.colors.statusbar.url.error.fg = '#f87171'

# Tabs
c.colors.tabs.bar.bg = '#2a2a6e'             # matches kitty tab bg
c.colors.tabs.odd.bg = '#3b2852'
c.colors.tabs.odd.fg = '#d8c2f0'
c.colors.tabs.even.bg = '#3b2852'
c.colors.tabs.even.fg = '#d8c2f0'
c.colors.tabs.selected.odd.bg = '#8b5cf6'
c.colors.tabs.selected.odd.fg = '#ffffff'
c.colors.tabs.selected.even.bg = '#8b5cf6'
c.colors.tabs.selected.even.fg = '#ffffff'
#c.colors.tabs.pinned.selected.bg = '#6d28d9'
#c.colors.tabs.pinned.selected.fg = '#ffffff'

# Hints (the little letter popups)
c.colors.hints.bg = '#2d1338aa'              # semi-transparent purple
c.colors.hints.fg = '#f3e8ff'
c.colors.hints.match.fg = '#c084fc'          # highlighted matching letters

# Completion menu (when you type :open or o/O)
c.colors.completion.item.selected.bg = '#8b5cf6'
c.colors.completion.item.selected.fg = '#ffffff'
c.colors.completion.item.selected.match.fg = '#ffffff'
c.colors.completion.item.selected.border.top = '#8b5cf6'
c.colors.completion.item.selected.border.bottom = '#8b5cf6'
c.colors.completion.category.bg = '#2a2a6e'
c.colors.completion.category.fg = '#c4a0ff'
c.colors.completion.even.bg = '#35244a'
c.colors.completion.odd.bg = '#2d1338'

# Messages / prompts
c.colors.messages.info.bg = '#4c1d95'
c.colors.messages.info.fg = '#e9d5ff'
c.colors.messages.warning.bg = '#7c3aed'
c.colors.messages.warning.fg = '#ffffff'
c.colors.prompts.bg = '#2d1338'
c.colors.prompts.fg = '#d8c2f0'
c.colors.prompts.selected.bg = '#8b5cf6'

# Downloads
c.colors.downloads.bar.bg = '#2d1338'
c.colors.downloads.error.bg = '#f87171'

# Context menu / scrollbar etc.
c.colors.contextmenu.menu.bg = '#2d1338'
c.colors.contextmenu.menu.fg = '#d8c2f0'
c.colors.contextmenu.selected.bg = '#8b5cf6'

# ====================
# === Extra nice tweaks ===
# ====================

#c.content.javascript.can_access_clipboard = True   # modern sites need this
c.content.pdfjs = True                              # built-in pdf viewer
c.scrolling.bar = 'when-searching'                  # thin scrollbar only when needed
c.tabs.background = True                            # allow bg loading
c.tabs.last_close = 'blank'                         # or 'startpage' / 'default-page'
c.tabs.position = 'top'                             # or 'left' if you want vertical
c.tabs.show = 'always'
c.tabs.title.format = '{audio}{current_title}'
c.window.transparent = True                         # needs compositor (Hyprland ok)

# Optional: if you cloned dracula theme and want stronger purple-pink
# dracula.draw.blood(c, {
#     'spacing': {'vertical': 1, 'horizontal': 8}
# })

# Quick keybinds you might want (nvim style already exists)
config.bind('M', 'hint links spawn mpv {hint-url}')     # open video in mpv
config.bind('<Ctrl-r>', 'reload')                       # classic reload
#config.bind(',p', 'spawn --userscript qute-keepassxc')  # if you use keepassxc
