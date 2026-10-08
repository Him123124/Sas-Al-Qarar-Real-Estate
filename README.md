# Sas Al-Qarar Real Estate – website

Dark cyan (#0b6b73) and beige (#efe6d3). Arabic by default, English toggle, light/dark theme.

- `index.html`, `services.html`, `contact.html` – pages
- `css/style.css` – all styling
- `js/main.js` – language, theme, menu, animations, form
- `images/` – logo, favicon, hero illustration (SVG)
- `server.py` – optional Python server; saves contact messages to `data/messages.jsonl`

## Run
- Quick look: open `index.html` in a browser (the form then falls back to WhatsApp).
- With saving: `python3 server.py` and open http://localhost:8000
- Hosting: upload the folder to any static host; use `server.py` only if you want to store messages yourself.

`build.py` regenerates the three HTML pages from one template.
