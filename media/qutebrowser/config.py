import subprocess
import os
from qutebrowser.api import interceptor
# from itertools import product
# from random import shuffle

# flake8: noqa

# Autogenerated config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://drive.google.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Switch to insert mode when clicking flash and other plugins.
# Type: Bool
#c.input.insert_mode.plugins = True

# === My Configs ===

config.load_autoconfig(False)

## Unbind stuff in normal mode
config.unbind('wi')
config.unbind('m')
config.unbind('<Ctrl-Tab>')
config.unbind('<Ctrl-t>')
config.unbind('<Ctrl-n>')
config.unbind('<Ctrl-Shift-n>')
config.unbind('<Ctrl-w>')
config.unbind('<Ctrl-Shift-w>')
config.unbind('<Ctrl-PgDown>')
config.unbind('<Ctrl-PgUp>')
config.unbind('<F5>')
config.unbind('<Ctrl-F5>')
config.unbind('<Back>')
config.unbind('<Forward>')
config.unbind('<F11>')
config.unbind('<Ctrl-Shift-t>')
config.unbind('<Ctrl-Shift-Tab>')
config.unbind('<Ctrl-^>')
config.unbind('<Alt+1>')
config.unbind('<Alt+2>')
config.unbind('<Alt+3>')
config.unbind('<Alt+4>')
config.unbind('<Alt+5>')
config.unbind('<Alt+6>')
config.unbind('<Alt+7>')
config.unbind('<Alt+8>')
config.unbind('<Alt+9>')
config.unbind('<Ctrl-h>')
config.unbind('<Ctrl-s>')
config.unbind('<Ctrl-Alt-p>')
config.unbind('<Ctrl-p>')
config.unbind('<Ctrl-Q>') # :q should be enough
config.unbind('ad') # download cancel
config.unbind('cd') # download clear
config.unbind('g$') # tab-focus -1 (<Ctrl-0> should be enough)
config.unbind('g0') # tab-focus 1 (<Ctrl-1> should be enough)
config.unbind('g^') # tab-focus 1 (<Ctrl-1> should be enough)
config.unbind('ga') # open -t (O + <Enter> should be enough)
config.unbind('gb') # bookmark-load (i'll deal with bookmarks later when i install buku)  !!!!!!!!!
config.unbind('gB') # bookmark-load -t (i'll deal with bookmarks later when i install buku)  !!!!!!!!
config.unbind('gC') # tab-clone
config.unbind('gd') # download
config.unbind('gD') # tab-give
config.unbind('gf') # view source (i don't know what to do with it yet) !!!!!! ALERT!!!!!
config.unbind('gm') # tab-move
config.unbind('gO') # set-cmd-text :open -t -r {url:pretty}
config.unbind('go') # set-cmd-text :open {url:pretty}
config.unbind('gt') # set-cmd-text -s :buffer
config.unbind('gU') # navigate up -t
config.unbind('co') # tab-only
config.unbind('J')
config.unbind('K')
config.unbind('r') # Prevent accidental reloads
config.unbind('R') # Prevent accidental reloads
config.unbind('xo') # set-cmd-text -s :open -b
config.unbind('xO') # set-cmd-text :open -b -r {url:pretty}
config.unbind('d') # tab-close
#config.unbind('e') # just in case
config.unbind('j') # enable keydrown
config.unbind('k') # enable keydrown
config.unbind('D') # tab-close -o
config.unbind('th') # back -t
config.unbind('tl') # forward -t
config.unbind('o') # open
config.unbind('O') # open -t
config.unbind('wh') # back -w
config.unbind('wl') # forward -w
config.unbind('.') # repeat last action (it may be problematic with russian layout
c.bindings.key_mappings = {} # Unmap <Ctrl-[> so codemirror can use it

# Make normal mode language agnostic
en_symbols = list("qwertyuiop[]asdfghjkl;'zxcvbnm,.QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>")
ru_symbols = list("йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ")
c.bindings.key_mappings = dict(zip(ru_symbols, en_symbols))
for i in range(32):
    c.bindings.key_mappings['<Alt-' + ru_symbols[i] + '>'] = '<Alt-' + en_symbols[i] + '>'

c.bindings.key_mappings['<Ctrl-J>'] = '<Return>'
c.bindings.key_mappings['<Ctrl-M>'] = '<Return>'
c.bindings.key_mappings['<Enter>'] = '<Return>'

# Merge windows
config.bind('__', 'set-cmd-text -s :tab-take ;; later 10 fake-key --global <Tab> ;; later 10 fake-key --global <Return>')

