
try:
    from termcolor import colored
except Exception:
    # Graceful fallback if termcolor missing
    def colored(text, color=None):
        return str(text)

def log_indicator(name, value, status="neutral"):
    color = "yellow"
    if status == "bullish":
        color = "green"
    elif status == "bearish":
        color = "red"
    print(colored(f"{name:<18}: {value}", color), flush=True)

def log_balance(usdt=None, coin=None, coin_symbol='COIN'):
    if usdt is not None:
        print(colored(f"USDT Balance        : {usdt}", "cyan"), flush=True)
    if coin is not None:
        print(colored(f"{coin_symbol} Balance     : {coin}", "magenta"), flush=True)

def color_rsi(rsi):
    if rsi is None:
        return "yellow"
    if rsi >= 70:
        return "red"
    if rsi <= 30:
        return "blue"
    return "green"

# Ensure unbuffered stdout at runtime (Render friendly)
import os, sys
os.environ.setdefault("PYTHONUNBUFFERED", "1")
try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass
