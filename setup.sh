#!/usr/bin/env bash
set -e

echo "=================================="
echo " FXP SETUP INSTALLER"
echo "=================================="

# -----------------------------
# 1. Python
# -----------------------------

if ! command -v python3.11 &> /dev/null; then
    echo "[ERROR] Python 3.11 no encontrado"
    exit 1
fi

echo "[INFO] Python: $(python3.11 --version)"

# -----------------------------
# 2. Venv
# -----------------------------

if [ ! -d ".venv" ]; then
    echo "[INFO] Creando entorno virtual..."
    python3.11 -m venv .venv
else
    echo "[INFO] .venv ya existe"
fi

# -----------------------------
# 3. Activar SOLO para instalación
# -----------------------------

echo "[INFO] Activando entorno virtual (temporal)..."
source .venv/bin/activate

# -----------------------------
# 4. Install
# -----------------------------

pip install --upgrade pip
pip install -e .

# -----------------------------
# 5. Detectar shell SOLO para instrucción
# -----------------------------

SHELL_NAME=$(basename "$SHELL")

echo ""
echo "=================================="
echo "SETUP COMPLETADO ✔"
echo "=================================="

echo "[INFO] Para activar el entorno usa:"

case "$SHELL_NAME" in
    fish)
        echo "  source .venv/bin/activate.fish"
        ;;
    *)
        echo "  source .venv/bin/activate"
        ;;
esac

echo "=================================="