# The "dunder" bindings

# Command chaining (_ = dunder, c = command chain, next two digits = id of chain, last digit = id of command in chain)
# NOTE "Command chaining" is my workaround for inability of some commands (like jseval) to have additional commands chained after them normally (i.e. with ;;)

# _c01: do stuff respecting the current (i3) layout (i.e. in this same workspace), and change wm_class
config.bind('_c010', 'spawn -d /home/boris/bin/i3/set-respect-layout.sh')
config.bind('_c011', 'devtools window ;; later 300 spawn -d /home/boris/.local/share/qutebrowser/userscripts/change-wm-class.sh')
config.bind('_c012', 'spawn -d qutebrowser --basedir /home/boris/qutebrowser-profiles/tiddlywiki/ --qt-arg name tiddlywiki')
config.bind('_c013', 'spawn i3-msg "mark --toggle inspect"')

# _c02: click on a dummy div
config.bind('_c020', 'jseval -q tmp=document.createElement("div");document.body.appendChild(tmp);tmp.setAttribute("id", "0");')  # Create a <div_id="0">
config.bind('_c021', 'click-element id 0 ;; jseval -q document.getElementById("0").remove();')  # Click this div
config.bind('_c022', 'later 30 click-element id 0')  # Clisk this div a few ms later

# _c03: state for keydrown
config.bind('_c030', 'jseval -q -w main window.qutebrowserMode = "insert";')
config.bind('_c031', 'hint inputs')

# Domain keychains: TiddlyWiki (prefix _d44tw, where _ = dunder, d = domain, 44 = ASCII code of comma (i.e. the key that is dispatched), tw = tiddlywiki ) ! I had to use ascii code instead of the character itself, because when xdotool types it, it collides with the actual key pressed by me.. digits are safe since they're not used in keychains usually.
# NOTE "Domain keychains" is my (ugly and dirty) workaround the absence of the native domain-specific keybindings

# Domain keychains: youtube (prefix _dyt, where _ = dunder, d = domain, yt = youtube)
config.bind('_d44yt0', 'seek_0%')
c.aliases['seek_0%'] = 'fake-key 0'
config.bind('_d44yt1', 'fake-key 1')
config.bind('_d44yt2', 'fake-key 2')
config.bind('_d44yt3', 'fake-key 3')
config.bind('_d44yt4', 'fake-key 4')
config.bind('_d44yt5', 'fake-key 5')
config.bind('_d44yt6', 'fake-key 6')
config.bind('_d44yt7', 'fake-key 7')
config.bind('_d44yt8', 'fake-key 8')
config.bind('_d44yt9', 'fake-key 9')
config.bind('_d44ytc', 'fake-key c')
config.bind('_d44ytt', 'fake-key t')
config.bind('_d44ytf', 'fake-key f ;; spawn i3-msg fullscreen disable')
config.bind('_d44yti', 'fake-key i')
config.bind('_d44yt/', 'fake-key /')
config.bind('_d44yt,', 'fake-key <Shift-,>')
config.bind('_d44yt.', 'fake-key <Shift-.>')
config.bind('_d44yts', 'hint yt-skip-ad')

# Aliases
c.aliases['yt-hide'] = 'jseval document.querySelector("#container.style-scope.ytd-masthead").style.display="none";'
c.aliases['yt-show'] = 'jseval document.querySelector("#container.style-scope.ytd-masthead").style.display="block";'
c.aliases['stylesheets-gruvbox'] = 'set content.user_stylesheets "~/.local/share/qutebrowser/stylesheets/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css"'
c.aliases['stylesheets-darculized'] = 'set content.user_stylesheets "~/.local/share/qutebrowser/stylesheets/solarized-everything-css/css/darculized/darculized-all-sites.css"'
c.aliases['stylesheets-solarized-dark'] = 'set content.user_stylesheets "~/.local/share/qutebrowser/stylesheets/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css"'
c.aliases['stylesheets-solarized-light'] = 'set content.user_stylesheets "~/.local/share/qutebrowser/stylesheets/solarized-everything-css/css/solarized-light/solarized-light-all-sites.css"'
c.aliases['stylesheets-apprentice'] = 'set content.user_stylesheets "~/.local/share/qutebrowser/stylesheets/solarized-everything-css/css/apprentice/apprentice-all-sites.css"'
c.aliases['stylesheets-off'] = 'set content.user_stylesheets ""'
c.aliases['merge-windows'] = 'fake-key --global _c020_c020_c020_c020'
c.aliases['noh'] = 'search'
c.aliases['bindings'] = 'open qute://bindings/'
c.aliases['bookmarks'] = 'open qute://bookmarks/'
c.aliases['version'] = 'open qute://version/'
c.aliases['buku-add'] = 'spawn buku -a {url}'
c.aliases['buku-load'] = 'spawn buku_run'

