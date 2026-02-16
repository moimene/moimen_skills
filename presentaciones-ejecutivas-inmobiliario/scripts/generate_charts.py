"""
Genera gráficos rápidos para el teaser:
- take-up vs vacancy (líneas)
- absorción por calidad (barras apiladas)

Salida por defecto:
  assets/charts/sample_takeup_vacancy.png
  assets/charts/sample_absorption_grade.png

Requisitos: matplotlib instalado.
"""

from pathlib import Path
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "assets" / "charts"


def takeup_vs_vacancy():
    years = list(range(2020, 2031))
    takeup_22 = [180, 190, 150, 160, 200, 240, 260, 280, 300, 310, 320]
    takeup_total = [320, 340, 300, 310, 360, 400, 420, 430, 440, 450, 460]
    vacancy = [12, 14, 15, 13, 11, 9, 8, 7.5, 7, 6.8, 6.5]

    fig, ax1 = plt.subplots(figsize=(8, 4.5))
    ax1.plot(years, takeup_22, label="22@ Take-up (k sqm)", color="#1f2a38", linewidth=2.2)
    ax1.plot(years, takeup_total, label="Barcelona Take-up (k sqm)", color="#6b7c8e", linewidth=2.0, linestyle="--")
    ax1.set_ylabel("Take-up (k sqm)")
    ax1.set_xlabel("Year")
    ax1.grid(axis="y", alpha=0.25)

    ax2 = ax1.twinx()
    ax2.plot(years, vacancy, label="Vacancy %", color="#e97500", linewidth=2.2, marker="o")
    ax2.set_ylabel("Vacancy (%)")

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc="upper left")

    fig.tight_layout()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / "sample_takeup_vacancy.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)
    print(f"Guardado {out}")


def absorption_by_grade():
    grades = ["A", "B+", "B", "C"]
    absorption = [65, 18, 12, 5]
    colors = ["#1f2a38", "#50627a", "#8090a3", "#b8c1c9"]

    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.bar(grades, absorption, color=colors)
    ax.set_ylabel("Absorción (%)")
    ax.set_title("Absorción por calidad (ejemplo)")
    for x, y in zip(grades, absorption):
        ax.text(x, y + 1, f"{y}%", ha="center", va="bottom", fontsize=10)
    ax.set_ylim(0, 80)
    ax.grid(axis="y", alpha=0.2)

    fig.tight_layout()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / "sample_absorption_grade.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)
    print(f"Guardado {out}")


def main():
    takeup_vs_vacancy()
    absorption_by_grade()


if __name__ == "__main__":
    main()
