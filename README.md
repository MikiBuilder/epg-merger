# 📺 EPG Merger

Combina automáticamente múltiples fuentes EPG (Electronic Program Guide) en un único archivo XML limpio y ordenado.

Se ejecuta **una vez al día** mediante GitHub Actions, sin necesidad de ningún servidor.

---

## 📦 Archivos generados

| Archivo | Descripción |
|---|---|
| `merged.xml` | EPG unificado listo para usar en cualquier reproductor IPTV (publicado en Releases) |
| `channels.txt` | Lista con todos los canales y el total |

---

## 📥 Descarga directa

| Archivo | Enlace |
|---|---|
| `merged.xml` | [⬇️ Descargar](https://github.com/MikiBuilder/epg-merger/releases/download/latest/merged.xml) |
| `channels.txt` | [⬇️ Descargar](https://raw.githubusercontent.com/MikiBuilder/epg-merger/main/channels.txt) |

---

## 🔗 URL para cliente IPTV

```
https://github.com/MikiBuilder/epg-merger/releases/download/latest/merged.xml
```

---

## 📡 Fuentes EPG incluidas

| Fuente | Descripción |
|---|---|
| [EPG dobleM](https://github.com/davidmuma/EPG_dobleM) | Guía IPTV en español |
| [PlutoTV (all)](https://github.com/matthuisman/i.mjh.nz) | Canales PlutoTV globales |
| [SamsungTV+ ES](https://github.com/matthuisman/i.mjh.nz) | Canales Samsung TV+ España |
| [Plex ES](https://github.com/matthuisman/i.mjh.nz) | Canales Plex España |

---

## ⚙️ Cómo funciona

1. GitHub Actions lanza `scraper.py` cada día a las **06:00 UTC**
2. Descarga cada fuente EPG
3. Elimina canales duplicados (por ID)
4. Genera el XML con **todos los canales primero** y luego **todos los programas**
5. Publica `merged.xml` en **GitHub Releases** (sin límite de tamaño)
6. Guarda `channels.txt` en el repositorio

---

## 🚀 Instalación local (opcional)

```bash
git clone https://github.com/MikiBuilder/epg-merger.git
cd epg-merger
pip install -r requirements.txt
python scraper.py
```

---

## 🔁 Ejecutar manualmente en GitHub

Ve a **Actions → EPG Merger → Run workflow** para lanzarlo en cualquier momento.

---

## 📝 Licencia

MIT — libre para uso personal.