# Search engines
c.url.searchengines['google'] = "https://www.google.com/search?q={}"
c.url.searchengines['youtube'] = "https://www.youtube.com/search?q={}"
c.url.searchengines['reddit'] = "https://www.reddit.com/search?q={}"
c.url.searchengines['stackoverflow'] = "https://www.stackoverflow.com/search?q={}"
c.url.searchengines['math.stackexchange'] = "https://math.stackexchange.com/search?q={}"
c.url.searchengines['askubuntu'] = "https://askubuntu.com/search?q={}"
c.url.searchengines['wikipedia'] = "https://wikipedia.org/wiki/{}"
c.url.searchengines['emuparadise'] = "https://www.emuparadise.me/roms/search.php?query={}"
c.url.searchengines['python.org'] = "https://www.python.org/search/?q={}"
c.url.searchengines['greasespot'] = "https://wiki.greasespot.net/index.php?title=Special%3ASearch&search={}&go=Go"
c.url.searchengines['greasyfork'] = "https://greasyfork.org/en/scripts?q={}"
c.url.searchengines['openuserjs'] = "https://openuserjs.org/?q={}"
c.url.searchengines['svg-wikimedia'] = "https://commons.wikimedia.org/w/index.php?sort=relevance&search={}+filemime%3Aimage%2Fsvg%2Bxml&title=Special:Search&profile=advanced&fulltext=1&advancedSearch-current=%7B%22fields%22%3A%7B%22filetype%22%3A%22image%2Fsvg%2Bxml%22%7D%7D&ns0=1&ns1=1&ns2=1&ns3=1&ns4=1&ns5=1&ns6=1&ns7=1&ns8=1&ns9=1&ns10=1&ns11=1&ns12=1&ns13=1&ns14=1&ns15=1&ns100=1&ns101=1&ns102=1&ns103=1&ns104=1&ns105=1&ns106=1&ns107=1&ns460=1&ns461=1&ns486=1&ns487=1&ns490=1&ns491=1&ns828=1&ns829=1&ns1198=1&ns1199=1&ns2300=1&ns2301=1&ns2302=1&ns2303=1"
c.url.searchengines['github'] = "https://github.com/search?q={}"
c.url.searchengines['translate:ru-to-en'] = "https://translate.google.com/#view=home&op=translate&sl=ru&tl=en&text={}"
c.url.searchengines['translate:en-to-ru'] = "https://translate.google.com/#view=home&op=translate&sl=en&tl=ru&text={}"

# Characters used for hint strings
# c.hints.chars = "sfgwrtuiocvnm.23489"
c.hints.chars = "sfgwrtuiocvnm23489"

# Add hints selectors
c.hints.selectors['paragraphs'] = ['div, span, p, ol, ul, li, h1, h2, h3, h4, h5, h6, pre, td, dt, dd']
c.hints.selectors['alll'] = ['*']
c.hints.selectors['yt'] = ['yt-formatted-string']
c.hints.selectors['yt-video'] = ['video']
c.hints.selectors['all'].append('yt-formatted-string')
c.hints.selectors['all'].append('h3 span')
c.hints.selectors['all'].append('span.qt_read_more')   # the fucking quora's read button!
c.hints.selectors['tables'] = ['table']
c.hints.selectors['pre'] = ['pre']
c.hints.selectors['folder'] = ['svg.tc-image-folder']
c.hints.selectors['select'] = ['select']
c.hints.selectors['frame'] = [ 'div', 'header', 'section', 'nav']
c.hints.selectors['div'] = ['div']
c.hints.selectors['header'] = ['header']
c.hints.selectors['section'] = ['section']
c.hints.selectors['nav'] = ['nav']
c.hints.selectors['yt-skip-ad'] = ['button.ytp-ad-skip-button']
c.hints.selectors['iframe'] = ['iframe#mainframe']
c.hints.selectors['text'] = ['#text']
config.bind('a', 'spawn /home/boris/.local/share/qutebrowser/userscripts/run-keynav.sh')

# Open base URL of a search engine if no search terms
c.url.open_base_url = True

config.set('tabs.mode_on_change', 'restore')
config.set('tabs.last_close', 'close')
config.set('tabs.max_width', 200)
config.set('downloads.position', 'bottom')

c.messages.timeout = 3000
c.content.autoplay = False
c.input.partial_timeout = 0
c.input.insert_mode.auto_load = False
c.input.insert_mode.leave_on_load = True
c.input.insert_mode.plugins = False
c.input.insert_mode.auto_enter = True
c.input.insert_mode.auto_leave = True
c.keyhint.delay = 0
c.hints.uppercase = True
c.hints.auto_follow = 'always'

c.input.forward_unbound_keys = 'all'

config.bind(';s', 'hint paragraphs userscript run-mimic.sh')
config.bind(';S', 'spawn -d /home/boris/bin/i3/hint-qutebrowser.sh')
config.bind('m', 'hint paragraphs userscript run-mimic.sh')

config.bind(';p', 'hint pre userscript yank-pre.sh')
config.bind(';T', 'hint tables userscript yank-table.sh')

config.bind('..', 'repeat-command')

config.bind(';m', 'hint links spawn --detach mpv --x11-name=mpv {hint-url}')
config.bind(';x', 'spawn youtube-dl -o "/media/boris/d/Smth/%(title)s-%(id)s.%(ext)s" {url}')
config.bind(';M', 'spawn -d mpv --x11-name=mpv {url}')
config.bind(';P', 'spawn -d palemoon {url}')
config.bind(';F', 'spawn -d firefox {url}')

config.bind(';<Ctrl-E>', 'hint paragraphs userscript /home/boris/.local/share/qutebrowser/userscripts/run-gvim.sh')

config.bind(';v', 'hint paragraphs userscript /home/boris/.local/share/qutebrowser/userscripts/hint-caret.sh')
config.bind('f', 'hint paragraphs userscript /home/boris/.local/share/qutebrowser/userscripts/hint-caret.sh', mode='caret')

config.bind('o', 'set-cmd-text -s :open -r -t')
config.bind('O', 'set-cmd-text -s :open -r -b')
config.bind('cc', 'set-cmd-text -s :open')
config.bind('A', 'set-cmd-text -s :open -b')
config.bind('$', 'set-cmd-text -s :open -t')

config.bind('cu', 'edit-url')

config.bind('wH', 'back -w')
config.bind('wL', 'forward -w')
config.bind('wgu', 'navigate up -w')

# Insert mode page navigation
config.bind('<Ctrl-E>', 'scroll-page 0 0.05', mode='insert')
config.bind('<Ctrl-Y>', 'scroll-page 0 -0.05', mode='insert')
config.bind('<Ctrl-P>', 'fake-key <Up>', mode='insert')
config.bind('<Ctrl-N>', 'fake-key <Down>', mode='insert')
config.bind('<Ctrl-P>', 'fake-key <Up>', mode='normal')  # for normal mode compatibility
config.bind('<Ctrl-N>', 'fake-key <Down>', mode='normal')  # for normale mode compatibility
config.bind('<Ctrl-H>', 'fake-key <Backspace>', mode='insert')
config.bind('<Ctrl-W>', 'fake-key <Ctrl-Backspace>', mode='insert')
config.bind('<Ctrl-U>', 'fake-key <Shift-Home> ;; fake-key <Backspace>', mode='insert')

# Caret mode page navigation
config.bind('<Ctrl-F>', 'scroll-page 0 1', mode='caret')
config.bind('<Ctrl-B>', 'scroll-page 0 -1', mode='caret')
config.bind('<Ctrl-D>', 'scroll-page 0 0.5', mode='caret')
config.bind('<Ctrl-U>', 'scroll-page 0 -0.5', mode='caret')
config.bind('<Ctrl-E>', 'scroll-page 0 0.05', mode='caret')
config.bind('<Ctrl-Y>', 'scroll-page 0 -0.05', mode='caret')
config.bind('s', 'spawn --userscript run-mimic-caret.sh', mode='caret')
config.bind('m', 'spawn --userscript run-mimic-caret.sh', mode='caret')
config.bind('m', 'spawn --userscript run-mimic-caret.sh', mode='caret')
config.bind('-', 'zoom-out', mode='caret')
config.bind('=', 'zoom-in', mode='caret')

# Prompt mode page navigation
config.bind('<Ctrl-F>', 'scroll-page 0 1', mode='prompt')
config.bind('<Ctrl-B>', 'scroll-page 0 -1', mode='prompt')
config.bind('<Ctrl-D>', 'scroll-page 0 0.5', mode='prompt')
config.bind('<Ctrl-U>', 'scroll-page 0 -0.5', mode='prompt')
config.bind('<Ctrl-E>', 'scroll-page 0 0.05', mode='prompt')
config.bind('<Ctrl-Y>', 'scroll-page 0 -0.05', mode='prompt')

# Normal mode page navigation
config.bind('<Ctrl-E>', 'scroll-page 0 0.05')
config.bind('<Ctrl-Y>', 'scroll-page 0 -0.05')

# <Return> aliases
# TODO remove these after some testing
#config.bind('<Ctrl-J>', 'command-accept', mode='command')
#config.bind('<Ctrl-M>', 'command-accept', mode='command')
#config.bind('<Ctrl-J>', 'spawn /home/boris/.local/share/qutebrowser/userscripts/IM_C-j_C-m_dispatcher.sh {url:host} {url:port}', mode='insert')
#config.bind('<Ctrl-M>', 'spawn /home/boris/.local/share/qutebrowser/userscripts/IM_C-j_C-m_dispatcher.sh {url:host} {url:port}', mode='insert')
#config.bind('<Ctrl-M>', 'spawn /home/boris/.local/share/qutebrowser/userscripts/IM_C-j_C-m_dispatcher.sh {url:host} {url:port}', mode='insert')
#config.bind('<Ctrl-J>', 'selection-follow', mode='normal')
#config.bind('<Ctrl-J>', 'prompt-accept', mode='prompt')
#config.bind('<Ctrl-M>', 'prompt-accept', mode='prompt')
config.bind('<Return>', 'spawn /home/boris/.local/share/qutebrowser/userscripts/IM_return_dispatcher.sh {url:host} {url:port}', mode='insert')

# Tab switching
config.bind('<Ctrl-.>', 'tab-move +')
config.bind('<Ctrl-,>', 'tab-move -')
config.bind('<Ctrl-.>', 'tab-move +', mode='insert')
config.bind('<Ctrl-,>', 'tab-move -', mode='insert')
config.bind('<Ctrl-.>', 'tab-move +', mode='prompt')
config.bind('<Ctrl-,>', 'tab-move -', mode='prompt')

config.bind('<Alt-J>', 'tab-next', mode='normal')
config.bind('<Alt-K>', 'tab-prev', mode='normal')
config.bind('<Alt-H>', 'tab-prev', mode='normal')
config.bind('<Alt-L>', 'tab-next', mode='normal')
config.bind('<Alt-J>', 'tab-next', mode='insert')
config.bind('<Alt-K>', 'tab-prev', mode='insert')
config.bind('<Alt-H>', 'tab-prev', mode='insert')
config.bind('<Alt-L>', 'tab-next', mode='insert')
config.bind('<Alt-K>', 'tab-prev', mode='prompt')
config.bind('<Alt-L>', 'tab-next', mode='prompt')

for key_no in range(10):
    for mode in ['normal', 'insert', 'prompt']:
        tab_to_focus = " " + str(key_no) if key_no != 0 else " -1"
        tab_to_move = " " + str(key_no) if key_no != 0 else ""
        key_to_focus = '<Ctrl-{}>'.format(key_no)
        key_to_move = '<Alt-{}>'.format(key_no)
        command_to_focus = 'tab-focus{}'.format(tab_to_focus)
        command_to_move = 'tab-move{}'.format(tab_to_move)
        config.bind(key_to_focus, command_to_focus, mode=mode)
        config.bind(key_to_move, command_to_move, mode=mode)


# Tabs
config.bind('>', 'tab-move +')
config.bind('<<', 'tab-move -')
config.bind('><', 'tab-move')
config.bind('tG', 'set-cmd-text -s :tab-give')
config.bind('tT', 'set-cmd-text -s :tab-take')
config.bind('typ', 'tab-clone')
config.bind('tk', 'set tabs.position top')
config.bind('tj', 'set tabs.position bottom')
config.bind('th', 'set tabs.position left')
config.bind('tl', 'set tabs.position right')
config.bind('tt', 'config-cycle -p tabs.show always switching')
config.bind('tw', 'open -r -t http://127.0.0.1:8081/')
config.bind('t--', 'set-cmd-text -s :set tabs.width')
config.bind('tH', 'back -t')
config.bind('tL', 'forward -t')
config.bind('tgu', 'navigate up -t')
config.bind('<Space>d', 'tab-close')
config.bind('x', 'tab-close')
config.bind('F3', 'tab-close')
config.bind('s', 'spawn /home/boris/.local/share/qutebrowser/userscripts/NM_s_dispatcher.sh {url:host} {url:port}')  # special hinting for tiddlywiki
config.bind('X', 'tab-close -o')
config.bind('!x', 'tab-only')

# Downloads
config.bind('Du', 'download-cancel')
config.bind('D<Ctrl-R>', 'download-retry')
config.bind('Ddd', 'download-clear')
config.bind('DZQ', 'download-delete')
config.bind('DZZ', 'download-remove')
config.bind('DD', 'download-open')
config.bind('Dk', 'set downloads.position top')
config.bind('Dj', 'set downloads.position bottom')
config.bind('Dh', 'set downloads.position left')
config.bind('Dl', 'set downloads.position right')

config.bind(';k', 'hint alll delete')
config.bind(';a', 'hint alll')

config.bind('<Shift-Return>', 'hint-follow -s {hint-url}', mode='hint')

# Tiddlywiki
# XXX state for keydrown
config.bind('<Escape>', 'mode-leave ;; set input.spatial_navigation false ;; jseval -q -w main window.qutebrowserMode = "normal";', mode='insert')
config.bind('<Ctrl-G>', 'mode-leave ;; set input.spatial_navigation false ;; jseval -q -w main window.qutebrowserMode = "normal";', mode='insert')
config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave ;; fake-key --global _c020_c021', mode='normal') # Added a fake click on a dummy <div> (see 'dunder' bindings) to get rid of the fucking sticky dropdowns

config.bind('<Ctrl-C><Ctrl-V>', 'edit-text', mode='insert')

config.bind('tn', 'config-cycle -p input.spatial_navigation true false', mode='normal')
config.bind('gg', 'scroll-to-perc 0')
config.bind('G', 'scroll-to-perc 100')

config.unbind('<Ctrl-V>')
config.bind('<Ctrl-Shift-V>', 'mode-enter passthrough')

config.bind('<Ctrl-G>', 'clear-keychain ;; search ;; fullscreen --leave ;; fake-key --global _c020_c021', mode='normal')
config.bind('<Ctrl-G>', 'mode-leave', mode='caret')
config.bind('<Ctrl-G>', 'mode-leave', mode='command')
config.bind('<Ctrl-G>', 'mode-leave', mode='hint')
config.bind('<Ctrl-G>', 'mode-leave', mode='prompt')
config.bind('<Ctrl-G>', 'mode-leave', mode='register')
config.bind('<Ctrl-G>', 'mode-leave', mode='yesno')

# Evil-escape
config.bind('jk', 'mode-leave', mode='yesno')
config.bind('jk', 'mode-leave', mode='hint')

config.bind('<Ctrl-O>', 'fake-key <Return> ;; fake-key <Up> ;; fake-key <End>', mode='insert')
config.bind('<Ctrl-I>', 'fake-key <Tab>', mode='insert')  # tab (bash/ASCII ^I)
config.bind('<Ctrl-Alt-D>', 'fake-key <Shift-Tab>', mode='insert')  # 'de-tab'/dedent (vim)
config.bind('<Ctrl-D>', 'fake-key <Del>', mode='insert')
config.bind('<Alt-D>', 'fake-key <Ctrl-Del>', mode='insert')
config.bind('<Ctrl-F>', 'fake-key <Right>', mode='insert')
config.bind('<Ctrl-B>', 'fake-key <Left>', mode='insert')
config.bind('<Alt-F>', 'fake-key <Ctrl-Right>', mode='insert')
config.bind('<Alt-B>', 'fake-key <Ctrl-Left>', mode='insert')
config.bind('<Ctrl-K>', 'fake-key <Shift-End> ;; fake-key <Del>', mode='insert')  # kill line forward (emacs/readline)
config.bind('<Ctrl-/>', 'fake-key <Ctrl-Z> ;; fake-key <Left> ;; fake-key <Right>', mode='insert') # undo (bash)

config.bind('<Alt-W>', 'fake-key <Ctrl-Insert>', mode='insert')
config.bind('<Alt-Y>', 'fake-key <Shift-Insert>', mode='insert')

config.bind('<Alt-U>', 'fake-key <Shift-Home> ;; fake-key <Del> ;; fake-key <Backspace> ;; fake-key <Ctrl-[>', mode='insert')
config.bind('<Alt-O>', 'fake-key <End> ;; fake-key <Return>', mode='insert')

config.bind('<Alt-A>', 'fake-key <Ctrl-Home>', mode='insert')
config.bind('<Alt-E>', 'fake-key <Ctrl-End>', mode='insert')
config.bind('<Ctrl-Alt-A>', 'fake-key <Home>', mode='insert')
config.bind('<Ctrl-Alt-E>', 'fake-key <End>', mode='insert')

# Tab key replacement
config.bind('<Ctrl-I>', 'fake-key <Tab>', mode='normal')
config.bind('<Ctrl-Alt-I>', 'fake-key <Shift-Tab>', mode='normal')
config.bind('<Ctrl-Alt-I>', 'fake-key <Shift-Tab>', mode='insert')
config.bind('<Ctrl-I>', 'prompt-item-focus next', mode='prompt')
config.bind('<Ctrl-Alt-I>', 'prompt-item-focus prev', mode='prompt')
config.bind('<Ctrl-I>', 'completion-item-focus next', mode='command')
config.bind('<Ctrl-Alt-I>', 'completion-item-focus prev', mode='command')

config.bind('=', 'zoom-in', mode='normal')

config.bind('gh', 'tab-prev', mode='normal')
config.bind('gj', 'tab-next', mode='normal')
config.bind('gk', 'tab-prev', mode='normal')
config.bind('gl', 'tab-next', mode='normal')
config.bind('<Space>h', 'tab-prev', mode='normal')
config.bind('<Space>j', 'tab-next', mode='normal')
config.bind('<Space>k', 'tab-prev', mode='normal')
config.bind('<Space>l', 'tab-next', mode='normal')
config.bind('<Ctrl-H>', 'tab-prev', mode='normal')
config.bind('<Ctrl-J>', 'tab-next', mode='normal')
config.bind('<Ctrl-K>', 'tab-prev', mode='normal')
config.bind('<Ctrl-L>', 'tab-next', mode='normal')

config.bind('y', 'yank selection --keep', mode='caret')
config.bind('<Ctrl-Y>', 'yank selection', mode='caret')

config.set('tabs.close_mouse_button_on_bar', 'close-current')

config.bind('g.','set-cmd-text :')
config.bind('g,','set-cmd-text :')
config.bind('<Space><Space>','set-cmd-text :')
config.bind('go','open -r -t ;; set-cmd-text :')

config.bind('<Ctrl-S>5', 'height=50%', mode='command')
c.aliases['height=50%'] = 'set completion.height 50%'
config.bind('<Ctrl-S>2', 'height=20%', mode='command')
c.aliases['height=20%'] = 'set completion.height 20%'
config.bind('<Ctrl-S>0', 'height=0%', mode='command')
c.aliases['height=0%'] = 'set completion.height 0%'
config.bind('<Ctrl-S>s', 'shrink', mode='command')
c.aliases['shrink'] = 'config-cycle completion.shrink true false'

config.bind('<Ctrl-W>', 'rl-backward-kill-word', mode='command')
config.bind('<Ctrl-W>', 'rl-backward-kill-word ;; rl-backward-kill-word', mode='prompt')

config.bind(",",'spawn -d /home/boris/.local/share/qutebrowser/userscripts/NM_comma_dispatcher.sh {url:host} {url:port}')

# this is an (working) example of how you can make complex commands more readable
# config.bind('a', 'spawn\
#                   xdotool\
#                   type\
#                   _dtw')

config.bind(',', 'mode-leave ;; spawn /home/boris/.local/share/qutebrowser/userscripts/NM_comma_dispatcher.sh {url:host} {url:port}', mode='hint')
config.bind('jt', "config-cycle colors.hints.bg 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 247, 133, 0.8), stop:1 rgba(255, 197, 66, 0.8))' 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 247, 133, 0.2), stop:1 rgba(255, 197, 66, 0.2))' ;; config-cycle colors.hints.fg black 'rgba(0, 0, 0, 0.2)", mode='hint')

# XXX state for keydrown
config.bind('i', 'mode-enter insert ;; jseval -q -w main window.qutebrowserMode = "insert";')
config.bind('gi', 'hint inputs --first ;; jseval -q -w main window.qutebrowserMode = "insert";')
config.bind(';t', 'fake-key --global _c030_c031')

config.bind('td', 'spawn --userscript /home/boris/.local/share/qutebrowser/userscripts/toggle-keydrown.sh')

config.bind('<\><Space>', 'space')
c.aliases['space'] = 'fake-key <Space>'

config.bind('wi', 'fake-key --global _c010 ;; fake-key --global _c013 ;; fake-key --global _c011')

# smacemacs-style bindings
config.bind('<Space>bb', 'list_tabs')
c.aliases['list_tabs'] = 'set-cmd-text -s :tab-select'
config.bind('<Space>01', 'tab-focus 1')
config.bind('<Space>q', 'tab-focus 1')
config.bind('<Space>02', 'tab-focus 2')
config.bind('<Space>3', 'tab-focus 3')
config.bind('<Space>4', 'tab-focus 4')
config.bind('<Space>5', 'tab-focus 5')
config.bind('<Space>6', 'tab-focus 6')
config.bind('<Space>7', 'tab-focus 7')
config.bind('<Space>8', 'tab-focus 8')
config.bind('<Space>9', 'tab-focus 9')
config.bind('<Space>10', 'tab-focus 10')
config.bind('<Space>11', 'tab-focus 11')
config.bind('<Space>12', 'tab-focus 12')
config.bind('<Space>13', 'tab-focus 13')
config.bind('<Space>14', 'tab-focus 14')
config.bind('<Space>15', 'tab-focus 15')
config.bind('<Space>16', 'tab-focus 16')
config.bind('<Space>17', 'tab-focus 17')
config.bind('<Space>18', 'tab-focus 18')
config.bind('<Space>19', 'tab-focus 19')
config.bind('<Space>20', 'tab-focus 20')
config.bind('<Space>21', 'tab-focus 21')
config.bind('<Space>22', 'tab-focus 22')
config.bind('<Space>23', 'tab-focus 23')
config.bind('<Space>24', 'tab-focus 24')
config.bind('<Space>25', 'tab-focus 25')
config.bind('<Space>26', 'tab-focus 26')
config.bind('<Space>27', 'tab-focus 27')
config.bind('<Space>28', 'tab-focus 28')
config.bind('<Space>29', 'tab-focus 29')
config.bind('<Space>$', 'tab-focus -1')
config.bind('<Space>-1', 'tab-focus -1')
config.bind('<Space>-2', 'tab-focus -2')
config.bind('<Space>-3', 'tab-focus -3')
config.bind('<Space>-4', 'tab-focus -4')
config.bind('<Space>-5', 'tab-focus -5')
config.bind('<Space>-6', 'tab-focus -6')
config.bind('<Space>-7', 'tab-focus -7')
config.bind('<Space>-8', 'tab-focus -8')
config.bind('<Space>-9', 'tab-focus -9')
c.aliases['last_tab'] = 'tab-focus last'
config.bind('<Space><Tab>', 'last_tab')
config.bind('<Space><Ctrl-I>', 'last_tab')
config.bind('<Space>fed', 'config-edit')
config.bind('<Space>fe<Shift-R>', 'config-source')
c.keyhint.blacklist.append('<Space>-*')
c.keyhint.blacklist.append('<Space>0*')
c.keyhint.blacklist.append('<Space>1*')
c.keyhint.blacklist.append('<Space>2*')
c.keyhint.blacklist.append('<Space>3')
c.keyhint.blacklist.append('<Space>4')
c.keyhint.blacklist.append('<Space>5')
c.keyhint.blacklist.append('<Space>6')
c.keyhint.blacklist.append('<Space>7')
c.keyhint.blacklist.append('<Space>8')
c.keyhint.blacklist.append('<Space>9')
c.keyhint.blacklist.append('<Space>$')
c.keyhint.blacklist.append('<Space>q')
c.keyhint.blacklist.append('<Space>-*')

c.content.blocking.method = 'both'

c.fonts.default_size = '13pt'
c.zoom.default = '130%'
c.fonts.hints = 'bold 15pt default_family'
c.content.pdfjs = False
c.keyhint.radius = 0
c.fonts.keyhint = 'bold default_size default_family'
c.hints.radius = 0

c.window.title_format = "{id}{title_sep}{perc}{current_title}{title_sep}qutebrowser"
c.content.notifications = False # globally turn off notifications, hoping that it will fix the service worker problem

c.fileselect.handler = 'external'
c.fileselect.multiple_files.command = ["/home/boris/kitty/kitty/launcher/kitty", "--class", "Gvim", "-e", "ranger", "--choosefile={}"]
c.fileselect.single_file.command = ["/home/boris/kitty/kitty/launcher/kitty", "--class", "Gvim", "-e", "ranger", "--choosefile={}"]

c.qt.workarounds.remove_service_workers = True

c.aliases['cure-keydrown'] = 'jseval -q -w main kd.stop(); kd.run(function () {kd.tick();});'
config.bind('ck', 'cure-keydrown')
config.bind('cm', 'clear-messages')

c.aliases['bm'] = 'quit --save'

config.bind('r', 'hint paragraphs userscript run-rhvoice.sh')
c.zoom.mouse_divider = 2048
